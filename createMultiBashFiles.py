import argparse, subprocess, os

parser = argparse.ArgumentParser(description = 'Generate Bash scripts for EPOS-LHC Generation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--nfiles', type=int, help='Number of HepMC files to create per batch', default=500)
parser.add_argument('--nevts', type=int, help='Number of events per file', default=4000)
parser.add_argument('--scramarch', type=str, help='SCRAM architecture of system', default='slc7_amd64_gcc700')
parser.add_argument('--workdir', type=str, help='working directory (should be your cmssw/src)', default='/afs/cern.ch/work/w/wvetens/Sexaquarks/CMSSW_10_2_26/src')
parser.add_argument('--gfal_prefix', type=str, help='Your T2 prefix for gfal', default='davs://cmsxrootd.hep.wisc.edu:1094')
parser.add_argument('--trialname', type=str, help='name of trial (note, to change the mass in the simulation in crmc_Sexaq_incl_installed go to crmc.param and at the end of the file add the line "setamhdibar m_x" where m_x is the desire S mass you want to generate', default="0_1p8GeV")
parser.add_argument('--batchnum', type=int, help='number of batches', default=2)
parser.add_argument('--pwstdin', type=str, help='path of fil with password standin for voms', default="~/pwstdin")
parser.add_argument('--user', type=str, help='your username on lxplus and your T2', default="wvetens")

args = parser.parse_args()

#number of files to create
for batch in range(0, args.batchnum):
    if not os.path.exists("condor/" + args.trialname + "/" + str(batch)):
        os.makedirs("condor/" + args.trialname + "/" + str(batch))
    if not os.path.exists("shell/" + args.trialname + "/" + str(batch)):
        os.makedirs("shell/" + args.trialname + "/" + str(batch))
    for i in range(0,args.nfiles):
    	
    	file = open("shell/" + args.trialname + '/' + str(batch) + '/' + str(i) + ".sh","w") 
    	#CMSSW stuff
    	file.write("#!/bin/bash" + "\n")
    	file.write("source /cvmfs/cms.cern.ch/cmsset_default.sh" + "\n")
    	file.write("export SCRAM_ARCH=" + args.scramarch + "\n")
    	file.write("cd " + args.workdir + " ; eval `scram runtime -sh` ; cd - >/dev/null" + "\n")
        #info for debugging purposes
        file.write("echo 'ENVIRONMENT BEGIN:'\n")
        file.write("env\n")
        file.write("echo 'ENVIRONMENT END'\n")
        file.write("echo 'LDD BEGIN:'\n")
        file.write("ldd /afs/cern.ch/work/w/wvetens/Sexaquarks/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/bin/crmc\n")
        file.write("echo 'LDD END'\n")
        #debug end
    	#proxy to be able to write the files to /pnfs
        file.write("export X509_USER_PROXY=/tmp/x509up_u$(id -u $USER)" + "\n")
        file.write("voms-proxy-init -voms cms -pwstdin < " + args.pwstdin + "\n")
    	#create dir for output files
    	file.write("cd " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed" + "\n")
    	file.write("mkdir -p " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/" + args.trialname + "/" + str(batch) + "/" + "\n")
    	file.write("mkdir -p " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/" + args.trialname + "/" + str(batch) + "/" + "\n")
    	#run EPOS
    	file.write(args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/bin/crmc -S13000 -n" + str(args.nevts) + " -m0 -f " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_"+str(i)+".hepmc" + "\n")
    	#convert hepmc to EDM
    	file.write("cmsRun " + args.workdir + "/IOMC/Input/test/hepmc2gen.py print inputFiles=file:" + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".hepmc outputFile=file:" + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".root" + "\n")
    	#remove hepmc file
    	file.write("rm " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".hepmc" + "\n")
    	#prepare to move to pnfs
    	file.write("(eval `scram unsetenv -sh`; gfal-mkdir " + args.gfal_prefix + "/store/user/" + args.user + "/crmc_Sexaq/crmc/Sexaquark_13TeV_trial_"+ args.trialname + "/" + str(batch) + " >/dev/null)"+"\n")
    	#sometimes the copy failed the first time so therefore I put it twice ...
    	file.write("(eval `scram unsetenv -sh`; gfal-copy " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".root " + args.gfal_prefix + "/store/user/" + args.user + "/crmc_Sexaq/crmc/Sexaquark_13TeV_trial_" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".root)" + "\n")
    	file.write("(eval `scram unsetenv -sh`; gfal-copy " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".root " + args.gfal_prefix + "/store/user/" + args.user + "/crmc_Sexaq/crmc/Sexaquark_13TeV_trial_" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".root)" + "\n")
    	#its now on /pnfs so I can remove
    	file.write("rm " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/" + args.trialname + "/" + str(batch) + "/crmc_Sexaq_" + str(i) + ".root " + "\n")
    	file.close()
        #subprocess.call(str("chmod +x shell/" + args.trialname + "/" + str(batch) + "/" + str(i) + ".sh").split(), shell=True)
    
    file2 = open("condor/" + args.trialname + "/" + str(batch) + "/condor_multiple.cfg", "w")
    file2.write("Universe = vanilla\n")
    file2.write("Executable = " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/CRMCSexaqSim/shell/" + args.trialname + "/" + str(batch) + "/$(ProcID).sh\n")
    file2.write("x509userproxy = " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/CRMCSexaqSim/userproxy\n")
    file2.write("use_x509userproxy = True\n")
    file2.write("Log        = " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/CRMCSexaqSim/condor/" + args.trialname + "/" + str(batch) + "/log/$(ProcID).log\n")
    file2.write("Output     = " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/CRMCSexaqSim/condor/" + args.trialname + "/" + str(batch) + "/out/$(ProcID).out\n")
    file2.write("Error      = " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/CRMCSexaqSim/condor/" + args.trialname + "/" + str(batch) + "/error/$(ProcID).error\n")
    file2.write("should_transfer_files = Yes\n")
    file2.write("when_to_transfer_output = ON_EXIT\n")
    file2.write("getenv     = True\n")
    file2.write("request_cpus = 4\n")
    file2.write("+JobFlavour = \"nextweek\"\n")
    file2.write("\n")
    file2.write("queue " + str(args.nfiles) + "\n")
    file2.close()
