import sys

from ROOT import *

from cuts import *
from drawPlots import *

## run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT 
ROOT.gROOT.SetBatch(1)

#_______________________________________________________________________________
def me0SimHitOccupancyXY(plotter):
  draw_occ(plotter.targetDir, "sh_me0_xy_rm1_l1", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1, layer1;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rm1,l1), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rm1_l2", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1, layer2;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rm1,l2), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rm1_l3", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1, layer3;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rm1,l3), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rm1_l4", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1, layer4;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rm1,l4), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rm1_l5", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1, layer5;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rm1,l5), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rm1_l6", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1, layer6;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rm1,l6), "COLZ")
  
  draw_occ(plotter.targetDir, "sh_me0_xy_rp1_l1", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1, layer1;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rp1,l1), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rp1_l2", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1, layer2;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rp1,l2), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rp1_l3", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1, layer3;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rp1,l3), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rp1_l4", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1, layer4;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rp1,l4), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rp1_l5", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1, layer5;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rp1,l5), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_xy_rp1_l6", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1, layer6;globalX [cm];globalY [cm]", 
           "h_", "(120,-280,280,120,-280,280)", "globalX:globalY", AND(rp1,l6), "COLZ")

#_______________________________________________________________________________
def me0SimHitOccupancyRZ(plotter):
  draw_occ(plotter.targetDir, "sh_me0_zr_rm1", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region-1;globalZ [cm];globalR [cm]", 
           "h_", "(80,-555,-515,120,20,280)", "sqrt(globalX*globalX+globalY*globalY):globalZ", AND(rm1), "COLZ")
  draw_occ(plotter.targetDir, "sh_me0_zr_rp1", plotter.ext, plotter.treeME0SimHits," SimHit occupancy: region1;globalZ [cm];globalR [cm]", 
           "h_", "(80,515,555,120,20,280)", "sqrt(globalX*globalX+globalY*globalY):globalZ", AND(rp1), "COLZ")

#_______________________________________________________________________________
def me0SimHitTOF(plotter):
  draw_1D(plotter.targetDir, "sh_me0_tof_rm1_l1", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region-1, layer1;Time of flight [ns];entries", 
          "h_", "(40,15,19)", "timeOfFlight", AND(rm1,l1))
  draw_1D(plotter.targetDir, "sh_me0_tof_rm1_l2", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region-1, layer2;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rm1,l2))
  draw_1D(plotter.targetDir, "sh_me0_tof_rm1_l3", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region-1, layer3;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rm1,l3))
  draw_1D(plotter.targetDir, "sh_me0_tof_rm1_l4", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region-1, layer4;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rm1,l4))
  draw_1D(plotter.targetDir, "sh_me0_tof_rm1_l5", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region-1, layer5;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rm1,l5))
  draw_1D(plotter.targetDir, "sh_me0_tof_rm1_l6", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region-1, layer6;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rm1,l6))
  
  draw_1D(plotter.targetDir, "sh_me0_tof_rp1_l1", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region1, layer1;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rp1,l1))
  draw_1D(plotter.targetDir, "sh_me0_tof_rp1_l2", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region1, layer2;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rp1,l2))
  draw_1D(plotter.targetDir, "sh_me0_tof_rp1_l3", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region1, layer3;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rp1,l3))
  draw_1D(plotter.targetDir, "sh_me0_tof_rp1_l4", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region1, layer4;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rp1,l4))
  draw_1D(plotter.targetDir, "sh_me0_tof_rp1_l5", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region1, layer5;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rp1,l5))
  draw_1D(plotter.targetDir, "sh_me0_tof_rp1_l6", plotter.ext, plotter.treeME0SimHits," SimHit TOF: region1, layer6;Time of flight [ns];entries", 
          "h_", "(40,15,22)", "timeOfFlight", AND(rp1,l6))
  
#_______________________________________________________________________________
def me0SimTrackToSimHitMatchingLX(plotter):
  pass

#_______________________________________________________________________________
def me0SimTrackToSimHitMatchingLY(plotter):
  pass

#_______________________________________________________________________________
def me0SimTrackToSimHitMatchingEta(plotter): 
  pass

#_______________________________________________________________________________
def me0SimTrackToSimHitMatchingPhi(plotter):
  pass
