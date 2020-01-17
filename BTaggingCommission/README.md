
## Recipe for CMS b-tagging commissioning study in ttbar di-lepton channel
### Pre-requirements
* Ask conveners to get access right of eos storage space at /eos/cms/store/group/phys_btag/Commissioning/TTbar/
* Obtain Grid User certificate at https://ca.cern.ch/ca/
* Checkout Gridding and Plotting macros from https://github.com/pmandrik/CMS_btagana/tree/master/BTaggingCommission

### Grid Step
* Checkout CMSSW and follow the recipe from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagAnalyzer
  corresponded to the CMSSW version of the Data/MC samples. Sometimes the is no any recipes for the newest CMSSW 
  version of the samples - in this case the CMSSW vesion of the samples should be used with available recipe for the most      similare version.
* Take all unprescaled MuonEG triggers from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopTrigger
  and change *trigNamesToSel* and *trigChannels* in TTbarSelectionProducer_cfi.py (https://github.com/cms-btv-pog/RecoBTag-PerformanceMeasurements/blob/9_4_X/python/TTbarSelectionProducer_cfi.py)
* Define Data/MC samples in JSON files (such as https://github.com/pmandrik/CMS_btagana/blob/master/BTaggingCommission/ntupler/data/samples_Run2018_20190101_miniAOD.json)
* Create Python cfg in https://github.com/cms-btv-pog/RecoBTag-PerformanceMeasurements/tree/10_6_X/python/defaults
  * take basic options from recommended defaults file from recipe (such as **PixelStudies** in https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagAnalyzer#Recipe_for_10_5_X_releases)
  * add ttbar specific options in common: 
    ```python
    common = {
        'miniAOD' : True,
        'produceAllTrackTree': False,
        'produceJetTrackTree': True,
        'useSelectedTracks': False,
        'useTrackHistory': False,
        'useTTbarFilter': True,

        'runPFMuonVariables': True,
        'runPFElectronVariables': True,
        'runDeepFlavourTagVariables' : True,
        'runCSVTagVariables': True,        
        'runCTagVariables': True,

        'groups':['Petr','TTbar','PFMuon'],
    }
    ```
* Check production locally:
   ```shell
   cmsRun ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py defaults=YOUR_DEFAULTS maxEvents=100 runOnData=False
   cmsRun ${CMSSW_BASE}/src/RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py defaults=YOUR_DEFAULTS maxEvents=100 runOnData=True
   ```
* Check the options in submitToGrid.py (https://github.com/cms-btv-pog/RecoBTag-PerformanceMeasurements/blob/9_4_X/test/ttbar/submitToGrid.py) - following options should be inserted/changed in the right place of the script following the expected call order:
   ```python
      config_file.write('config.JobType.allowUndistributedCMSSW = True\n')
      config_file.write('config.JobType.pyCfgParams = [\'defaults=YOUR_DEFAULTS\', \'maxEvents=-1\', \'runOnData=%s\']\n' % bool(isData))
      config_file.write('config.Data.allowNonValidInputDataset = True')
      config_file.write('config.Data.unitsPerJob = 10\n') # <- PUT HERE RIGHT VALUE BASED ON SIZE OF THE DATASETS
      config_file.write('config.JobType.allowUndistributedCMSSW = True\n')
      config_file.write('config.Site.storageSite = "T2_CH_CERN"\n')
   ```
* Submit with submitHelper.sh (https://github.com/pmandrik/CMS_btagana/blob/master/BTaggingCommission/ntupler/submitHelper.sh) - nothing as wrapper around submitToGrid.py script. Be sure to setup GRID enviroment first:
   ```shell
   source /cvmfs/cms.cern.ch/crab3/crab.sh
   grid-proxy-init
   voms-proxy-init -voms cms
   ```
   * take lumimask from https://twiki.cern.ch/twiki/bin/view/CMS/PdmV (such as Golden JSON from https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2018Analysis#DATA)
    
### Plotting Step
* Generate lumimask of processed lumisections (for Data if the xsection of the processed files is expected to be significantly smaller from the total year xsection):
  * for every crab outpu directory:
  ```shell
  crab report -d crabTaskDir
  ```
  * merge processedLumis.json files using CMSSW script:
  ```shell
  mergeJSON.py --output=merged.json processedLumis_1.json processedLumis_2.json ...
  ```
  * calculate processed luminosity using brilcalc (https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html)
  ```shell
  export PATH=$HOME/.local/bin:/cvmfs/cms-bril.cern.ch/brilconda/bin:$PATH
  brilcalc lumi -u /fb -i merged.json
  ```
* Generates pileup reweighting file:
  * find corresponded pileup_latest.txt file (such as /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PileUp/pileup_latest.txt)
  * update MixingModule in runPileupEstimation.py (git cms-addpkg SimGeneral/MixingModule)
  * run runPileupEstimations.py script (work at least in CMSSW_10_0_0)
  ```shell
  python runPileupEstimations.py --json=merged.json --puJson=pileup_latest.txt
  ```
  or
  ```
  python runCode4ttbar.py pu merged.json pileup_latest.txt
  ```
  
* Create batch HTCondor jobs (-c) and submit (-s) the jobs (modify data/dataToRun_Tag.py):
  ```shell
  python runCode4ttbar.py -c create data/dataToRun_Tag.py -s
  ```
  * some things are hardcoded :D, so change the trigger list in line in runCode4ttbar.py:
  ```            triggers = ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v',```
  and update paths in runCode4ttbar.sh
  * status of the task could be checked using *condor_q* command (https://batchdocs.web.cern.ch/local/quick.html)

* Merge all histogram:
  ```shell
  python runCode4ttbar.py merge data/dataToRun_Tag.py
  ```
  
* Draw plots (modify drawAll_cfi.py, drawAll.py - a lot of work here usually):
  ```shell
  python runCode4ttbar.py draw
  ```
### Put the pictures online and submit to the conviners!
Plots from previous studies: https://pmandrik.web.cern.ch/pmandrik/cgi-bin/dirloop.py?path=SWORK/BTAG/ttbar_commision
Previous version of the instruction: https://hackmd.io/Q0ecnGzqQvqOptvvfIgRJQ
