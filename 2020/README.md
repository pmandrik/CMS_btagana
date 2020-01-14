
## Recipe for CMS b-tagging commissioning study in ttbar di-lepton channel

### Grid Step
* Checkout CMSSW and follow the recipe from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagAnalyzer
  corresponded to the CMSSW version of the Data/MC samples. Sometimes the is no any recipes for the newest CMSSW 
  version of the samples - in this case the CMSSW vesion of the samples should be used with latest available recipe.
* Take all unprescaled MuonEG triggers from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopTrigger
  and change *trigNamesToSel* and *trigChannels* in TTbarSelectionProducer_cfi.py (https://github.com/cms-btv-pog/RecoBTag-PerformanceMeasurements/blob/9_4_X/python/TTbarSelectionProducer_cfi.py)
* Define Data/MC samples in JSON files (such as FIXME link to files)
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
* Check the options in submitToGrid.py (https://github.com/cms-btv-pog/RecoBTag-PerformanceMeasurements/blob/9_4_X/test/ttbar/submitToGrid.py):
   ```python
      config_file.write('config.JobType.allowUndistributedCMSSW = True\n')
      config_file.write('config.JobType.pyCfgParams = [\'defaults=YOUR_DEFAULTS\', \'maxEvents=-1\', \'runOnData=%s\']\n' % bool(isData))
      config_file.write('config.Data.allowNonValidInputDataset = True')
      config_file.write('config.Data.unitsPerJob = 10\n') # <- PUT HERE RIGHT VALUE BASED ON SIZE OF THE DATASETS
      config_file.write('config.JobType.allowUndistributedCMSSW = True\n')
      config_file.write('config.Site.storageSite = "T2_CH_CERN"\n')
   ```
* TODO
    
### Plotting Step
