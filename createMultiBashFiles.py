trial = "27_1p8GeV"

#number of files to create
for i in range(0,1000):
	
	file = open("shell/"+str(i)+".sh","w") 
	#CMSSW stuff
	file.write("source $VO_CMS_SW_DIR/cmsset_default.sh"+"\n")
	file.write("export SCRAM_ARCH=slc6_amd64_gcc481"+"\n")
	file.write("cd /user/jdeclerc/CMSSW_7_1_20_patch2/src ; eval `scram runtime -sh` ; cd - >/dev/null" + "\n")
	#proxy to be able to write the files to /pnfs
        file.write("export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER)"+"\n")
        file.write("export X509_USER_PROXY=/tmp/x509up_u20641"+"\n")
        file.write("voms-proxy-init -pwstdin < /storage_mnt/storage/user/jdeclerc/CMSSW_8_0_30/src/STEP1_STEP2_Skimming_FlatTree/qsub/password"+"\n")
	#create dir for output files
	file.write("cd /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed" +"\n")
	file.write("mkdir /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/"+"\n")
	file.write("mkdir /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/"+"\n")
	#run EPOS
	file.write("/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/bin/crmc -S13000 -n4000 -m0 -f /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_"+str(i)+".hepmc"+"\n")
	#convert hepmc to EDM
	file.write("cmsRun /user/jdeclerc/CMSSW_7_1_20_patch2/src/IOMC/Input/test/hepmc2gen.py print inputFiles=file:/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_" + str(i)+".hepmc outputFile=file:/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_"+str(i)+".root"+"\n")
	#remove hepmc file
	file.write("rm /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_"+str(i)+".hepmc"+"\n")
	#prepare to move to pnfs
	file.write("gfal-mkdir srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/crmc/Sexaquark_13TeV_trial"+ str(trial) + " 2>/dev/null"+"\n")
	#sometimes the copy failed the first time so therefore I put it twice ...
	file.write("gfal-copy /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_"+str(i)+".root "+ "srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/crmc/Sexaquark_13TeV_trial"+str(trial) +"\n")
	file.write("gfal-copy /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_"+str(i)+".root "+ "srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/crmc/Sexaquark_13TeV_trial"+str(trial) +"\n")
	#its now on /pnfs so I can remove
	file.write("rm /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_"+str(i)+".root "+"\n")
	file.close()

