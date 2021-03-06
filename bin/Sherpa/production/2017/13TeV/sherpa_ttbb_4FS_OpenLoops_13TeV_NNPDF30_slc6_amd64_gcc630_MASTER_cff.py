import FWCore.ParameterSet.Config as cms
import os

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('ttbb_4FS_OpenLoops_13TeV_NNPDF30'),
  SherpackLocation = cms.string('[/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/sherpa/V2.2.4/sherpa_ttbb_4FS_OpenLoops_13TeV_NNPDF30_slc6_amd64_gcc630_MASTER/v1/]'),
  SherpackChecksum = cms.string('f17644b5524e0a051f5bbd986de102be'),
  FetchSherpack = cms.bool(True),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 1.87373e+06 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" ## ATLAS global parameters",
				" BEAM_1=2212; BEAM_2=2212;",
				" BEAM_ENERGY_1=6500; BEAM_ENERGY_2=6500;",
				" MAX_PROPER_LIFETIME=10.0",
				" HEPMC_TREE_LIKE=1",
				" MASS[6]=172.5",
				" MASS[24]=80.399",
				" OL_PARAMETERS=preset=2=write_parameters=1",
				" HDH_WIDTH[24,2,-1]=0.7041",
				" HDH_WIDTH[24,4,-3]=0.7041",
				" HDH_WIDTH[24,12,-11]=0.2256",
				" HDH_WIDTH[24,14,-13]=0.2256",
				" HDH_WIDTH[24,16,-15]=0.2256",
				" HDH_WIDTH[-24,-2,1]=0.7041",
				" HDH_WIDTH[-24,-4,3]=0.7041",
				" HDH_WIDTH[-24,-12,11]=0.2256",
				" HDH_WIDTH[-24,-14,13]=0.2256",
				" HDH_WIDTH[-24,-16,15]=0.2256",
				" ## + systematic variation settings (PDFs, scales)",
				" FSF:=1.; RSF:=1.; QSF:=1.;",
				" SCALES VAR{FSF*H_TM2/4}{RSF*sqrt(MPerp(p[2])*MPerp(p[3])*MPerp(p[4])*MPerp(p[5]))}{QSF*H_TM2/4}",
				" ME_SIGNAL_GENERATOR Comix Amegic LOOPGEN;",
				" OL_PREFIX=/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/openloops/1.3.1-mlhled2",
				" LOOPGEN:=OpenLoops;",
				" MASSIVE[5]=1",
				" MASS[5]=4.8",
				" PDF_LIBRARY LHAPDFSherpa",
				" #LHAPDF_GRID_PATH=./PDFsets",
				" PDF_SET NNPDF30_nnlo_as_0118_nf_4",
				" USE_PDF_ALPHAS=1",
				" CSS_ENHANCE S{G}{t}{tb} 0",
				" CSS_ENHANCE S{G}{tb}{t} 0",
				" MCATNLO_MASSIVE_SPLITTINGS=0     # deactivates g->bb first emission in MC@NLO",
				" EXCLUSIVE_CLUSTER_MODE=1",
				" CSS_KMODE=34",
				" HARD_DECAYS=1",
				" STABLE[6]=0",
				" WIDTH[6]=0",
				" STABLE[24]=0",
				"}(run)",
				" (processes){",
				" Process 93 93 -> 6 -6 5 -5",
				" Order (*,0)",
				" NLO_QCD_Mode MC@NLO",
				" Loop_Generator LOOPGEN",
				" ME_Generator Amegic",
				" RS_ME_Generator Comix",
				" End process",
				"}(processes)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

