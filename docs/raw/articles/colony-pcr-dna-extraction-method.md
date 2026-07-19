---
source_url: 
source_type: article
ingested: 2026-07-19
sha256: 66f9e5d4129339951a62e4a1b8043bd7c0da04c2fe05e675e1ecf493724cf0c4
---

OXFORD NANOPORE
Whole genome colony PCR
FOR RESEARCH USE ONLY
OXFORD NANOPORE TECHNOLOGIES | Whole genome colony PCR
PAGE 1
Contents
Introduction
Materials
Methods
Sequencing performance
Change log
OXFORD NANOPORE TECHNOLOGIES | Whole genome colony PCR
PAGE 2
Introduction
This protocol describes a method to extract and prepare genomic and plasmid DNA from a bacterial
colony. This has been verified using gram-negative E. coli. A colony was picked from a plate of
cultured bacteria and then treated with Proteinase K before preparing libraries for sequencing using
the Rapid PCR Barcoding Kit. The sequencing performance of the prepared libraries was assessed
using GridION.
Materials
Plated bacterial colonies
Rapid PCR Barcoding Kit
SFB Expansion (EXP-SFB001)
Flow Cell Priming Kit
1.5 ml Eppendorf DNA LoBind tubes
0.2 ml thin-walled PCR tubes
Nuclease-free water (e.g. ThermoFisher, cat # AM9937)
Agencourt AMPure XP beads
LongAmp Taq 2X Master Mix (e.g. NEB M0287)
10 mM Tris-HCl pH 8.0
10 mM Tris-HCl pH 8.0, 50mM NaCl (or EB from Sequencing Auxillary Vials (EXP-AUX001 or
equivalent)
(Optional) Thermolabile Proteinase K (e.g. NEB P8111S)
Microfuge
Thermal cycler
Pipettes and tips for P1000, P200, P100, P20, P10, and P2
Timer
Ice bucket with ice
Magnetic separator, suitable for either 1.5 ml Eppendorf tubes or 0.2 ml PCR tubes
Hula mixer (or similar gentle rotator mixer)
DNA QC equipment, e.g. Agilent Bioanalyzer, Qubit fluorometer
Inoculating loop/needle or sterile toothpick
Methods
1. Using either a pipette tip, sterile toothpick, inoculating loop or needle, pick one colony and dip
into 50 μl of 10 mM Tris-HCl pH 8.0. Swirl for 10 seconds until the solution becomes turbid.
2. Enriching for plasmid DNA only: If you are interested in the genomic DNA, proceed straight to
step 4. If you are interested in the plasmid DNA, transfer the 50 μl cell suspension to a 0.2 ml
thin-walled PCR tube and incubate at 95°C for 5 minutes. Note: It is observed that pre-treating
the colony by heating leads to an enrichment in the observation of plasmid reads in the
downstream sequencing, compared with non-heat treated libraries.
3. Enriching for plasmid DNA only: Add 1 μl of Thermolabile Proteinase K and incubate at 37°C for 15
minutes, then 55°C for 10 minutes.
4. Libraries can be prepared for sequencing using the Rapid PCR Barcoding Kit, using 3 μl of the
treated cell suspension as the template. If using cells without the heat treatment in step two, it
OXFORD NANOPORE TECHNOLOGIES | Whole genome colony PCR
PAGE 3
is recommended to PCR for 25 cycles, and if using heat-treated cells, it is recommended to PCR
for 30 cycles.
Sequencing performance
Libraries were prepared using the Rapid PCR Barcoding Kit:
Post PCR yield: 30-60 ng/μl
Output from the flow cell may be increased by performing a flow cell wash step at the point
where the rate of data acquisition begins to deteriorate due to the accumulation of pores in the
“unavailable” or “recovering” state, and then adding a new library.
Read length profile:
Change log
Version
Change
v3, 02nd
April 2024
Removed reference to Exonuclease I in Equipment and consumables as no longer
needed with the V14 Rapid PCR Barcoding Kit
v2, 21st
April 2021
Title changed from ‘PCR amplification of gram-negative bacterial DNA direct from a
colony’ to ‘Whole genome colony PCR’. Updated step 3 sub-title from ‘(plasmid DNA
only)’ to ‘(enriching for plasmid DNA only)’.
OXFORD NANOPORE TECHNOLOGIES | Whole genome colony PCR
PAGE 4
OXFORD NANOPORE TECHNOLOGIES | Whole genome colony PCR
PAGE 5

