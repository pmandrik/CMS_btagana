dataset = {}

# An example config
#dataset['name'] = {
#    'xsec'              : -1, # -1 for data, others for MC
#    'ipath'             : ['localpath','lfnpath1','lfnpath2'], # Will check ALL '*.root' under the dir, localpath and lfn are supported.
#}

defaultLumi=44.98 # In /pb
defalutPUWgtUrl="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/12_UL_2017/BTaggingCommission/puw_2017.root"

MC_PATH="/eos/cms/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/21Oct2019_UL2017_MC_v2/bef9eef/"
DATA_PATH="/eos/cms/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/21Oct2019_UL2017_DATA_v2/bef9eef/MuonEG/"

for era in ["B", "C", "D", "E", "F"] :
  dataset[ 'run' + era ] = {
      'xsec'              : -1,
      'ipath'             : [DATA_PATH + 'crab_Data13TeV_MuonEG_2017' + era],
      'puWgtUrl'          : defalutPUWgtUrl,
  }

dataset['ttbar'] = {
    'xsec'              : 831.77 * pow(1. - 0.6741, 2),
    'ipath'             : [MC_PATH + 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['dy'] = {
    'xsec'              : 6025, # * pow(1. - 0.6741, 2),
    'ipath'             : [MC_PATH + 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

# If 'xsec' is -1, take the 'xsec' setting from datasets.
groupdata = {}
groupdata['mc'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['ttbar'],
     'xsec'      : [-1],
 }
groupdata['dy'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['dy'],
     'xsec'      : [-1],
}
groupdata['ttbar'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['ttbar'],
     'xsec'      : [-1],
}

groupdata['data'] = {
    'lumi'      : -1,
    'dataset'   : [ 'runB', 'runC', 'runD', 'runE', 'runF' ],
    'xsec'      : [-1, -1, -1, -1, -1],
}







