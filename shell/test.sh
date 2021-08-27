source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cd /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src ; eval `scram runtime -sh` ; cd - >/dev/null
export X509_USER_PROXY=/tmp/x509up_u$(id -u $USER)
voms-proxy-init -voms cms -pwstdin < ~/pwstdin
cd /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed
mkdir -p /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/
mkdir -p /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/
/afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/bin/crmc -S13000 -n10 -m0 -f /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_0.hepmc
cmsRun /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/IOMC/Input/test/hepmc2gen.py print inputFiles=file:/afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_0.hepmc outputFile=file:/afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_0.root
rm /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/tmp/crmc_Sexaq_0.hepmc

(eval `scram unsetenv -sh`; gfal-mkdir davs://cmsxrootd.hep.wisc.edu:1094/store/user/wvetens/crmc_Sexaq/crmc/Sexaquark_13TeV_trial_test_1p8GeV >/dev/null)
(eval `scram unsetenv -sh`; gfal-copy /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_0.root davs://cmsxrootd.hep.wisc.edu:1094/store/user/wvetens/crmc_Sexaq/crmc/Sexaquark_13TeV_trial_test_1p8GeV/crmc_Sexaq_0.root)
(eval `scram unsetenv -sh`; gfal-copy /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_0.root davs://cmsxrootd.hep.wisc.edu:1094/store/user/wvetens/crmc_Sexaq/crmc/Sexaquark_13TeV_trial_test_1p8GeV/crmc_Sexaq_0.root)
rm /afs/cern.ch/work/w/wvetens/Sexaquarks/tmp/CMSSW_10_2_26/src/CustomGenerator/Custom/crmc_Sexaq_incl_installed/SexaquarkProduction/OutputRootFile/OutputRootFile_with_Vtx_smearing2/crmc_Sexaq_0.root 
