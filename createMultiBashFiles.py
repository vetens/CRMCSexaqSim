

for i in range(1,10000):
	file = open("shell_with_antiS_eta_cut/"+str(i)+".sh","w") 
#	file.write("#!/bin/bash"+"\n")
#	file.write("cd /afs/cern.ch/user/j/jdeclerc/CMSSW_9_4_7/src/"+"\n")
#	file.write("cmsenv"+"\n")

	file.write("source $VO_CMS_SW_DIR/cmsset_default.sh"+"\n")
	file.write("export SCRAM_ARCH=slc6_amd64_gcc481"+"\n")
	file.write("cd /user/jdeclerc/CMSSW_7_1_20_patch2/src ; eval `scram runtime -sh` ; cd - >/dev/null" + "\n")

	file.write("export X509_USER_PROXY=/tmp/x509up_u20641"+"\n")
	


	file.write("cd /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed" +"\n")
	file.write("mkdir /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/"+"\n")
	file.write("mkdir /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/"+"\n")

	file.write("/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/bin/crmc -S13000 -n1000 -m0 -f /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_"+str(i)+".hepmc"+"\n")
	file.write("cmsRun /user/jdeclerc/CMSSW_7_1_20_patch2/src/IOMC/Input/test/hepmc2gen.py print inputFiles=file:/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_" + str(i)+".hepmc outputFile=file:/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_"+str(i)+".root"+"\n")
	file.write("rm /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_"+str(i)+".hepmc"+"\n")
	#file.write("gfal-mkdir srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/Sexaquark_13TeV_trial4 2>/dev/null"+"\n")
	#file.write("gfal-copy ./crmc_Sexaq_"+str(i)+".hepmc "+ "srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/Sexaquark_13TeV_trial4" +"\n")
	#file.write("rm ./crmc_Sexaq_"+str(i)+".hepmc"+"\n")
	file.close()

