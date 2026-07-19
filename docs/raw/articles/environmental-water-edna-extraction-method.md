---
source_url: 
source_type: article
ingested: 2026-07-19
sha256: c6570ae60b8776fce9626eed764d632ef749f5d487a2fc19607e09d0f82efd63
---

OXFORD NANOPORE
Environmental water (eDNA)
FOR RESEARCH USE ONLY
OXFORD NANOPORE TECHNOLOGIES | Environmental water (eDNA)
PAGE 1
Contents
Introduction
Materials
Method
Results
Sequencing performance
Species identification
OXFORD NANOPORE TECHNOLOGIES | Environmental water (eDNA)
PAGE 2
Introduction
This protocol describes a method to extract genomic DNA (gDNA) from pond water as an example of
an environmental water sample. We tested multiple extraction kits and compared performance using
ZymoBIOMICS Microbial Community Standard, a commercial sample of known composition.
Our initial experiments were carried out using ZymoBIOMICS Microbial Community Standard diluted in
sterile water and filtered through a vacuum before the gDNA was extracted directly from the filter. We
tested the extraction kits:
ZymoBIOMICS DNA Miniprep Kit
Zymo Quick-DNA HMW MagBead Kit
QIAGEN MagAttract
QIAGEN Puregene
QIAGEN PowerWater
The extraction kit that yielded the community representation closest to the expected control was
ZymoBIOMICS DNA Miniprep Kit. All the other methods showed a deviation from the expected species
distribution.
To validate the method further, we used a sample of water from a residential garden pond (containing
a known fish species). The sample was extracted and prepared for sequencing with and without PCR
amplification using the Rapid PCR Barcoding Kit and the Ligation Sequencing Kit, respectively. DNA
was also amplified using QIAGEN REPLI-G Midi kit for whole genome amplification following our
recommended protocol; Ligation sequencing gDNA - whole genome amplification. All samples were
sequenced on MinION and the reads generated were analysed using Centrifuge run on raw reads.
Results showed that the expected fish species were detected in all samples. In addition, it was also
possible to detect other eukaryotic species that are present in the garden such as rodents, birds, and
plants, alongside diverse species belonging to the rich microbial community that can be found in an
environmental sample.
Materials
ZymoBIOMICS Microbial Community Standard
ZymoBIOMICS DNA Miniprep Kit
Vacuum filter unit (e.g. Thermo Scientific™ Nalgene™ Reusable Filter Units)
Vacuum pump
0.2 µm cellulose nitrate filter (e.g. Cytiva Whatman™ Cellulose Nitrate Membrane Filters)
ZR BashingBead Lysis Tubes
Tweezers
1.5 ml Eppendorf tubes
Vortex mixer
Microcentrifuge
Method
1. Prepare the vacuum filter unit with a 0.2 µm cellulose nitrate filter.
2. Pour 500 ml of pond water through a vacuum filter unit.
OXFORD NANOPORE TECHNOLOGIES | Environmental water (eDNA)
PAGE 3
3. Once all the solution has passed through vacuum, disassemble the vacuum filter unit, and use
tweezers to remove the filter.
4. Carefully roll the filter with tweezers and transfer it directly to a ZR BashingBead™ Lysis Tube.
5. Add 750 µl of ZymoBIOMICS™ Lysis solution, and ensure the tube is properly closed.
6. Place the tube in a tube holder, vortex adapter or simply tape the tubes to the vortex. Agitate at
maximum speed for 40 minutes.
7. Follow the recommended protocol from steps 4-13 (pages 6-7 from the ZymoBIOMICS DNA
Miniprep kit handbook.
Results
DNA yield: 1.5 - 2 µg OD A260/280: 2.73 OD A260/230: 0.49
Wavelength ( nm)
220
240
260
280
300
320
340
10 mm Absorbance
0
0.2
0.4
0.6
1.0
0.8
Sequencing performance
Read length profile:
Bases sequenced
Read length ( kb)
0
10
15
20
30
Output (Gb )
Run time (h)
0
15 20
5
30
25
10
0
12
16
8
4
5
25
Ligation Seq Kit
Rapid PCR
WGA
Ligation Seq Kit
Rapid PCR
WGA
Species identification
OXFORD NANOPORE TECHNOLOGIES | Environmental water (eDNA)
PAGE 4
Pseudomonas aeruginosa
Escherichia coli
Salmonella enterica
Lactobacillus fermentum
Enterococcus faecalis
Staphylococcus aureus
Listeria monocytogenes
Bacillus subtilis
Saccharomyces cerevisiae
Cryptococcus neoformans
Zymo Quick -DNA
MagBead Kit
expected
ZymoBIOMICS
Miniprep Kit
Species representation (%)
Extraction
0
75
50
25
100
QIAGEN
Puregene
QIAGEN
PowerWater
Figure 1. ZymoBIOMICS Microbial Community Standard species abundance (percentage of base pairs)
according to the theoretical composition and the different kits that were tested.
%
3
.
0
   
Archaea
__
k
%
1
.
0
   
Viruses
__
k
%
04
.
0
   
organism
_
uncultured
__
s
%
02
.
0
   
microorganism
_
uncultured
__
s
%
01
.
0
   
prokaryote
_
uncultured
__
s
%
004
.
0
   
construct
_
synthetic
__
s
%
004
.
0
   
organism
_
marine
_
uncultured
__
s
%
0008
.
0
   
microorganism
_
marine
_
uncultured
__
s
%
0006
.
0
   
unidentified
__
s
%
0004
.
0
   
3
AT
_
prokaryote
_
uncultured
__
s
%
0003
.
0
   
11
J
137
ANIW
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0003
.
0
   
37
CA
_
organism
_
uncultured
__
s
%
0002
.
0
   
microorganism
_
unidentified
__
s
%
0002
.
0
   
878
CA
_
organism
_
uncultured
__
s
%
0002
.
0
   
23
H
7
APKG
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0002
.
0
   
6
EC
_
prokaryote
_
uncultured
__
s
%
0001
.
0
   
AIresMuro
2
GAPTrapT
_
vector
_
Cloning
__
s
%
0001
.
0
   
pCelD
_
organism
_
uncultured
__
s
%
0001
.
0
   
98
pMOL
_
plasmid
_
Synthetic
__
s
%
0001
.
0
   
185
C
-
05
S
-
OCT
-
MedDCM
_
organism
_
uncultured
__
s
%
0001
.
0
   
7
L
8
APKG
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0001
.
0
   
organism
_
soil
_
unidentified
__
s
%
0001
.
0
   
426
C
-
09
S
-
OCT
-
MedDCM
_
organism
_
uncultured
__
s
%
0001
.
0
   
478
C
-
04
S
-
OCT
-
MedDCM
_
organism
_
uncultured
__
s
%
0001
.
0
   
11
H
5
APKG
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0001
.
0
   
288
C
-
08
S
-
OCT
-
MedDCM
_
organism
_
uncultured
__
s
%
0001
.
0
   
1
C
-
04
S
-
OCT
-
MedDCM
_
organism
_
uncultured
__
s
%
0001
.
0
   
pTSL
_
vector
_
Cloning
__
s
%
0001
.
0
   
5
AT
_
prokaryote
_
uncultured
__
s
%
0001
.
0
   
12
H
10
APKG
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0001
.
0
   
1
P
_
Plasmid
__
s
%
0001
.
0
   
HTsLsM
2
pBBRKW
_
vector
_
Expression
__
s
%
0001
.
0
   
microorganism
_
soil
_
uncultured
__
s
%
0001
.
0
   
20
B
133
ANIW
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0001
.
0
   
5
K
8
APKG
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
%
0001
.
0
   
7
C
141
ANIW
_
4000
HF
_
microorganism
_
marine
_
uncultured
__
s
all
k__Bacteria
p__Proteobacteria
c__Betaproteobacteria
o__Burkholderiales
f__...eae
%
9
.
0
   
Rhodoferax
__
g
%
9
.0
   
Acidovorax
__
g
%
7
.0
   
Hydrogenophaga
__
g
more
19
f__...eae
%
8
.0
   
Burkholderia
__
g
more
5
%
1
   
Oxalobacteraceae
__
f
more
17
%
7
.0
   
Rhodocyclales
__
o
more
14
c__Gammap...obacteria
o__Pseudomonadales
f__Pseudomonadaceae
g__Pse...omonas
more
116
%
9
.0
   
Enterobacterales
__
o
%
7.
0
   
Xanthomonadales
__
o
more
50
c __Alpha...bacteria
%
2
   
Rhizobiales
__
o
o__...les
%
1
   
Sphingomonadaceae
__
f
o__Rh ...rales
%
9
.
0
   
Rhodobacteraceae
__
f
more
20
c__Epsilonp...teobacteria
o__...les
f_...ae
%
7
.
0
   
Arcobacter
__
g
%
8
.
0
   
Deltaproteobacteria
__
c
p__Ac ...teria
c__ Actinobacteria
o__Cor...riales
...
%
8
.
0
   
Mycobacterium
__
g
f__St...aceae
...
more
241
%
9
.0
   
Micrococcales
__
o
more
23
p__Bacteroidetes
c __Flavobacteriia
o__Flavo...teriales
f__Flavobacteriaceae
%
1
   
Flavobacterium
__
g
more
43
more
11
p__Fi...cutes
%
9
.0
   
Bacilli
__
c
more
673
41%   Unclassified
k__Eukaryota
p__Chordata
c__Actinopteri
o__ Cypr...iformes
f__ Cyprinidae
0.9%   s__Cyprinus _carpio
39 more
c__Mammalia
o__Primates
0.6%   f__Hominidae
27 more
14 more
3%   p__Streptophyta
p__ Arthropoda
1%   c__Insecta
p__Nematoda
1%   c __Chromadorea
1%   p __Platyhelminthes
1%   p__ Ascomycota
130 more
Figure 2. A Krona graphical representation of the species detected with Centrifuge on the pond
sample. The number of unclassified reads is within expectation for a real sample as there will be
species present for which a reference genome does not yet exist. Sequencing the native DNA shows
the microbial and eukaryotic species diversity present in this pond.
OXFORD NANOPORE TECHNOLOGIES | Environmental water (eDNA)
PAGE 5
Figure 3. A representation of the species (minimum abundance cut-off of 0.1%) detected with EPI2ME
FASTQ WIMP (What’s In My Pot) workflow. WIMP provides the identification of bacteria, fungi, viruses,
and archaea, being ideal for users focused on microorganisms.
OXFORD NANOPORE TECHNOLOGIES | Environmental water (eDNA)
PAGE 6

