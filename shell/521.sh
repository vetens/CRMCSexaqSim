source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
cd /user/jdeclerc/CMSSW_7_1_20_patch2/src ; eval `scram runtime -sh` ; cd - >/dev/null
export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER)
export X509_USER_PROXY=/tmp/x509up_u20641
voms-proxy-init -pwstdin < /storage_mnt/storage/user/jdeclerc/CMSSW_8_0_30/src/STEP1_STEP2_Skimming_FlatTree/qsub/password
cd /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed
mkdir /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/
mkdir /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/
/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/bin/crmc -S13000 -n4000 -m0 -f /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_521.hepmc
cmsRun /user/jdeclerc/CMSSW_7_1_20_patch2/src/IOMC/Input/test/hepmc2gen.py print inputFiles=file:/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_521.hepmc outputFile=file:/user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_521.root
rm /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_521.hepmc
gfal-mkdir srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/crmc/Sexaquark_13TeV_trial27_1p8GeV 2>/dev/null
gfal-copy /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_521.root srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/crmc/Sexaquark_13TeV_trial27_1p8GeV
gfal-copy /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_521.root srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/crmc/Sexaquark_13TeV_trial27_1p8GeV
rm /user/jdeclerc/Analysis/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_521.root 
