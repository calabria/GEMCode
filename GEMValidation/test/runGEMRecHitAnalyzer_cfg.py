import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMRECOANA")

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2023MuonReco_cff')
process.load('Configuration.Geometry.GeometryExtended2023Muon_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

## TrackingComponentsRecord required for matchers
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')

## global tag for 2019 upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')

# the analyzer configuration
from GEMCode.GEMValidation.simTrackMatching_cfi import SimTrackMatching
process.GEMRecHitAnalyzer = cms.EDAnalyzer("GEMRecHitAnalyzer",
    simTrackMatching = SimTrackMatching
)
process.GEMRecHitAnalyzer.simTrackMatching.gemStripDigi.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.gemPadDigi.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.gemCoPadDigi.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.cscStripDigi.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.cscWireDigi.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.cscCLCT.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.cscALCT.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.cscLCT.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.cscMPLCT.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.tfTrack.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.tfCand.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.gmtCand.input = ""
process.GEMRecHitAnalyzer.simTrackMatching.l1Extra.input = ""

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_101_1_F74.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_102_1_DVN.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_103_1_2ld.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_104_1_AtV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_105_1_gN5.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_106_1_kV6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_107_1_Uy8.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_109_1_UUo.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_10_1_WPf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_110_1_urI.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_111_1_pYj.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_112_1_0nY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_113_1_7Ut.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_114_1_HCY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_115_1_eNZ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_116_1_Ec0.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_117_1_qvN.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_11_1_7xY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_120_1_50P.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_121_1_VF4.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_122_1_Grv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_123_1_IBz.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_124_1_kRh.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_125_1_oJ0.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_126_1_Wf0.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_128_1_zGp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_129_1_7xQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_130_1_QSi.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_131_1_4FV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_132_1_Y5i.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_133_1_nsi.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_134_1_UsP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_135_1_2Mq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_136_1_8jb.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_137_1_Yla.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_138_1_9VO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_139_1_F6f.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_13_1_ve5.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_140_1_0Ms.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_141_1_NbC.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_142_1_Wre.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_143_1_QeU.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_144_1_JqB.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_145_1_Zx3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_146_1_Xjc.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_147_1_9Tr.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_148_1_n0S.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_149_1_8Ad.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_14_1_uXf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_150_1_Kul.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_151_1_CbC.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_152_1_cXi.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_153_1_luQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_154_1_VR3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_155_1_Cd9.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_156_1_9nL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_157_1_Y7w.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_158_1_wYM.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_159_1_ijF.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_15_1_gHk.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_160_1_4Xf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_161_1_U80.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_162_1_UtP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_163_1_7VB.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_164_1_SEv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_165_1_jlq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_166_1_Ggx.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_167_1_gi7.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_169_1_qxV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_16_1_pf6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_170_1_Q26.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_172_1_rxO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_173_1_D1v.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_174_1_ulP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_175_1_X1K.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_176_1_Yfo.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_177_1_3yR.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_178_1_56R.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_179_1_y2y.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_17_1_6Wu.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_180_1_Niz.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_181_1_uDO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_182_1_0bk.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_183_1_l87.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_184_1_ogm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_185_1_4zF.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_187_1_6HA.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_188_1_pdj.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_189_1_ANb.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_18_1_9AO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_190_1_erN.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_191_1_wBI.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_192_1_sDy.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_193_1_H3B.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_194_1_0uH.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_195_1_Q3U.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_196_1_iL1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_197_1_9UP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_198_1_axC.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_199_1_J3W.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_19_1_XXd.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_200_1_J5R.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_20_1_NLu.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_21_1_zS7.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_22_1_vQq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_23_1_qT9.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_24_1_oW9.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_27_1_SlO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_28_1_Mpm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_29_1_XVZ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_2_1_5IR.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_30_1_6AR.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_31_1_ICX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_32_1_1BO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_33_1_0E3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_34_1_Ygm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_35_1_6Kd.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_36_1_MY1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_37_1_UkQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_38_1_KPF.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_39_1_Djn.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_3_1_POQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_40_1_gU9.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_42_1_vOV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_43_1_yGp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_44_1_3vQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_45_1_a5E.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_46_1_VEn.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_47_1_5H8.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_48_1_1cQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_49_1_vJp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_4_1_GwS.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_50_1_8lL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_52_1_6l4.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_53_1_geq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_54_1_it6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_55_1_yNX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_56_1_NVp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_57_1_wtv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_59_1_fIv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_5_1_IXF.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_60_1_Q7o.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_61_1_xeN.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_62_1_rLx.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_63_1_EYs.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_64_1_wtC.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_65_1_YJG.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_68_1_0gc.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_69_1_2Hy.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_6_1_js6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_71_1_vKm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_72_1_lsA.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_73_1_Mdq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_74_1_MoJ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_76_1_YAw.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_77_1_Nxk.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_78_1_9Iw.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_79_1_vkH.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_7_1_E3G.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_80_1_00y.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_81_1_obd.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_82_1_2dv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_83_1_ouc.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_84_1_tPl.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_85_1_8jV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_86_1_2ha.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_87_1_1qr.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_89_1_C13.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_8_1_phQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_90_1_pl4.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_91_1_ayM.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_92_1_Fl1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_93_1_zut.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_94_1_prI.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_95_1_ImG.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_96_1_eVj.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_97_1_ye6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_98_1_c0P.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleMuPt50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/aaa4eafee0733be350faad1cbaa40e4d/out_reco_99_1_357.root'

  )
)

process.TFileService = cms.Service("TFileService",
  fileName = cms.string("gem_localrec_ana.root")
)

process.p = cms.Path(process.GEMRecHitAnalyzer)
