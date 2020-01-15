dataset = {}

# An example config
#dataset['name'] = {
#    'xsec'              : -1, # -1 for data, others for MC
#    'ipath'             : ['localpath','lfnpath1','lfnpath2'], # Will check ALL '*.root' under the dir, localpath and lfn are supported.
#}

defaultLumi=57716 # In /pb
defalutPUWgtUrl="/afs/cern.ch/work/p/pmandrik/swork/2_btag_ttbar/7_jan_2018_SF/CMSSW_10_0_0/src/pileupWgts.root"

MC_PATH="/eos/cms/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/22Jan2018_SF_Moriond19_MC_resubmit/4e8605c/"
DATA_PATH="/eos/cms/store/group/phys_btag/Commissioning/TTbar/Run2018/crab/22Jan2018_SF_Moriond19/4e8605c/MuonEG/"

dataset['runA'] = {
    'xsec'              : -1,
    'ipath'             : [DATA_PATH + 'crab_Data13TeV_MuonEG_2018A'],
    'puWgtUrl'          : defalutPUWgtUrl,
}
dataset['runB'] = {
    'xsec'              : -1,
    'ipath'             : [DATA_PATH + 'crab_Data13TeV_MuonEG_2018B'],
    'puWgtUrl'          : defalutPUWgtUrl,
}
dataset['runC'] = {
    'xsec'              : -1,
    'ipath'             : [DATA_PATH + 'crab_Data13TeV_MuonEG_2018C'],
    'puWgtUrl'          : defalutPUWgtUrl,
}
dataset['runD'] = {
    'xsec'              : -1,
    'ipath'             : [DATA_PATH + 'crab_Data13TeV_MuonEG_2018D'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['ttbar'] = {
    'xsec'              : 831.77 * pow(1. - 0.6741, 2),
    'ipath'             : [MC_PATH + 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['dy1'] = {
    'xsec'              : 18610,
    'ipath'             : [MC_PATH + 'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['dy2'] = {
    'xsec'              : 6025,
    'ipath'             : [MC_PATH + 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['st1'] = {
    'xsec'              : 35.85,
    'ipath'             : [MC_PATH + 'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['st2'] = {
    'xsec'              : 35.85,
    'ipath'             : [MC_PATH + 'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['ww'] = {
    'xsec'              : 118.7,
    'ipath'             : [MC_PATH + 'WW_TuneCP5_13TeV-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['wz'] = {
    'xsec'              : 47.13,
    'ipath'             : [MC_PATH + 'WZ_TuneCP5_13TeV-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

dataset['zz'] = {
    'xsec'              : 16.5,
    'ipath'             : [MC_PATH + 'ZZ_TuneCP5_13TeV-pythia8'],
    'puWgtUrl'          : defalutPUWgtUrl,
}

# If 'xsec' is -1, take the 'xsec' setting from datasets.
groupdata = {}
groupdata['mc'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['ttbar','st1','st2','dy1','dy2','ww','wz','zz'],
     'xsec'      : [-1,-1,-1,-1,-1,-1,-1,-1],
 }
groupdata['tt'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['ttbar'],
     'xsec'      : [-1],
}
groupdata['st'] = {
     'lumi'      : defaultLumi,
    'dataset'   : ['st1','st2'],
    'xsec'      : [-1, -1],
}
groupdata['dy'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['dy1','dy2'],
     'xsec'      : [-1, -1],
}
groupdata['ww'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['ww'],
     'xsec'      : [-1],
}
groupdata['wz'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['wz'],
     'xsec'      : [-1],
}
groupdata['zz'] = {
     'lumi'      : defaultLumi,
     'dataset'   : ['zz'],
     'xsec'      : [-1],
}
groupdata['data'] = {
    'lumi'      : -1,
    'dataset'   : ['runA', 'runB', 'runC', 'runD'],
    'xsec'      : [-1, -1, -1, -1],
}







