import argparse

parser = argparse.ArgumentParser(description = 'Generate Bash scripts for EPOS-LHC Generation')
parser.add_argument('--nfiles', type=int, help='Number of HepMC files to create', default=1000)
parser.add_argument('--nevts', type=int, help='Number of events per file', default=4000)
parser.add_argument('--scramarch', type=str, help='SCRAM architecture of system', default='slc7_amd64_gcc700')
parser.add_argument('--workdir', type=str, help='working directory (should be your cmssw/src)', default='/afs/cern.ch/work/w/wvetens/Sexaquarks/CMSSW_10_2_26/src')
parser.add_argument('--gfal_prefix', type=str, help='Your T2 prefix for gfal', default='davs://cmsxrootd.hep.wisc.edu:1094')
parser.add_argument('--trialname', type=str, help='name of trial (note, to change the mass in the simulation in crmc_Sexaq_incl_installed go to crmc.param and at the end of the file add the line "setamhdibar m_x" where m_x is the desire S mass you want to generate', default="27_1p8GeV")
parser.add_argument('--pwstdin', type=str, help='path of fil with password standin for voms', default="~/pwstdin")
parser.add_argument('--user', type=str, help='your username on lxplus and your T2', default="wvetens")

args = parser.parse_args()

#number of files to create
for i in range(0,args.nfiles):
	
	file = open("shell/" + str(i) + ".sh","w") 
	#CMSSW stuff
	file.write("source /cvmfs/cms.cern.ch/cmsset_default.sh" + "\n")
	file.write("export SCRAM_ARCH=" + args.scramarch + "\n")
	file.write("cd " + args.workdir + " ; eval `scram runtime -sh` ; cd - >/dev/null" + "\n")
	#proxy to be able to write the files to /pnfs
        file.write("export X509_USER_PROXY=/tmp/x509up_u$(id -u $USER)" + "\n")
        file.write("voms-proxy-init -pwstdin < " + args.pwstdin + "\n")
	#create dir for output files
	file.write("cd " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed" + "\n")
	file.write("mkdir -p " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/" + "\n")
	file.write("mkdir -p " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/" + "\n")
	#run EPOS
	file.write(args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/bin/crmc -S13000 -n" + str(args.nevts) + " -m0 -f " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_"+str(i)+".hepmc" + "\n")
	#convert hepmc to EDM
	file.write("cmsRun " + args.workdir + "/IOMC/Input/test/hepmc2gen.py print inputFiles=file:" + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_" + str(i) + ".hepmc outputFile=file:" + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_" + str(i) + ".root" + "\n")
	#remove hepmc file
	file.write("rm " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_" + str(i) + ".hepmc" + "\n")
	#prepare to move to pnfs
	file.write("gfal-mkdir " + args.gfal_prefix + "/store/user/" + args.user + "/crmc_Sexaq/crmc/Sexaquark_13TeV_trial"+ args.trialname + " 2>/dev/null"+"\n")
	#sometimes the copy failed the first time so therefore I put it twice ...
	file.write("gfal-copy " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_" + str(i) + ".root " + args.gfal_prefix + "/store/user/" + args.user + "/crmc_Sexaq/crmc/Sexaquark_13TeV_trial" + args.trialname + "\n")
	file.write("gfal-copy " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_" + str(i) + ".root " + args.gfal_prefix + "/store/user/" + args.user + "/crmc_Sexaq/crmc/Sexaquark_13TeV_trial" + args.trialname + "\n")
	#its now on /pnfs so I can remove
	file.write("rm " + args.workdir + "/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_" + str(i) + ".root " + "\n")
	file.close()

