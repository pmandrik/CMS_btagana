#!/usr/bin/env bash

#lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
#lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"

# Data
workdir="12_04_19_Ultimate_DATA"
psetname="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/8_april_ultimate_SF/BTaggingCommission/ntupler/data/samples_Ultimate_DATA.json"
lfnpath="/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/12_04_19_Ultimate_DATA"
globalTag="102X_dataRun2_Prompt_v11"

# MC
#workdir="12_04_19_Ultimate_MC"
#psetname="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/8_april_ultimate_SF/BTaggingCommission/ntupler/data/samples_Ultimate_MC.json"
#lfnpath="/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/12_04_19_Ultimate_MC"
#globalTag="102X_upgrade2018_realistic_v12"

cd ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/ttbar
python submitToGrid.py -j ${psetname} -c ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py --lfn ${lfnpath} -l ${lumimask} -w ${workdir} -s

