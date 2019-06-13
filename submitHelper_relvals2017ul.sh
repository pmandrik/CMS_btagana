#!/usr/bin/env bash

#lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
#lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
lumimask="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"

# Data
#workdir="06_05_19_trk_relval_data"
#psetname="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/9_impact_of_miss/BTaggingCommission/ntupler/data/samples_tracker_relvals_DATA.json"
#lfnpath="/store/group/phys_btag/Commissioning/TTbar/Run2017/crab/06_05_19_trk_relval_data"

# MC
workdir="06_05_19_trk_relval_mc"
psetname="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/10_tracker_relvals/BTaggingCommission/ntupler/data/samples_tracker_relvals.json"
lfnpath="/store/group/phys_btag/Commissioning/TTbar/Run2017/crab/06_05_19_trk_relval_mc"

cd ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/ttbar
python submitToGrid.py -j ${psetname} -c ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py --lfn ${lfnpath} -l ${lumimask} -w ${workdir} -s


