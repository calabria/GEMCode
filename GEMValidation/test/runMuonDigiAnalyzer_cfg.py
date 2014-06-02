import FWCore.ParameterSet.Config as cms

process = cms.Process("MUONDIGIANA")

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
process.MuonDigiAnalyzer = cms.EDAnalyzer("MuonDigiAnalyzer",
    simTrackMatching = SimTrackMatching
)
process.MuonDigiAnalyzer.simTrackMatching.cscStripDigi.input = ""
process.MuonDigiAnalyzer.simTrackMatching.cscWireDigi.input = ""
process.MuonDigiAnalyzer.simTrackMatching.cscCLCT.input = ""
process.MuonDigiAnalyzer.simTrackMatching.cscALCT.input = ""
process.MuonDigiAnalyzer.simTrackMatching.cscLCT.input = ""
process.MuonDigiAnalyzer.simTrackMatching.gemRecHit.input = ""
process.MuonDigiAnalyzer.simTrackMatching.tfTrack.input = ""
process.MuonDigiAnalyzer.simTrackMatching.tfCand.input = ""
process.MuonDigiAnalyzer.simTrackMatching.gmtCand.input = ""
process.MuonDigiAnalyzer.simTrackMatching.l1Extra.input = ""

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

	'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_100_1_v55.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_101_1_eMu.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_102_1_2qQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_103_1_zB1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_104_1_IuL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_106_1_xLQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_107_1_PRo.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_108_1_2TT.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_109_1_GsY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_10_1_Hej.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_110_1_rha.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_111_1_exy.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_112_1_nA3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_113_1_SKf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_114_1_e54.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_115_1_VkV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_116_1_osY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_117_1_qLp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_118_1_8uR.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_119_1_DwG.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_11_1_fj2.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_120_1_puE.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_121_1_q3D.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_122_1_kyR.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_123_1_A1U.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_124_1_eAh.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_126_1_pPP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_127_1_M77.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_128_1_Da9.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_129_1_Xkt.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_12_1_uMv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_130_1_Fvk.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_131_1_bRm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_132_1_x9S.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_133_1_w6r.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_134_1_1BN.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_135_1_vWv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_137_1_bjq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_138_1_lCd.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_139_1_noD.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_13_1_Vwr.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_140_1_r8u.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_141_1_qB4.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_143_1_3F5.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_144_1_XqZ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_146_1_49K.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_147_1_5Nd.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_149_1_GX1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_14_1_2iA.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_150_1_Bxc.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_153_1_qJf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_154_1_V52.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_156_1_hZE.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_157_1_sXX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_159_1_8sb.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_160_1_8aD.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_161_1_l9c.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_162_1_YcV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_163_1_23p.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_164_1_SB7.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_165_1_4fg.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_166_1_nh7.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_167_1_ZFw.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_168_1_QT3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_169_1_41j.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_16_1_Wjl.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_170_1_6E3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_171_1_U1j.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_172_1_XI0.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_173_1_yyd.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_174_1_YcW.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_175_1_SIE.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_176_1_7N9.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_177_1_XSi.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_178_1_Ujk.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_179_1_Lh4.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_17_1_Dti.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_180_1_Pwa.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_181_1_B6b.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_182_1_Hzh.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_183_1_A8g.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_184_1_V3H.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_185_1_3bq.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_186_1_Org.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_187_1_PEp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_188_1_UCY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_189_1_82Q.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_190_1_SG3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_191_1_w0y.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_192_1_hlL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_193_1_BDA.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_194_1_3gg.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_195_1_DLr.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_196_1_2ZL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_197_1_oIG.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_198_1_yoN.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_199_1_u2B.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_19_1_3Dx.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_1_1_iNL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_200_1_Ofb.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_20_1_E07.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_21_1_OWf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_22_1_fhf.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_23_1_QIK.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_24_1_qi2.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_25_1_mHT.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_26_1_B4y.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_27_1_fUb.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_28_1_c2k.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_29_1_H4B.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_2_1_exb.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_30_1_0Om.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_32_1_CHX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_33_1_UUY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_35_1_leU.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_36_1_oPp.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_37_1_fFL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_38_1_VHP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_39_1_oig.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_3_1_Hqm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_40_1_E8D.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_41_1_Ei6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_44_1_Qco.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_45_1_XXX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_46_1_f8i.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_47_1_PIj.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_48_1_BnD.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_49_1_LDL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_4_1_2o1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_50_1_UuP.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_51_1_Bgu.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_52_1_m7x.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_53_1_cdn.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_54_1_8kM.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_55_1_FO3.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_56_1_mbg.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_57_1_lUV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_58_1_wSL.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_59_1_QT5.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_5_1_0Ep.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_60_1_j14.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_61_1_0E5.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_62_1_vgv.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_63_1_hlu.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_64_1_DQG.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_65_1_TrV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_66_1_b5K.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_67_1_p57.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_68_1_hvX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_69_1_4hM.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_6_1_2MD.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_70_1_n17.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_71_1_gYU.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_72_1_zLy.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_73_1_elK.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_74_1_KCx.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_75_1_YWX.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_76_1_YIz.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_77_1_bPY.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_78_1_BnF.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_79_1_9GE.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_7_1_KnO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_80_1_3eV.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_81_1_Mas.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_82_1_u9H.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_83_1_YDQ.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_84_1_IYO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_85_1_ufM.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_86_1_ewk.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_87_1_IHm.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_88_1_yfE.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_89_1_sJT.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_8_1_Luo.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_90_1_yg6.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_91_1_QTI.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_92_1_Njz.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_93_1_RJl.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_94_1_bH1.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_95_1_3YU.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_96_1_kNO.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_97_1_fVW.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_98_1_8CW.root',
       'root://xrootd.unl.edu//store/user/calabria/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/calabria_SingleNu50_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC13_ME0/86b4a7c67886003e93ce5e672deee57a/out_reco_99_1_WuB.root'
  )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("gem_digi_ana.root")
)

process.p = cms.Path(process.MuonDigiAnalyzer)

