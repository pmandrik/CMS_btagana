#!/bin/bash

set -x

echo $1
echo $2

# /afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/12_UL_2017/BTaggingCommission/plotter

cd /afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/12_UL_2017/CMSSW_10_6_4_patch2/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros;
eval `scram runtime -sh`

cd ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/batch
/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/12_UL_2017/BTaggingCommission/plotter/runCode4ttbar.py run $1 --pu $2
