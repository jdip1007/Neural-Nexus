---
source_url: https://doi.org/10.1101/pdb.prot095141
source_type: article
ingested: 2026-07-26
sha256: 421d70449948587aceda293aa6193b4288e95b84f274ec32926e82710c9f07b3
---

# PCR Amplification of GC-Rich Templates

Michael R. Green and Joseph Sambrook
Cold Spring Harbor Protocols, 2019

Protocol
Polymerase Chain Reaction (PCR) Amplification
of GC-Rich Templates
Michael R. Green and Joseph Sambrook
The efﬁciency of polymerase chain reaction (PCR) ampliﬁcation is inﬂuenced by the nucleotide
composition and sequence of the template DNA. Problematic templates include those with long
homopolymeric runs, inverted repeats, or GC-rich tracts—such as those containing >60% G + C
residues—that are found in the regulatory regions of many mammalian genes. Localized regions of
templates rich in GC residues tend to fold into complex secondary structures that might not melt
during the annealing phase of the PCR cycle. Also, the primers used to amplify GC-rich regions often
have a high capacity to form self- and cross-dimers and a strong tendency to fold into stem–loop
structures that can impede the progress of the DNA polymerase along the template molecule. Pre-
dictably, ampliﬁcation of full-length template DNA is inefﬁcient, and the products of the reaction
contain a high proportion of shorter molecules that result from blockage of the DNA polymerase.
Altering the design of the primers and using a combination of hot start and touchdown PCR can
sometimes improve the efﬁciency of ampliﬁcation. More often, a multipronged approach is required,
such as the use of enhancers in the ampliﬁcation reaction, adjustment of the cycling protocol, and, if
necessary, designing new sets of primers. This protocol uses a mixture of four additives—betaine,
dithiothreitol (DTT), dimethyl sulfoxide (DMSO), and bovine serum albumin (BSA)—for use with
Taq DNA polymerase.
MATERIALS
It is essential that you consult the appropriate Material Safety Data Sheets and your institution’s Environmental
Health and Safety Ofﬁce for proper handling of equipment and hazardous material used in this protocol.
RECIPES: Please see the end of this protocol for recipes indicated by <R>. Additional recipes can be found online at
http://cshprotocols.cshlp.org/site/recipes.
Reagents
Additive solution (5×) <R>
Bystander DNA
Bystander DNA does not contain target sequences. It should resemble the template DNA in all other respects:
complexity, size, and concentration.
Chloroform (optional; see Step 6)
dNTP mix (all four dNTPs, 20 mM each; pH 8.0)
Ethidium bromide (optional; see Step 5)
GC-rich ampliﬁcation buffer (10×) <R>
From the Molecular Cloning collection, edited by Michael R. Green and Joseph Sambrook.
© 2019 Cold Spring Harbor Laboratory Press
Cite this protocol as Cold Spring Harb Protoc; doi:10.1101/pdb.prot095141
165
 
Cold Spring Harbor Laboratory Press
 at University of Hong Kong Libraries on July 26, 2026 - Published by 
http://cshprotocols.cshlp.org/
Downloaded from 
The concentration of MgCl2 in this buffer is 30 mM; however, the concentration of Mg2+ should be optimized in a
series of pilot reactions containing different concentrations of Mg2+ (0.5–5.0 mM).
Gel, polyacrylamide or agarose (see Step 5)
Mineral oil (optional; see Step 3)
Parafﬁn wax (optional; see Step 3)
Primers:
Forward primer (20 µM, in H2O)
Reverse primer (20 µM, in H2O)
Use the following formula to calculate the molecular mass of the oligonucleotides:
Mr = (C × 289) + (A × 313) + (T × 304) + (G × 329),
where C is the number of C residues in the oligonucleotide, A is the number of A residues, T is the number
of T residues, and G is the number of G residues. The molecular mass of a 20-mer will be ≏6000 Da; 100
pmol of the oligonucleotide will be equivalent to ≏0.6 µg.
SYBR Gold (optional; see Step 5)
Taq DNA polymerase (e.g., Agilent, Thermo Fisher, etc.)
Template DNA (100–500 ng/mL in 10 mM Tris-Cl at pH 7.6)
High concentrations of template DNA are reported to inhibit amplification of GC-rich sequences.
To reduce the chance of contamination with exogenous DNAs, prepare and use a special set of reagents and
solutions for PCR only.
Equipment
Barrier tips (for automatic micropipetting device)
Gel electrophoresis equipment (for polyacrylamide or agarose gels)
Microcentrifuge tubes, 0.5 mL, thin-walled (optional; see Step 1)
Microtiter plates (optional; see Step 1)
Positive-displacement pipette
Thermal cycler
A number of programmable thermal cyclers marketed by different commercial companies (e.g., Mastercycler
[Eppendorf], PTC-100 [MJ Research]) are licensed by PerkinElmer for use in PCR. The choice among these
instruments depends on the investigator’s inclination, the available budget, and the range of uses to which the
machine will be put. Before purchasing a thermal cycler, we recommend soliciting as many opinions as possible
to discover the advantages and disadvantages of different machines.
Bake all glassware for 6 h at 150˚C, and autoclave all plasticware.
METHOD
1. In a sterile 0.5-mL microcentrifuge tube, ampliﬁcation tube, or the well of a sterile microtiter plate,
mix in the following order:
GC-rich ampliﬁcation buffer (10×)
5 µL
dNTP mix (20 mM each, pH 8.0)
1 µL
Forward primer (20 µM)
2.5 µL
Reverse primer (20 µM)
2.5 µL
Thermostable DNA polymerase (1–5 units/µL)
1–2 units
Template DNA
5–10 µL
Additive solution (5×)
5 µL
H2O
to a ﬁnal volume of 50 µL
166
Cite this protocol as Cold Spring Harb Protoc; doi:10.1101/pdb.prot095141
M.R. Green and J. Sambrook
 
Cold Spring Harbor Laboratory Press
 at University of Hong Kong Libraries on July 26, 2026 - Published by 
http://cshprotocols.cshlp.org/
Downloaded from 
2. Prepare positive and negative controls, as detailed below:
Positive controls are required to monitor the efficiency of the PCR, whereas negative controls are required to
detect contamination with DNAs that contain the target sequence.
Bystander DNA
Template DNAa
Target DNAb
Speciﬁc primersc
Positive controls
1
+
−
+
+
2
−
−
+
+
Negative controls
3
−
−
−
+
4
+
−
−
+
aTemplate DNA is the DNA under test.
bTarget DNA contains the target sequence. It can be a recombinant DNA clone, a puriﬁed DNA
fragment, or a sample of genomic DNA. It should be added to the positive control at concentrations
equivalent to those expected in the template DNA. It is often necessary to set up a series of positive
controls containing different amounts of target DNA spanning the amount predicted in the template
DNA. An appropriate dilution of the target sequence should be prepared ahead of time in an area of
the laboratory different from that used for the preparation of other PCR reagents. This precaution
reduces the risk of contaminating equipment and plasticware in the area of the laboratory set aside for
PCRs.
cSpeciﬁc primers are oligonucleotide primers speciﬁc for the segment of target DNA.
3. If the thermal cycler is not ﬁtted with a heated lid, overlay the reaction mixtures with 1 drop (≏50
µL) of light mineral oil. Alternatively, if using a hot start protocol (see Protocol: Hot Start
Polymerase Chain Reaction (PCR) [Green and Sambrook 2018]), place a bead of wax into the
tube. Place the tubes or the microtiter plate in the thermal cycler.
4. Amplify the nucleic acids using the denaturation, annealing, and polymerization times and tem-
peratures listed below:
Cycle number
Denaturation
Annealing
Polymerization
1–30
30 sec at 94˚C
30 sec at 55˚C
1 min at 72˚C
Last cycle
1 min at 94˚C
30 sec at 55˚C
1 min at 72˚C
Normally, polymerization is performed for 1 min for every 1000 bp of length of the target DNA. Times
and temperatures might need to be adapted to suit the specific thermal cycler used and/or reaction
volumes.
Most thermal cyclers have an end routine in which the amplified samples are incubated at 4˚C until they are
removed from the machine. Samples can be left overnight at this temperature but should be stored thereafter
at −20˚C.
5. Analyze a sample (5–10 µL) from the reaction mixtures and each of the control reactions by
electrophoresis through an agarose or polyacrylamide gel. Be sure to include DNA markers
of an appropriate size. Stain the gel with ethidium bromide or SYBR Gold to visualize the
DNA.
6. If mineral oil was used to overlay the reaction (Step 3), remove the oil from the sample by
extraction with 150 µL of chloroform.
The aqueous phase, which contains the amplified DNA, will form a micelle near the meniscus. The micelle
can be transferred to a fresh tube with an automatic micropipette.
For many purposes, for example, purification of the amplified DNA using a Centricon microconcentrator or
cloning amplification products, it is desirable to remove the oil from the sample before proceeding.
Do not attempt chloroform extractions in microtiter plates. The plastic used in these plates is not resistant to
organic solvents.
Cite this protocol as Cold Spring Harb Protoc; doi:10.1101/pdb.prot095141
167
PCR Amplification of GC-Rich Templates
 
Cold Spring Harbor Laboratory Press
 at University of Hong Kong Libraries on July 26, 2026 - Published by 
http://cshprotocols.cshlp.org/
Downloaded from 
DISCUSSION
When designing primers for ampliﬁcation of GC-rich sequences, use an oligonucleotide design
program to check the Gibbs free-energy values (ΔG) for (1) the duplexes between the primers and
their binding sites on the targets and (2) the secondary structures predicted for each oligonucleotide.
Choose pairs of primers with the highest percent match score and lowest entropy (i.e., a minimum ΔG
of about –4 kcal/mol) (Hubé et al. 2005). If these oligonucleotides are inefﬁcient in hot start PCRs, use
enhancers in the ampliﬁcation reaction (see below). If all else fails, consider reducing the entropy of
the oligonucleotides by introducing null mutations into the central regions of GC-rich oligonucleo-
tides (see, e.g., Sahdev et al. 2007).
Many additives have been reported to enhance PCRs containing GC-rich templates and primers
(see Table 1). Their effects are unpredictable, and using them—either singly or in combination—does
not guarantee improvement in the efﬁciency of ampliﬁcation of DNA substrates with substantial
secondary or tertiary structure. The chances of success are increased if several enhancers are used
simultaneously (see, e.g., Musso et al. 2006; Ralser et al. 2006; Zhang et al. 2009). Alternatively, kits
containing combinations of additives are available from commercial manufacturers. Most of the kits
are believed to contain betaine, in addition to other unspeciﬁed additives.
If the combination of touchdown PCR, hot start PCR, and cocktails of additives fails to improve
the ampliﬁcation of a recalcitrant GC-rich template, altering the cycling conditions can solve the
problem. For example, Frey et al. (2008) describe the use of a combination of slow ramping rates
(2.5˚C/sec) and slow cooling rates (1.5˚C/sec) to approach the annealing temperature. An essential
component of “slowdown” PCR is the inclusion in the reaction mixture of 7-deaza-2′-
deoxyguanosine.
TABLE 1. Enhancers commonly used to improve the efficiency of amplification of GC-rich templates
Enhancer
Mode of action
Reference
Betaine (N,N,N-trimethylglycine) (0.5–1 M)
Reduces the formation of secondary structures by
lowering the Tm of GC-rich regions
Rees et al. 1993; Henke et al. 1997
7-Deaza-2′-deoxyguanosine
Eliminates Hoogsteen bond formation but does not
impair Watson–Crick base pairing.
McConlogue et al. 1988
DMSO and low-molecular-weight sulfones
(1%–10%)
Bind to the major and minor grooves of template
DNA and destabilize the double helix
Winship 1989; Pomp and Medrano 1991;
Varadaraj and Skinner 1994; Chakrabarti and
Schutt 2001
Formamide (1%–5%)
Interferes with hydrogen-bond formation between
the two strands of DNA
Sarkar et al. 1990
Polyethylene glycol (5%–15%)
A crowding agent; can also destabilize regions of
DNA with high Tm
Ethylene glycol and 1,2-propanediol
Decrease melting temperature of DNAs by an
unknown mechanism apparently different from
that of betaine
Zhang et al. 2009
Glycerol (5%–20%), bovine serum albumin
(0.1 mg/mL), or gelatin (0.1%–1.0%)
General enzyme-stabilizing agents
Giambernardi et al. 1998
Nonionic detergents (e.g., Triton X-100
[0.1%–0.5%]; Nonidet P-40 [0.1%–
0.5%])
Displace traces of ionic detergents used in
preparation of templates
Gelfand and White 1990
168
Cite this protocol as Cold Spring Harb Protoc; doi:10.1101/pdb.prot095141
M.R. Green and J. Sambrook
 
Cold Spring Harbor Laboratory Press
 at University of Hong Kong Libraries on July 26, 2026 - Published by 
http://cshprotocols.cshlp.org/
Downloaded from 
RECIPES
Additive Solution (5×)
Reagent
Quantity (for 10 mL) Final concentration
Betaine (5 M)
5.4 mL
2.7 M
Dithiothreitol (1 M)
67 µL
6.7 mM
Dimethyl sulfoxide
670 µL
6.7% (v/v)
Bovine serum albumin (2 mg/mL)
275 µL
55 µg/mL
Store at 4˚C for no longer than a week.
GC-Rich Ampliﬁcation Buffer (10×)
Reagent
Quantity (for 10 mL)
Final concentration
Ammonium sulfate (1 M)
1.66 mL
166 mM
MgCl2 (1 M)
300 µL
30 mM
Tris-HCl (1 M, pH 8.5)
6.6 mL
0.66 M
Tween 20
10 µL
0.1% (v/v)
Store at 4˚C.
REFERENCES
Chakrabarti R, Schutt CE. 2001. The enhancement of PCR ampliﬁcation by
low molecular weight amides. Nucleic Acids Res 29: 2377–2381.
Frey UH, Bachmann HS, Peters J, Siffert W. 2008. PCR-ampliﬁcation of GC-
rich regions: ‘Slowdown PCR’. Nat Protoc 3: 1312–1317.
Gelfand DH, White TJ. 1990. Thermostable DNA polymerases. In PCR
protocols: A guide to methods and applications (ed. Innes MA, et al.),
pp. 121–141. Academic Press, San Diego.
Giambernardi TA, Rodeck U, Klebe RJ. 1998. Bovine serum albumin revers-
es inhibition of RT-PCR by melanin. Biotechniques 25: 564–566.
Green MR, Sambrook J. 2018. Hot start polymerase chain reaction (PCR).
Cold Spring Harb Protoc doi: 10.1101/pdb.prot095125.
Henke W, Herdel K, Jung J, Schnorr D, Loening SA. 1997. Betaine improves
the PCR ampliﬁcation of GC-rich sequences. Nucleic Acids Res 25:
3957–3958.
Hubé F, Reverdiau P, Iochmann S, Gruel Y. 2005. Improved PCR method
for ampliﬁcation of GC-rich DNA sequences. Mol Biotechnol 31: 81–84.
McConlogue L, Brow MA, Innis MA. 1988. Structure-independent DNA
ampliﬁcation by PCR using 7-deaza-2′-deoxyguanosine. Nucleic Acids
Res 16: 9869.
Musso M, Bocciardi R, Parodi S, Ravazzolo R, Ceccherini I. 2006. Betaine,
dimethyl sulfoxide, and 7-deaza-dGTP, a powerful mixture for ampli-
ﬁcation of GC-rich sequences. J Mol Diagn 8: 544–550.
Pomp D, Medrano JF. 1991. Organic solvents as facilitators of polymerase
chain reaction. Biotechniques 10: 58–59.
Ralser M, Querfurth R, Warnatz H-J, Lehrach H, Yaspo M-L, Krobitsch S.
2006. An efﬁcient and common enhancer mix for PCR. Biochem
Biophys Res Commun 347: 747–751.
Rees WA, Yager TD, Korte J, von Hippel PH. 1993. Betaine can eliminate the
base pair composition dependence of DNA melting. Biochemistry 32:
137–144.
Sahdev S, Saini S, Tiwari P, Saxena S, Singh Saini K. 2007. Ampliﬁcation of
GC-rich genes by following a combination strategy of primer design,
enhancers and modiﬁed PCR cycle conditions. Mol Cell Probes 21:
303–307.
Sarkar G, Kapelner S, Sommer SS. 1990. Formamide can dramatically
improve the speciﬁcity of PCR. Nucleic Acids Res 18: 7465.
Varadaraj K, Skinner DM. 1994. Denaturants or cosolvents improve the
speciﬁcity of PCR ampliﬁcation of a G + C-rich DNA using genetically
engineered DNA polymerases. Gene 140: 1–5.
Winship PR. 1989. An improved method for directly sequencing PCR am-
pliﬁed material using dimethyl sulphoxide. Nucleic Acids Res 17: 1266.
Zhang Z, Yang Y, Meng L, Liu F, Shen C, Yang W. 2009. Enhanced ampli-
ﬁcation of GC-rich DNA with two organic solvents. Biotechniques 47:
775–779.
Cite this protocol as Cold Spring Harb Protoc; doi:10.1101/pdb.prot095141
169
PCR Amplification of GC-Rich Templates
 
Cold Spring Harbor Laboratory Press
 at University of Hong Kong Libraries on July 26, 2026 - Published by 
http://cshprotocols.cshlp.org/
Downloaded from 
doi: 10.1101/pdb.prot095141
Cold Spring Harb Protoc; 
 
Michael R. Green and Joseph Sambrook
 
Polymerase Chain Reaction (PCR) Amplification of GC-Rich Templates
Service
Email Alerting
 
click here.
Receive free email alerts when new articles cite this article - 
Categories
Subject
Cold Spring Harbor Protocols.
Browse articles on similar topics from 
 (185 articles)
Polymerase Chain Reaction (PCR), general
 (145 articles)
Polymerase Chain Reaction (PCR)
 (1321 articles)
Molecular Biology, general
 (86 articles)
Amplification of DNA by PCR
http://cshprotocols.cshlp.org/subscriptions 
go to: 
Cold Spring Harbor Protocols 
To subscribe to 
© 2019 Cold Spring Harbor Laboratory Press
 
Cold Spring Harbor Laboratory Press
 at University of Hong Kong Libraries on July 26, 2026 - Published by 
http://cshprotocols.cshlp.org/
Downloaded from 

