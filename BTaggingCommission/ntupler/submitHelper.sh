#!/usr/bin/env bash

#lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
#lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"

# Data
workdir="21Oct2019_UL_EGAMMA_DATA"
psetname="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/11_UL_2018/BTaggingCommission/ntupler/data/samples_Run2018_20190101_miniAOD_Data.json"
lfnpath="/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/21Oct2019_UL_EGAMMA_DATA"

# MC
workdir="21Oct2019_UL_EGAMMA_MC"
psetname="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/11_UL_2018/BTaggingCommission/ntupler/data/samples_Run2018_20190101_miniAOD.json"
lfnpath="/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/21Oct2019_UL_EGAMMA_MC"

cd ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/ttbar
python submitToGrid.py -j ${psetname} -c ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py --lfn ${lfnpath} -l ${lumimask} -w ${workdir} -s

