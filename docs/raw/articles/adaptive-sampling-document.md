---
source_url: 
source_type: article
ingested: 2026-07-19
sha256: ae04c851c22f7a5bb6b47f35dc715a732687d664810d48406c3d1312b0623811
---

PROTOCOL
Adaptive sampling
V ADS_S1016_v1_revN_05Sep2025
FOR RESEARCH USE ONLY
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 1
Contents
Quick Start
1. Introduction
2. Sample preparation and analysis
3. Targeting and buffering a .bed file
4. MinKNOW UI and dialogs
5. Final notes
Advanced guide
6. Introduction
7. Sample preparation and analysis
8. Targeting and buffering
9. Library length considerations
10. Strand directionality
11. Depletion mode
12. Device specifications
13. Where to find, create, and modify FASTA and .bed files
14. Adaptive sampling catalogue
15. Troubleshooting
16. MinKNOW UI and dialogs
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 2
1. Introduction
Adaptive sampling introduction
In some sequencing applications, the focus of study — a single gene, or a selection of genomic
regions — makes up a small fraction of the genome or sample. In these cases, whole-genome
sequencing can be inefficient and costly. Targeted sequencing is a term used to describe
strategies that reduce the time spent sequencing regions that are not of interest, which
significantly reduces the amount of data required to achieve the desired depth of the regions of
interest. This reduces sequencing costs and the data analysis burden, and enables a quicker
workflow. Targeted sequencing using nanopore technology can be achieved in several ways:
amplicon sequencing
pull-down
adaptive sampling
Oxford Nanopore sequencing allows real-time decoding of the region of the genome being
sequenced. This characteristic allows decisions to be made in real time on whether a particular
strand is of interest or not. This called adaptive sampling, and it can perform real-time selection
of reads when the sequencing software (MinKNOW) is supplied with a .bed file containing the
regions of interest (ROI) and a FASTA reference file.
Adaptive sampling offers a fast and flexible method to enrich regions of interest by rejecting off-
target regions: target selection takes place during sequencing itself, with no requirement for
upfront sample manipulation. Prepare and load the library as normal and select “adaptive
sampling” in MinKNOW (you will need to upload a FASTA file with the reference as well as a .bed
file detailing the regions of interest). Once sequencing begins, due to the real-time nature of
nanopore sequencing, MinKNOW identifies whether the strand that is being sequenced is within
the ROI. If the read does not map to the ROI, MinKNOW reverses the polarity of the applied
potential, ejecting the strand from the pore so that it is able to accept a new strand. Off-target
strands are continually rejected until a strand from the ROI is detected and sequencing is allowed
to proceed.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 3
Figure 1. Overview of an adaptive sampling experiment
Adaptive sampling can run in two different modes: enrichment and depletion. In enrichment
mode you would upload ROIs to MinKNOW, which then rejects strands that fall outside of these
regions. In depletion mode, upload targets that are not of interest (e.g. host DNA in a host :
microbiome metagenomic analysis) to MinKNOW, which then rejects strands that fall within these
regions. We observe an enrichment for ROI of ~5-10-fold when using adaptive sampling, and we
outline our advice on how this can be achieved below. When targeting regions within human
genomes, we find this level of enrichment to be robust if the total fraction that is being targeted
is <10% of the total genome. This allows you to obtain a mean depth of >20-40x of ROI on a
MinION Flow Cell.
For a visual overview of adaptive sampling, refer to this video: Adaptive sampling on nanopore
technology.
2. Sample preparation and analysis
Although adaptive sampling does not require any particular sample preparation,
there are some aspects of library preparation which benefit an adaptive
sampling experiment.
There are two main aspects to consider when trying to maximise output: pore occupancy and
library fragmentation.
Pore occupancy
The adaptive sampling methodology is based on rejecting unwanted DNA strands to free up the
pore, ready to capture a new strand. This can cause a significant reduction in pore occupancy, as
the constant rejection of strands reduces the amount of time that pores are occupied with a
strand. Therefore, maintaining high pore occupancy is one of the most important aspects in
adaptive sampling. To achieve this, we recommend loading a higher amount of sample than you
would normally use for a sequencing run. The right amount of DNA to load into the flow cell
needs to be calculated from the point of view of molarity instead of mass (explained in more
detail below).
Library fragmentation
This is important for two reasons: firstly, the fragment length affects the molarity, which is the
main measure of DNA to be loaded in an adaptive sampling run. Secondly, adaptive sampling
runs are more likely to block pores due to the high amount of strand rejection. Using a library
made up of shorter fragments increases flow cell longevity and therefore data output, since the
library causes less blocking and gives a higher molarity with lower amounts of total DNA. Not
only does shearing reduce blocking, but it can also increase enrichment depending on the size of
your individual ROIs. If most of your ROIs are a few kb long (e.g. 2–5 kb), then using a library with
an N50 in the 30 kb range is going to be wasteful. This is because every time a strand is accepted
for sequencing, the pore will be occupied sequencing 30 kb of data to extract 2–5 kb of on-target
sequence. This is a potential waste of 25–28 kb, when the pore could be sampling more reads
during this timeframe instead of sequencing off-target.
Another method to increase output from an adaptive sampling run is to perform multiple flow
cell washes throughout the run and reload the library. However, by reducing the library fragment
size you can reduce the number of flow cell washes needed to maximise the output from a
sequencing experiment.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 4
Figure 2 shows the difference in pore blocking in adaptive sampling mode over time with two
different fragment size libraries: 5 kb and 25 kb. Each bar represents the number of pores
available for sequencing every 1.5 hours throughout the run. Attrition of channels due to blocked
pores occurs at a faster rate in the library with the longer fragments. Although flow cell washing
can recover some lost pores, it is a hands-on process which adds hands-on time to the run. For
this reason, it is important to give consideration the size of your library when designing adaptive
sampling experiments to keep blocking to a minimum and reduce the need to interact with the
flow cell.
Figure 2. Pore scans for 6 kb (left) and 20 kb (right) libraries in adaptive sampling runs without
flow cell washes.
The fragment size will also affect the molarity of your sample if you are using a Qubit or other
mass-related measurement to calculate the amount of DNA loaded into the flow cell. Qubit is the
recommended method for evaluating your DNA library concentration, but this should be
converted into a molarity concentration which can be done based on your average fragment
length. You can evaluate fragment lengths using the Agilent Femto Pulse (for fragments >10 kb),
or the Agilent Bioanalyzer (for fragments <10 kb).
Using the average molecular weight of a base pair (660 g/mol), you can easily calculate the
molarity of the sample. This will make the mass of DNA needed for short and long libraries quite
different when normalising for the same molarity. Molarity is an important property to consider,
since the number of DNA ends available to be captured by the pore is the main factor in
improving pore occupancy. The ideal molarity when using the latest V14 chemistry is 50–65 fmol
per load.
With a library which has a normal read length distribution centred at 6.5 kb (Figure 3), 50 fmol
would correspond to approximately 200 ng, according to the following calculations:
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 5
Total mass of a mol of 6.5 kb fragments: 6500 base pairs x 660 (g/mol) =
4,290,000 g in 1 mole
Multiply this by the number of femtomoles needed: 4,290,000 x 50 x 10^-15
= 2.145 x 10^-7
Convert grams to ng: 2.145 x 10^-7 x 1,000,000,000 = 214.5 ng
To facilitates these calculations, you can use a biomath calculator such as the following: Biomath
Calculators | DNA Calculator | Vector Insert Ratio
Figure 3. Read length distribution of a library with an N50 of 6.5 kb.
This is a rough approximation, based only on the N50 of the library. The real molarity calculation
is more intricate to calculate, as you need to consider the range of the distribution. Nevertheless,
this is a good approximation to understand the amount of DNA you would need for an adaptive
sampling run. It is also worth noting that these calculations and values are assuming optimal
ligation efficiencies. If for any reason a library is not ligating as efficiently, we advise adding more
sample to the sequencing run. Note that a higher DNA input has not been shown to affect the run
negatively when using V14 chemistry up to a maximum of 600 ng.
For more detailed information about ideal sample metrics for adaptive sampling runs, refer to the
Adaptive sampling advanced guide below.
3. Targeting and buffering a .bed file
1
Targeting and buffering a .bed file
Disclaimer: This section was shortened for the purpose of providing the most useful, quick-use
information. The cases described are ideal adaptive sampling use cases. For detailed information of
targeting (how it works) and buffering, please visit the “Targeting and buffering page” in the Advanced
guide section. For information on depletion mode, refer to the corresponding section of the advanced
guide.
Adaptive sampling ideally requires a reference (.fasta) and a bed file (.bed) to know which strands
to select for sequencing. The reference contains a representation of the whole sample, and the
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 6
.bed file serves as a mask to subset the reference and inform MinKNOW which regions of the
reference are of interest.
To provide maximum benefit to enrichment, the .bed files should ideally target less than 5% of
the sample. However, you can target as much as 10% for reasonable returns of enrichment (for
instance the RRMS panel available in the Adaptive Sampling Catalogue). Targeting more than 10%
will reduce the enrichment values obtained.
As an ideal targeting example, we will use the hereditary cancer panel also available in the
Adaptive Sampling Catalogue. This example panel targets ~0.54% of the human genome. This
means that in a sample composed exclusively of human DNA, this panel would instruct MinKNOW
to accept and sequence ~0.54% of all the reads captured by pores in the flow cell.
The decision to accept or reject a read is made on the first chunk of a read, and this is the only
information that MinKNOW will have to make a decision. This causes MinKNOW to reject strands
which start (first chunk) in the flanking regions of a target, but does not actually hit the target
within the first chunk. To account for this behaviour we use a “buffer” which is added to the side
of the regions of interest (ROI). This will allow MinKNOW to accept a strand which starts in a
flanking region and that will likely extend into the ROI.
To define the buffer, you need to know the read length distribution of the library being
sequenced. Ideally the amount of buffer to add should be equal to ~N10 of the read length
distribution of the library. The buffer value does not need to be very precise due to the nature of
a library red lengths being a normal distribution. This means that as long as the library
preparation method stays consistent, a characterisation of the read length distribution is not
necessary for every single library made.
As a rule of thumb, for a library with a normal distribution with an N50 of ~8 kb, aim for adding
20 kb of buffer.
There are several caveats and exceptions to this, mostly around how much the buffer with modify
the total amount targeted. For instance, for the hereditary panel mentioned above (which targets
0.54% of the human genome) a 20 kb buffer will make it target ~0.67% if added site-specifically.
For more information about the details of buffering, refer to the “Targeting and buffering page”
in the advanced guide section.
Lastly, Oxford Nanopore provides a page for checking your .bed file, which should be done before
and after buffering:
Bed file checker - Bed Bugs
This page will catch errors with the .bed files and prevent runs from crashing. You will need to
provide the same reference file which you used to acquire the .bed file coordinates and use this
same reference during the run setup. If Bed Bugs is reporting issues with your .bed file (besides
overlapping), these will need to be fixed, before using the bufferer.py script. Furthermore, Bed
Bugs has now a functionality to automatically buffer your .bed file with a directionally-aware 10
kb buffer. If your .bed file shows no errors besides a “self overlap warning, a new options will be
available to download an “buffered” version of your bed file (Figure 4). The buffer size is currently
set to 10 kb and cannot be changed. It will not fit all .bed files and applications, but it is a good
start for most ideal size .bed files. for more information of .bed file buffer sizes, please visit the
“Targeting and buffering page” in the advanced guide section.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 7
Figure 4. Screenshot of Bed Bugs after validation of a .bed file containing no run threatening
errors.
Note: Sometimes, you may observe a “self overlap” issue reported by Bed Bugs. The reason for
this is that after using the buffering script, the new .bed file will have overlapping region defined.
However these overlapping regions are necessary as they are different depending on the strand
(coding or non-coding). If you see this error reported by Bed Bugs, it will not affect MinKNOW
performance and you can ignore the error.
4. MinKNOW UI and dialogs
During an adaptive sampling experiment, MinKNOW carries out basecalling and
alignment with adaptive sampling in parallel with live basecalling. The
MinKNOW user interface shows dialogs with information for both processes.
Here, we explain where you can find each type of information.
Firstly, there are separate sections in MinKNOW for uploading a live sequencing alignment
reference and .bed file, and an adaptive sampling alignment reference and .bed file. Both the
reference FASTA file and the .bed file can be the same in both sections (hence the Alignment
section is pre-populated with the files uploaded in the Adaptive Sampling section). Nevertheless,
it is important to understand the function of each file as you can get a better ongoing view of
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 8
coverage obtained throughout the run, by loading a different .bed file in the live alignment
section.
The adaptive sampling files are loaded in the 3. Run Options section under the section named
“Adaptive Sampling” - Figure 5, top section. These will be used for targeting your sample and will
affect the reads which get selected by MinKNOW for sequencing. The .bed file loaded in this
section should also contain a buffer region, when applicable. For more information on this, refer
to previous guide sections about buffers.
The live alignment files are loaded in the 4. Analysis section of the run setup in MinKNOW. The
purpose of the FASTA reference is to align the reads after live basecalling and therefore should be
the same file as the one loaded for the adaptive sampling decision. This will allow to output BAM
files containing the basecalled and aligned sequence in real time.
The .bed file in the 4. Analysis section is used for two different processes: Firstly, it provides an
identifier in the sequencing summary reporting whether the complete read hit the regions
described in the .bed file loaded in 4. Analysis. This is shown in the sequencing_summary.txt file
under the column bed_alignment and populated with a 0 or a 1, for whether it hits or does not hit
the .bed file. Secondly, this .bed file is used to check for the coverage obtained at each of the
regions described in the same .bed file. You can follow this live during the run in the Alignment
hits tab of MinKNOW.
To make the most of the live alignment feature and the coverage tracking feature, load the
buffered .bed file (bed file containing the ROI + buffer) in the 3. Run options Adaptive sampling
section, and the .bed file containing only ROI (unbuffered) in the 4. Analysis section. This
guarantees that you only track coverage on the targets of interest, and will give a more accurate
description of coverage on the ROIs. The .bed file provided in the alignment section does not
modify the run output and is not strictly necessary. Nevertheless, depending on the amount of
buffer added to each region in the adaptive sampling .bed, having a targets only (unbuffered)
.bed in the alignment section may provide a more accurate coverage report. Importantly, the
coverage tracking (and therefore the files provided in 4. Analysis) does not modify the
sequencing run in any way. It is a tool for real-time alignment and for checking during a run how
much coverage has already been obtained for each bed region. Lastly, note that the coverage
reported is referring to the percentage of sequence that has been basecalled. This means that if
the live basecalling is not keeping up, the coverage reported is only relative to the percentage
already basecalled.
Live alignment is a computationally demanding process which can easily affect the adaptive
sampling decision time. Therefore, please refer the tables of advised metrics on how many flow
cells you can run with this feature per device to avoid affecting enrichment rates. To prevent live
alignment being used, remove the reference sequence denoted “1” in Figure 5.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 9
Figure 5. MinKNOW dialogs for uploading the FASTA reference file and .bed file for the adaptive
sampling panel (top, sections 3 and 4) and the live basecalling panel (bottom, sections 1 and 2).
You can see which files are being used in each section in the first page of the run summary once
the run is started. An example of this panel is shown in Figure 6.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 10
Figure 6. MinKNOW front panel containing run summary details. Alignment information has been
labelled accordingly.
5. Final notes
Final notes
The information provided in this quick start guide is a starting point for learning how to use
adaptive sampling. Caveats and exceptions apply to most sections of the quick start guide.
Moreover, our sequencing devices have limits on the amount of real-time analysis they can
perform, and adaptive sampling is a real-time analysis tool with minimal latency. Adaptive
sampling therefore demands a considerable amount of resources from the machines. You can
find recommendations on the limits of adaptive sampling in the “Advanced guide” pages.
We also provide a troubleshooting guide, along with more in-depth explanation of how adaptive
sampling works. We welcome all feedback on the new guide and would like to hear what details
you would like to see explained in more detail. More information will be added to this guide over
time, in particular regarding features surrounding the adaptive sampling capabilities: coverage
tracking, multiplexing, barcode balancing, etc.
6. Introduction
Adaptive sampling introduction
In some sequencing applications, the focus of study — a single gene, or a selection of genomic
regions — makes up a small fraction of the genome or sample. In these cases, whole-genome
sequencing can be inefficient and costly. Targeted sequencing is a term used to describe
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 11
strategies that reduce the time spent sequencing regions that are not of interest, which
significantly reduces the amount of data required to achieve the desired depth of the regions of
interest. This reduces sequencing costs and the data analysis burden, and enables a quicker
workflow. Targeted sequencing using nanopore technology can be achieved in several ways:
amplicon sequencing
pull-down
adaptive sampling
Oxford Nanopore sequencing allows real-time decoding of the region of the genome being
sequenced. This characteristic allows decisions to be made in real time on whether a particular
strand is of interest or not. This called adaptive sampling, and it can perform real-time selection
of reads when the sequencing software (MinKNOW) is supplied with a .bed file containing the
regions of interest (ROI) and a FASTA reference file.
Adaptive sampling offers a fast and flexible method to enrich regions of interest by rejecting off-
target regions: target selection takes place during sequencing itself, with no requirement for
upfront sample manipulation. Prepare and load the library as normal and select “adaptive
sampling” in MinKNOW (you will need to upload a FASTA file with the reference as well as a .bed
file detailing the regions of interest). Once sequencing begins, due to the real-time nature of
nanopore sequencing, MinKNOW identifies whether the strand that is being sequenced is within
the ROI. If the read does not map to the ROI, MinKNOW reverses the polarity of the applied
potential, ejecting the strand from the pore so that it is able to accept a new strand. Off-target
strands are continually rejected until a strand from the ROI is detected and sequencing is allowed
to proceed.
Figure 1. Overview of an adaptive sampling experiment
Adaptive sampling can run in two different modes: enrichment and depletion. In enrichment
mode you would upload ROIs to MinKNOW, which then rejects strands that fall outside of these
regions. In depletion mode, upload targets that are not of interest (e.g. host DNA in a host :
microbiome metagenomic analysis) to MinKNOW, which then rejects strands that fall within these
regions. We observe an enrichment for ROI of ~5-10-fold when using adaptive sampling, and we
outline our advice on how this can be achieved below. When targeting regions within human
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 12
genomes, we find this level of enrichment to be robust if the total fraction that is being targeted
is <10% of the total genome. This allows you to obtain a mean depth of >20-40x of ROI on a
MinION Flow Cell.
For a visual overview of adaptive sampling, refer to this video: Adaptive sampling on nanopore
technology.
How adaptive sampling works
Adaptive sampling is used to target ROIs in the genome by ejecting strands from the pore that do
not map in these regions. As strands are captured by the pore the start of the reads are
basecalled and aligned to a reference. If the strand maps to the ROI provided, the software allows
the strand to continue through the pore and be sequenced. If the strand is off target, it is ejected
from the pore by reversing the applied potential at the electrode and released back to the top
side of the membrane. Rejection of strands reduces the amount of time that pores are occupied
with a strand, freeing the pore to capture another strand which could be of interest.
Adaptive sampling can be run in two modes:
Enrichment: Sequences present in the target file are accepted and sequenced. In this mode,
decisions follow the logic:
If sequence aligns in .bed region: Accept
If sequence aligns outside of .bed region: Reject
If sequence does not align: Reject
Depletion: Sequences present in the target file are rejected back to the cis side of the membrane.
If sequence aligns in .bed region: Reject
If sequence aligns outside of .bed region: Accept
If sequence does not align: Accept
Notes:
Reads which cannot be aligned have different destination in enrichment and
depletion modes, according to the description above.
If only a FASTA file is uploaded then the previous rules would apply equally
to this file instead of the .bed file.
Target sequences are defined by use of the .bed format file. This file specifies the start and end
coordinates of the target sequences based on a reference (FASTA) file which contains the actual
sequence of the sample. If you do not provide a .bed file, then the reference (FASTA) is not subset,
and all the sequences present in the reference will be used as a target. This means that if no .bed
file is provided, in enrichment mode, everything present in the reference will be accepted, and in
depletion mode, everything will be rejected.
The best practice, regardless of whether you are using adaptive sampling in enrichment or
depletion mode, is to provide a FASTA reference containing as much information about the
sample as possible, and then use a .bed file to subset the ROIs. This is because when a particular
sequence in the sample is not present in the reference, it is more likely to be ‘force-aligned’ to the
wrong reference. For example, if you target the complete sequence of chromosome 7 from a
human sample and provide a FASTA reference containing only chromosome 7, sequences from
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 13
other chromosomes will be force-aligned to the chromosome 7 reference. This will cause for a
large amount of off-target sequences to be accepted, affecting the enrichment ability of adaptive
sampling.
Defining concepts and vocabulary
ROI (Region of Interest)
The ROI is your region of interest, and in this guide, it will be used to refer to your actual target of
interest excluding the buffer regions. For an adaptive sampling experiment, submit a .bed file
containing the coordinates for the ROIs + buffer region. This file is uploaded under the reference
input in the “Adaptive sampling” section in the Run Options tab the run setup in MinKNOW.
You can upload another .bed file in the Analysis tab in MinKNOW UI under the alignment options.
MinKNOW uses this file to check whether a strand falls within the targets set in this .bed
uploaded in the Analysis tab. This is a separate process to the adaptive sampling alignment and
is used to calculate coverage of targets in real-time whenever live alignment is turned on. The
presence of this second .bed file also populates the column alignment_bed_hits in the final
sequencing_summary.txt . This alignment .bed file is optional and not necessary for the normal
functioning of adaptive sampling. Because the alignment .bed file is used for real-time coverage
calculation, you can make this calculation more accurate by providing a .bed file containing ROIs
only, as opposed to the .bed loaded in the Adaptive Sampling section where the .bed contains
ROI + buffer. More information on how and where to load each one of these files is shown in the
“UI information and dialogs” section of this guide.
Buffer region
Buffer regions are flanking regions added to the side of every ROI. Since adaptive sampling only
aligns the beginning of each captured strand, these regions allow the software to accept reads
which begin with a sequence that may not map to the ROI but may extend into it as the strand
continues being sequenced. By accepting reads which map to these flanking regions, you
increase the number of accepted reads that hit your target.
Target
“Target” refers to the sequence targeted by the adaptive sampling process. This includes ROI +
buffer region and accounts for the total sequence that adaptive sampling uses to decide whether
to accept or reject a strand.
The calculation of the percentage of sample targeted by AS needs to consider the prevalence of
the targeted regions in the sample. It is important to consider the relative abundance of the
targeted sequences in your sample to calculate the total amount of genomic sequence targeted
from that same sample. For instance, if targeting 50% of the E. coli genome spiked into a human
sample, but the E. coli genome representation only makes up 10% of the total amount of DNA
present in the sample, this means you are targeting 5% of the genomic sequences present in the
sample. This is important, as the percentage of sequence targeted from the overall sample affects
the performance of the adaptive sampling enrichment.
Note: there is no wrong targeting range, and adaptive sampling will work with any target range
and distribution of ROIs. However, the larger the amount you target, the lower your potential
enrichment. You can read more details on this in the “Defining buffer regions” section.
Reference
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 14
The reference is a FASTA file which contains the sequences present in a sample for a particular
sequencing experiment. This should, whenever possible, represent the complete sample. So if
your sample contains three genomes, your reference should also contain the sequence for these
same three genomes to prevent possible false positives in the adaptive sampling decision.
Whenever you provide an incomplete reference (a reference that does not represent the totality
of your sample), the software will try to force-align the reads that are not represented in the
reference. In the case of similar sequences, this could cause miss-alignments due to the lack of a
full reference. A common example of this, is providing the reference for a single chromosome,
which will cause similar/repetitive sequences in other chromosomes to be force-aligned to the
single chromosome reference provided.
In the case of environmental samples, you may not know all the genomes contained within the
sample. An example of adaptive sampling use in this case is a depletion approach to reject all the
known genomes present in the sample to enrich for unknown genomes. In this case, a reference
accounting for all the sequences in the sample cannot be used.
FASTA files can be obtained from NCBI in full for a particular genome, or subset to contain only
particular parts of the genome (this use case will be discussed in more detail for the MinION
Mk1C in the “Devices” section of this guide).
Choosing the correct reference FASTA file depends on the ROIs you are planning to target. If the
ROIs were obtained from an annotation file, you will need to use the reference FASTA that is
coupled with this annotation file. To avoid misalignments, you will need to use the full reference
genome when using a target .bed file.
The UCSC Table browser is a good option to look for reference FASTA files and associated
annotations files. The NCBI RefSeq database is another good option for accessing reference
FASTA files with stable genome annotation for a wide range of organisms. However, these are
only two examples of databases that can be useful, and other options are available. The most
important point to consider is to use the same reference for the adaptive sampling sequencing
run as the reference used to make the annotation.
.bed files
The .bed file is a text file with a minimum of three columns up to 12
(https://samtools.github.io/hts-specs/BEDv1.pdf, but currently only the first three are mandatory
for adaptive sampling). .bed files are used to subset the provided reference. The first column is
the sequence name identifier from the provided FASTA reference. The second column is the
coordinate at which the target region starts, and the third column is the final coordinate of the
target region. .bed files function as a mask for the FASTA file, which should ideally contain the
sequences for the whole sample, allowing you to define your targets for enrichment.
Advanced options: The 6th column (referring the direction of a sequence) is usable if present.
This is not mandatory and targeting will work without it. However by providing the 6th column
with the directionality, you are telling MinKNOW you are only interested in that particular
sequence from one of the strands only. By duplicating a region and having opposing signs in the
6th column, you can target the sequence in both strands. Additionally you can also use a “.” (dot)
in the 6th column to express that you are interested in both strands. You can read more details on
this in the “Strand directionality” section.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 15
Figure 2. Conjugation of a .bed file sequence identifier with a FASTA identifier (circled in red).
Enrichment
Enrichment is the metric used for evaluating the performance of adapting sampling. This metric
compares the on-target output from an adaptive sampling run vs the on-target output from a
normal sequencing run. Since the output of a flow cell depends mostly on the number of
available pores, output is normalised per number of pores used during the sequencing and then
compared with the same normalised output from the non-adaptive sampling run. The calculation
is made as follows:
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 16
7. Sample preparation and analysis
Although adaptive sampling does not require any particular sample preparation,
there are some aspects of library preparation which benefit an adaptive
sampling experiment.
There are two main aspects to consider when trying to maximise output: pore occupancy and
library fragmentation.
Pore occupancy
The adaptive sampling methodology is based on rejecting unwanted DNA strands to free up the
pore, ready to capture a new strand. This can cause a significant reduction in pore occupancy, as
the constant rejection of strands reduces the amount of time that pores are occupied with a
strand. Therefore, maintaining high pore occupancy is one of the most important aspects in
adaptive sampling. To achieve this, we recommend loading a higher amount of sample than you
would normally use for a sequencing run. The right amount of DNA to load into the flow cell
needs to be calculated from the point of view of molarity instead of mass (explained in more
detail below).
Library fragmentation
This is important for two reasons: firstly, the fragment length affects the molarity, which is the
main measure of DNA to be loaded in an adaptive sampling run. Secondly, adaptive sampling
runs are more likely to block pores due to the high amount of strand rejection. Using a library
made up of shorter fragments increases flow cell longevity and therefore data output, since the
library causes less blocking and gives a higher molarity with lower amounts of total DNA. Not
only does shearing reduce blocking, but it can also increase enrichment depending on the size of
your individual ROIs. If most of your ROIs are a few kb long (e.g. 2–5 kb), then using a library with
an N50 in the 30 kb range is going to be wasteful. This is because every time a strand is accepted
for sequencing, the pore will be occupied sequencing 30 kb of data to extract 2–5 kb of on-target
sequence. This is a potential waste of 23–25 kb, when the pore could be sampling more reads
during this timeframe instead of sequencing off-target. Lastly, the use of longer fragments may
cause the flow cell to block longer, requiring flow cell washes to be performed more frequently to
extract maximum output from the flow cell.
Another method to increase output from an adaptive sampling run is to perform multiple flow
cell washes throughout the run and reload the library. However, by reducing the library fragment
size you can reduce the number of flow cell washes needed to maximise the output from a
sequencing experiment.
Figure 3 shows the difference in pore blocking in adaptive sampling mode over time with two
different fragment size libraries: 5 kb and 25 kb. Each bar represents the number of pores
available for sequencing every 1.5 hours throughout the run. Attrition of channels due to blocked
pores occurs at a faster rate in the library with the longer fragments. Although flow cell washing
can recover some lost pores, it is a hands-on process which adds hands-on time to the run. For
this reason, it is important to give consideration the size of your library when designing adaptive
sampling experiments to keep blocking to a minimum and reduce the need to interact with the
flow cell.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 17
Figure 3. Pore scans for 6 kb (left) and 20 kb (right) libraries in adaptive sampling runs without
flow cell washes.
The fragment size will also affect the molarity of your sample if you are using a Qubit or other
mass-related measurement to calculate the amount of DNA loaded into the flow cell. Qubit is the
recommended method for evaluating your DNA library concentration, but this should be
converted into a molarity concentration which can be done based on your average fragment
length. You can evaluate fragment lengths using the Agilent Femto Pulse (for fragments >10 kb),
or the Agilent Bioanalyzer (for fragments <10 kb).
Using the average molecular weight of a base pair (660 g/mol), you can easily calculate the
molarity of the sample. This will make the mass of DNA needed for short and long libraries quite
different when normalising for the same molarity. Molarity is an important property to consider,
since the number of DNA ends available to be captured by the pore is the main factor in
improving pore occupancy. The ideal molarity when using the latest V14 chemistry is 50–65 fmol
per load.
With a library which has a normal read length distribution centred at 6.5 kb (Figure 4), 50 fmol
would correspond to approximately 200 ng, according to the following calculations:
Total mass of a mole of 6.5 kb fragments: 6500 base pairs x 660 (g/mol) =
4,290,000 g in 1 mole
Multiply this by the number of femtomoles needed: 4,290,000 x 50 x 10^-15
= 2.145 x 10^-7
Convert grams to ng: 2.145 x 10^-7 x 1,000,000,000 = 214.5 ng
To facilitates these calculations, you can use a biomath calculator such as the following:
https://www.promega.co.uk/resources/tools/biomath/
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 18
Figure 4. Read length distribution of a library with an N50 of 6.5 kb.
This is a rough approximation, based only on the N50 of the library. The real molarity calculation
is more intricate to calculate, as you need to consider the range of the distribution. Nevertheless,
this is a good approximation to understand the amount of DNA you would need for an adaptive
sampling run. It is also worth noting that these calculations and values are assuming optimal
ligation efficiencies. If for any reason it is suspected or shown that a library may not be ligating as
efficiently, adding an extra amount of sample is advised. It should be noted that a higher DNA
input has not been shown to affect the run negatively when using Kit 14 up to a maximum of 600
ng.
8. Targeting and buffering
How an adaptive sampling decision is made
Disclaimer: examples and schematics shown in most of this section are for adaptive sampling run in
enrichment mode. Please read this section even if you plan to use depletion mode. The end of this
section will build on the knowledge presented for the enrichment case, to provide advice for depletion
mode use cases.
When creating .bed files for adaptive sampling experiments, it is important to have a general idea
of the mechanisms behind the decision process. Adaptive sampling is a tool for real-time
basecalling and alignment of the reads that are inside the pore at any moment. This means that
as soon as a strand enters a pore, the software starts trying to make a decision on whether this
strand is of interest or not. For this, the following steps are executed in this order:
1. The software acquires one second of data (letting the strand go through the
pore for one second to acquire the first 400 bases – this is called “the
adaptive sampling (AS) chunk”).
2. The adaptive sampling (AS) chunk is sent to the basecaller*.
3. The basecalled sequence is aligned to the reference you provided to
MinKNOW.
4. The location where the sequence aligned to the reference is checked against
the .bed file (or reference only if .bed not provided) that you provided to
MinKNOW.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 19
5. A decision is made based on whether the strand aligned inside or outside
the sequences defined in the .bed file.
6. The strand is left to continue sequencing or ejected from the pore and not
sequenced.
*The basecalling and alignment process in adaptive sampling is independent of the live
basecalling and alignment shown in the running options of MinKNOW. Adaptive sampling has its
own basecaller and aligner; this is set in the background and cannot be modified or turned off.
There are also cases where strands do not align to the reference at all. There are multiple reasons
for this, but the two most common are low strand quality or an incomplete reference. For this
reason, a reference should always represent the entirety of the sample. If there are genomes or
sequences present in the sample which are not present in the reference, or the reference only
contains partial genomes, this will cause some strands to not get aligned as well as increase the
likelihood of false positive alignments. If you are using a complete reference and still see a lack of
alignments, this can come from long pore blocks or low q-scores from the library being sampled.
Adaptive sampling uses the Fast basecalling model (independently from the live basecalling
function in MinKNOW) to basecall the first chunk of acquired data as quickly as possible, and then
uses a special set of alignment parameters (different from live basecalling alignment) to quickly
align these short sequences to the provided FASTA reference. The alignment makes use of
minimap2 short read mode preset (-sr) with some modifications to the default parameters. After
the alignment, the region to which the chunk was mapped is checked against the provided .bed
file, which carries the target regions for adaptive sampling. This is shown in Figure 5.
Figure 5. Schematic of all the important components for the adaptive sampling alignment and
decision process. The top strand is the reference sequence (blue, red and orange), and in green is
the actual length of the DNA strands, with brown marking the beginning of each strand that is
read by adaptive sampling to make a decision. The first example (A) is where the strand’s first
adaptive sampling chunk (brown) maps within the target region defined by the .bed file, and this
strand will be accepted for sequencing. In the second example (B) the adaptive sampling chunk
falls within the buffer region (in red) and therefore the strand is accepted for sequencing. In the
third example (C), the first chunk falls outside the target region and the buffer region; this leads
to a rejection of this strand from the pore, meaning it will not be sequenced.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 20
Defining buffer regions
Defining correct buffer regions is one of the most important tasks before starting an adaptive
sampling run. Buffer regions allows you to capture strands which may align to flanking regions of
your ROI but as they continue being sequenced, will eventually reach the ROI. This allows you to
offset possible coverage drops at the edges of your targets.
Figure 6 shows a similar schematic to Figure 5, but using buffer regions.
Figure 6. Examples of A: a well-defined buffer region, and B: a badly-defined buffer region.
In example A, given the AS target region (pink), the software would accept any strand which
contains a sequence with any regions shown in pink (ROI and buffer). On the other hand, in
example B, the buffer was not defined correctly according to the size of the strand. This results in
a strand that contains some of the target region being rejected, because the first ~400 bases that
are used for the adaptive sampling decision lie outside the buffer region. This example
demonstrates the importance of picking the right length of buffer to add to the flanking regions
of the ROIs. It is not possible to accurately know the length of a strand until after the entire
strand is sequenced. Nevertheless, you can estimate its length based on the read length
distribution of the library as shown in Figure 4. By doing this, you can define the buffer regions
for the individual ROIs. Table 1 below summarises potential outcomes when defining buffer
regions.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 21
Table 1. Summary of how different buffer sizes and fragment lengths affect the adaptive
sampling outcomes.
How to define the right amount of buffer
The buffer size should be defined based on the library’s read length distribution. Figure 7 shows
the read length distribution of a library fragmented with a Covaris g-TUBE. Different Nxx values
are marked for this library.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 22
Figure 7. Read length distribution of a 5 kb library fragmented with a Covaris g-TUBE. The vertical
lines show the N50, N25, N10 and N01 of the read length distribution from left to right.
As a rule of thumb, an N25 to N10 of the read length distribution is a good measure of buffer to
be added to each side of each individual target. Figure 8 shows the results of an enrichment
experiment from two distinct sized libraries enriched using different buffer sizes.
Figure 8. Enrichments obtained from libraries with different buffer sizes, prepared using the
Short Fragment Eliminator Expansion (EXP-SFE001) and the Covaris g-TUBE.
However, the buffer size also depends on the details of your ROI. Because the buffer is added on
a per-individual region basis, the total number of individual regions becomes an important
measure when deciding the amount of buffer to add. As mentioned in the beginning of this
guide, the total amount of target given to adaptive sampling to make a decision (ROI + buffer) will
determine the degree of enrichment. Because of this, it is important to consider the amount of
buffer added to the target .bed file.
Notes:
Overlapping buffers from closely-located individual targets will not cause
any issues. However, in the case of an overlap, adaptive sampling will treat
the overlapping regions as a single region rather than two separate ones.
Consider also the minimum coverage per individual ROI. The purpose of the
buffer is to help with drop-offs in coverage at the edges of your ROIs.
Therefore you may consider a slightly lower amount of average coverage in
favour of a more homogeneous coverage intra-ROI (meaning a higher
minimum coverage). A simulation ran over 60 different conditions depicts
the impact of the buffer size on the minimum coverage obtained per ROI. As
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 23
shown in Figure 9. below, increasing the amount of buffer reduces the
difference between the minimum coverage and the average coverage of a
given region. This is understandable, as increasing the buffer allows you the
chance to capture longer reads which will only overlap with the ROIs at their
very end, adding coverage to the edges of the ROI.
Figure 9. Simulated data showing the difference between average coverage and minimum
coverage as a percentage of average coverage (%).
Buffer calculations
The examples below illustrate how adding buffer may affect your adaptive sampling run. Table 2
shows examples of two different ROIs relative to the human genome (3.2 Gbases). The following
equation is used to calculate the final target amount for an adaptive sampling decision:
Selection target (bases) = Number of targets ∗ (Nxx ∗ 2) + Total % of genome targeted ∗ genome
size
Table 2. Example ROIs for calculating the total target.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 24
As seen in Table 2, there is a large difference in the number of targets between examples 1 and 2.
According to the equation above, this will result in a significant difference in terms of total target
added from buffer alone. Table 3 contains two columns for each of the previous examples. The
first column contains the total amount of target (ROI + buffer) in bases, and the second column
(%) depicts the value of the first column as a percentage of the human genome. All of the values
shown for each Nxx are based on the read length distribution shown in Figure 7 above. The
second column is effectively the percentage of sample targeted by adaptive sampling assuming
sample homogeneity.
Table 3. Total number of bases targeted for each condition in Table 2 using various buffer sizes.
The amount targeted is also expressed as a percentage of the human genome in the second
column of each example (%).
As seen from Example 2 using N01, adding a buffer increases the adaptive sampling target from
an initial 4.5% of the sample (ROI only) to 20.5%. However, in Example 1, adding the highest
amount of buffer results in an adaptive sampling target of only 0.68% of the total sequence
present in the sample. These are two opposite cases. In Example 1, adding an N01 of the read
length distribution maximises the chances of sequencing a strand that may still extend into the
target without significantly increasing the total sequence target. However, in Example 2, using the
largest buffer size increases the target four-fold, leading you to target over 20% of the sample.
Such a high amount of target decreases the adaptive sampling enrichment power by keeping the
pores occupied for too long sequencing off-target reads.
One way to avoid this is to reduce the Nxx used for adding buffer. In Example 2, an N50 would be
a more reasonable amount of buffer to add to the ROI. Another way of reducing the buffer is to
reduce the average length of the library fragments. If your library has a read length distribution
of >15 kb, shearing the fragments to make them shorter would reduce the values of the Nxx
values picked from the read length distribution.
9. Library length considerations
Library length considerations
As shown in the previous section, the ideal buffer size to be added depends on several factors,
the most important being the read length distribution of your library. The average length of your
library will be important when considering how much you want to get out of your run. If you are
sequencing a library with very short read lengths (~1000 bases), this results in minimal blocking
and also provides the least benefit per flick. Assuming correctly defined buffers, the “benefit per
flick” is the amount of sample that you sequence through when you reject a read. For instance, if
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 25
your library has strands averaging 1000 bases, then every time a read is rejected, the software
“sampled” 1000 bases of the sample. On the other hand, if your library has an average read
length of 30 kb, every time a read is rejected, the software sampled 30 kb. Since the time to to
make a decision and reject is the same for short and long libraries, you can sample the full
genome much faster if you are using longer fragments.
However, there are some downsides to sequencing long libraries. Although they provide faster
sampling power and the ability to phase out regions that you are targeting, they will lead to a
higher rate of flow cell blocking as well as require a higher amount of input to load the necessary
molarity to keep the pore occupancy high. Long libraries will also require more frequent flow cell
washes, and may generate a lower total amount of data from the flow cell due to the higher
chance of terminal pore blocking.
Lastly, it is important to think about the distribution of your targets and their average size. If your
.bed file contains 20,000 targets with an average size per target of 3 kb, using a 30 kb library
could prove detrimental. Aside from a higher rate of pore blocking, every time the pore accepts a
strand for sequencing, it will sequence an average of 30 kb (which at 400 b/s takes 75 seconds),
yielding only 3 kb of useful sequence. With a decision time of ~2 seconds, this gives 75/2 = ~38
reads that the software could have sampled through. In this example, the total target is 60 Mb
(without buffer), which corresponds to ~2% of the human genome. This translates to a probability
of finding your target in 1 out of 50 reads sequenced. Therefore, sequencing a single 30 kb strand
prevents the sampling of 38 reads out of the necessary 50 reads you need to find the next on-
target read. This will detrimentally affect enrichment and the total coverage obtained from using
adaptive sampling.
A better use case of adaptive sampling would be to target e.g., 200 individual regions, with an
average of 60 kb per target. A library sheared with the Covaris g-TUBE (N50 of ~6-8 kb) would be
ideal for maximising output as well as minimising pore blocking and wasted sequencing. Adding
a ~20 kb buffer, corresponding to ~N01 of the library, would minimise the difference between
average and minimum coverage, giving the ideal output.
10. Strand directionality
Strand directionality
Another factor to consider when designing your buffer regions is strand targeting with respect to
directionality. Side-specific buffering allows reads to be correctly accepted on either side of the
target depending on the strand of origin (see the IGV plot in Figure 10). Note that this is an
advanced feature and not necessary for the correct functioning of adaptive sampling. Use
discretion if you are adding the directionality function for buffering.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 26
Figure 10. IGV plot, coloured by strand direction, showing the effect of strand-specific targeting
using the 6th column of the .bed file. Red lines represent the cut-off at each strand, where the
sequence is not accepted anymore for sequencing, and they match the end of the ROI (no buffer)
in each direction.
Setting the buffer to be side-specific prevents the acquisition of reads which start downstream of
the ROI. This can be seen in Figure 11, where there are no reads starting after the red lines in
each direction. However, reads which start within the ROI can still extend beyond the end of the
ROI. Directionality can be specified by using the 6th column of a .bed file (Figure 11). More
information is available from the following links:
https://samtools.github.io/hts-specs/BEDv1.pdfhttps://en.wikipedia.org/wiki/BED_(file_format)
You can add a side-specific buffer to your ROIs, for example, only adding buffer upstream of the
target sequence. To do this, include two lines in the .bed file for the same target, one for each
strand direction, and add the buffer amount upstream of the targeted sequence. For example:
Chr1              “start-buffer”    “end”                      “name”      “score”       
+
Chr1              “start”                  “end + buffer”       “name”      “score”       
-
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 27
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 28
Figure 11. Example of a .bed file containing six columns. From left to right: chromosome; starting
coordinate; end coordinate; region name; score; direction of strand.
Including a side-specific buffer halves the amount of buffer sequence added, since you are only
adding the buffer to a single side of the target in each strand. In contrast, when you are not
defining a strand direction, you are adding buffer regions indiscriminately to both sides of the
targets.
11. Depletion mode
Adaptive sampling depletion mode
In contrast to running adaptive sampling in enrichment mode, in depletion mode you are
choosing which sequences to reject rather than accept. This requires a different approach to
enrichment mode. Firstly, the advised total targeted amount is the inverse of what you would use
for the enrichment strategy. The amount of sample you specify to be rejected needs to be large
enough that the pores have the maximum time available to sequence the regions of interest. You
can still reach a similar level of enrichment as with the enrichment strategy if your sequences of
interest comprise a small amount of your sample (1-5%). This means you would need to create a
.bed file which targets/rejects 95-99% of the sample.
The second consideration is that, when depleting unwanted regions from a single genome
sample, the buffer size needs to work as a negative value. Therefore, instead of adding buffer to
your target file (which defines the sequences to be depleted), you will need to subtract it. Below is
a schematic of the logic used to transform an enrichment strategy into a rejection strategy.
Figure 12. Schematic of how to convert an enrichment .bed file into a depletion .bed file.
The schematic in Figure 12 goes through all the steps from taking an enrichment buffered .bed
with known buffers and creating a buffered depletion .bed file. You can easily go from the first to
the last step in a situation where the buffer size remains the same. With such an approach, you
need to know the total size of a chromosome so that you can target for depletion the entire
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 29
region from the end of the ROI to the end of the chromosome. These values may vary depending
on the reference used. Figure 13 shows an example of how this would look like in a .bed file
targeting two regions of the human chromosome 1:
Figure 13. Example of a .bed file converted from an enrichment to a depletion strategy.
If you are trying to enrich for specific regions in your genomes by depleting the rest of the
sample, it is easier to set up an enrichment strategy instead. Depletion mode is best used when
you want to enrich for unknown sequences or genomes. This is most common in cases where the
sample contains a mixture of organisms, and you want to deplete everything already known to be
in the sample so that adaptive sampling can enrich for rare or unknown genomes present in the
sample.
12. Device specifications
Device specifications for adaptive sampling
Adaptive sampling requires a lot of computing power because of its need to basecall, align, and
make a decision on all the strands captured in real-time. We currently recommend turning off live
basecalling when running adaptive sampling on more than one flow cell. Running live basecalling
during an adaptive sampling run may lead to reduced enrichment (reduction in on-target
coverage obtained) due to the lack of resources to handle both basecallers.
For this reason we recommend that nothing else is running on the device. This includes offline
basecalling, basecalling from WGS runs or any other processes which may consume CPU/GPU
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 30
usage. Once adaptive sampling runs are started, you can check the performance of adaptive
sampling by using the “Read length distribution” panel in the MinKNOW UI.
As long as the “Adaptive sampling voltage reversal” value is below 1 kb, the runs should be
performing ideally to obtain enrichment of the selected targets. If the value is above 1 kb,
consider the following:
Check that there are no other flow cells running on the device that are
sequencing with basecalling, and that there are no flow cells running super
accurate (SUP) basecalling models.
Check there are no other background processes consuming resources
(analysis tools, etc.)
Reduce the number of flow cells being used for adaptive sampling.
Once the changes have been applied, restart the run. The accumulated data during the initial
slow period will average out the new data (after turning off features/flow cells) and may mask the
effect on the run for a considerable time. For this reason it is best, when identifying an issue, to
stop the run, perform the necessary check/modifications, and restart the runs, to quickly observe
the effect on adaptive sampling performance.
Figure 14. Read length histogram in MinKNOW, showing the estimated N50s.
Alignment and memory limit on the MinION Mk1C
Due to insufficient RAM, the MinION Mk1C cannot hold a fully indexed human reference in
memory, and going over the memory limit will crash the adaptive sampling process. Alignment
time is another metric to bear in mind when considering the maximum reference file size for the
MinION Mk1C. The larger the reference provided, the longer it takes the adaptive sampling
process to run through the indexed reference to find the alignment. For this reason, we advise
uploading no more than 125 Mb of non-indexed reference (FASTA). Above this size, the MinION
Mk1C will experience heavy delays in the adaptive sampling decision.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 31
Final notes
In devices with larger amounts of memory, you can align your sequences to larger reference files
if you are not using adaptive sampling (for example, by performing regular sequencing with live
alignment). Nevertheless, you can expect the speed of the live basecalling to decline if the
references size exceeds the suggested values.
Do not pre-index your reference files before uploading them to MinKNOW to use with adaptive
sampling. In the latest version of MinKNOW, the software automatically indexes the reference at
the beginning of the run, and the run cannot start until indexing is completed. This allows Oxford
Nanopore to keep the alignment parameters flexible and to optimise for the fastest and most
accurate alignment for adaptive sampling. If you pre-index your reference, you will most likely
not use the same indexing parameters that MinKNOW uses, and this can affect the adaptive
sampling decisions, leading to false positives and false negatives.
13. Where to find, create, and modify FASTA and .bed files
Where to find, create, and modify FASTA and .bed files
Adaptive sampling requires the following inputs:
A genomic reference (FASTA or .mmi file) containing the sequences present
in the sample. An .mmi file is also called an indexed reference, and you can
obtain this by indexing the reference file (FASTA) before starting the run
either through MinKNOW (start page) or by using minimap2. Nevertheless,
it is not advised that references are pre-indexed, as the parameters for
indexing are subject to change by Oxford Nanopore to maximise adaptive
sampling performance.
The coordinates for the regions of interest, provided in a .bed file.
Coordinates should be based on the reference provided, meaning that
chromosome names should match with chromosome names used in the
reference.
We recommend that the reference you provide represents the complete sample being used. For
example, if your sample contains three different organisms, then the reference should contain
the complete genome of all three organisms. This will reduce possible false positive alignments
that arise from using an incomplete reference.
You can download reference files from trustworthy databases such as the UCSC Table browser
and the NCBI RefSeq database. These files will represent the template to align the reads captured
during the sequencing run. If more than one organism is present in the sample, download
multiple references, one for each organism, and concatenate the files to create a single file with
all the references. Check the names of the individual chromosomes to make sure that there is no
duplication of chromosome names (e.g. avoid “Chr1” in cat.fasta and also “Chr1” in human.fasta).
Once you have downloaded the correct references, build the .bed file using the existing
annotations for your references. In this guide, we will use the USCS Table browser as an example
of how to obtain a .bed file to target regions of structural variation in the human genome, as
shown in Figure 15. First, pick the clade, genome and assembly corresponding to human, choose
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 32
a group. This group corresponds to the type of sequenced you are targeting (e.g. Genes and
Genes predictions, Regulation sequences, variation of repetition regions, etc.). This will modify
the options available in the track with all the different pieces of annotation work developed for
the chosen group. The table will give the available list of regions provided by each track from
various combinations. For the current example of Structural variation regions, it is possible to
obtain common SV regions for different sets of the human population (drop-down menu shown in
Figure 16). This will give a complete list of regions for the whole genome.
Figure 15. Example of settings to download a .bed file for common structural variation regions in
the human X chromosome.
Figure 16. List of tables from the dbVar Common SV Track.
You can further subset the list of genes in each of these tables if you want to target regions in a
single chromosome. You can do this in the following section of the Table Browser, “Define region
of interest”. You can choose the genome or provide an interval of coordinates, as shown in Figure
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 33
15. Click lookup to activate the selection. If targeting the whole genome, select the “genome”
option, and no sub-setting will be performed. You can select further complex options in the
“Optional: Subset, combine, compare with another track”, however these will not be explained in
this guide.
Lastly, in the final section “Retrieve and display data”, set the “output format” to BED – browser
extensible data and a file name given in the input box below. Set “file type returned” to plain
text, as MinKNOW does not accepted compressed files. Click get output to be redirected to a
new page.
In this page (Figure 17), ensure that “include custom track header” is not selected. Instead, in
“Create one BED record per:”, select Whole Gene to get the exact regions defined in the track.
You can also select other options if you are interested in upstream, downstream, or specific
strand sequences only. Click get BED to download a file with the name previously specified but
without an extension. Rename the file to “name_chosen”.bed and your .bed file is ready to be
used.
By following all the settings in this guide, you will download a file with 62 lines, all of which are
from chromosome 1 represented by “chr1” in the first column of every line. You can visualise this
by opening the .bed file with any text file editor.
Figure 17. The last page in Table Browser before downloading the final .bed file.
Subsetting a large FASTA file for use with the MinION Mk1C
The MinION Mk1C does not have sufficient memory for large references sizes (>125 Mb). This
means that if you are working with a large reference, you will need to subset the FASTA file. In the
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 34
case of subsetting a large FASTA where only the regions of interest are present, there is no need
for a .bed file, as the reference has already been subset.
Below are instructions for making a subset FASTA file. You will need samtools and bedtools
installed on your computer. This may require some previous knowledge of how to use Conda and
samtools/bedtools.
1. Open a Terminal window.
2. Install samtools and bedtools using the following commands:
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh bash
Miniconda3-latest-Linux-x86_64.sh -b -f -p source ~/miniconda3/bin/activate
conda create -name adasamp -c bioconda samtools bedtools conda activate adasamp
3. Navigate to the folder containing your FASTA and .bed files. If they are in
different folders, create a link to the location of the FASTA file. If you are
already in the folder containing the .bed file:
ln -s /long/path/to/my/reference/in/different/folder/myref.fasta myref.fasta
REF=myref.fasta
If you are already in the folder containing the FASTA file:
ln -s /long/path/to/my/bed/in/different/folder/mybed.bed mybed.bed
BED=mybed.bed
4. Edit the settings for your reference and your .bed with target regions:
BASES_TO_EXPAND_PER_SIDE = this is the size of the buffer you calculated for
each side. REF=your_reference.fasta
BED=your_bed_with_target_regions.bed (The
subsetted FASTA file will be called
your_reference-your_bed_with_target_regions.fasta )
5. These are the intermediate files that will be created:
CHROM_SIZES=${REF}.chrom.sizes
SLOPPED_BED=${BED%.*}_slop-${BASES_TO_EXPAND_PER_SIDE}.bed These will be saved
in the same location where the commands are being run, and will remain
until they are deleted. This is the final file which you will upload into
MinKNOW: SUBSETTED_FASTA=${REF%.}-${SLOPPED_BED%.}.fasta . This is also saved
in the same location where the commands are being run.
6. Index the reference and get chromosome sizes:
samtools faidx ${REF} cut -f1,2 ${REF}.fai > ${CHROM_SIZES}
7. Expand the .bed and extract the FASTA from the expanded .bed:
bedtools slop -l ${BASES_TO_EXPAND_PER_SIDE} -r ${BASES_TO_EXPAND_PER_SIDE} -i
${BED} -g ${CHROM_SIZES} > ${SLOPPED_BED} bedtools getfasta -fi ${REF} -bed
${BED} -fo ${SUBSETTED_FASTA} -name
These commands take the .bed file that contains the regions of interest and
add a number of bases on either side of the ROI. This is your buffer region
for the adaptive sampling selection.
8. Copy the subset FASTA file to your sequencing device.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 35
14. Adaptive sampling catalogue
Adaptive Sampling Catalogue
The Nanopore Community has a page where you can share .bed file the whole community. You
may also find other users' .bed files that are relevant to your work. To browse adaptive sampling
.bed files submitted by other Community members, or to submit your own, visit the Adaptive
Sampling Catalogue. Instructions are provided on the page for how to add a .bed file to the
catalogue.
10 AG Catalogue page
Figure 18. Adaptive Sampling Catalogue page on the Nanopore Community website.
15. Troubleshooting
How to diagnose performance issues
High variability between samples and runs
Before comparing the performance of two runs, take note if both experiments were run under
similar conditions. This includes the run settings (number of flow cells, basecalling models,
alignment), references and .bed files, sequencing kit and sample preparation protocols.
If you tick the option Split by read end reason below the read length histogram, you will see
above the graph the mean value for the adaptive sampling rejection peaks as “Adaptive sampling
voltage reversal”. This values can be used as a proxy of the adaptive sampling decision speed.
There may be some variation between runs and samples. However, a variation above 30% may
indicate an issue with the run. The most probable cause of the increase in length of distributions
of the rejection peak is a delay in the decision. This can be due to slow basecalling or slow
alignment. Check that the device is not running any other background processes that are
occupying compute resources. If in doubt, reboot the device. If after the reboot the adaptive
sampling is still showing a delay in decision time, make sure you are complying with the limits
established for the correct performance of each device. This can be revisited in the “Devices”
section of this guide.
If after all the checks the adaptive sampling performance is still low, check the metrics for
sequencing quality (Q-scores, sequencing speed and device temperature). Issues with sequencing
speed could cause an increase in decision time by taking longer to acquire the necessary amount
of data.
High percentage of failed reads
The cumulative output, which you can see in the MinKNOW graphs if you are running live
basecalling, provides information about the amount of failed reads. This value should typically be
below 10%. If this value is >20%, this suggests an issue with the sample, which may then affect
basecalling performance and prevent the software from making an adaptive sampling decision on
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 36
time. This issue usually also coincides with the presence of a bimodal rejection peak in the read
length histogram.
Bimodal rejection peak
A bimodal rejection peak is a clear indicator of poor adaptive sampling performance. Sometimes,
a small peak can appear after the main peak. This means that a small proportion of reads are
taking longer to get a decision made up. There a couple of reasons which could lead to this:
Low quality strands can prevent the a decision to be made quickly by
requiring more strand to be sequenced until we are confident with the
alignment.
An overloaded system which can be caused by running to many instances of
adaptive sampling and/or live basecalling with heavy models.
A smaller peak appearing after the first main peak is not usually a cause for concern. However,
when the height of the second peaks reaches ~50% of the first peak, or there is a long tail behind
the first peak (as shown in Figure 19), this indicates reduced adaptive sampling performance. The
most common cause is too many MinKNOW features or flow cells running simultaneously. To
resolve this, either reduce the number of flow cells or switch off live basecalling.
Figure 19. An example of a bimodal rejection peak from the Read Length Histogram plot in
MinKNOW for a single flow cell running adaptive sampling.
How to interpret output files
The files that MinKNOW outputs during a sequencing experiment are described in the Data
analysis technical document.
For adaptive sampling experiments, there are two additional CSV files named
AS_decisions_x_x_x.csv and AS_timmings_x_x_x.csv that are saved in other_reports in
the run folder, which you can use for troubleshooting. These files can be “matched” with the
sequencing summary by read_id to concatenate adaptive sampling information and
sequencing summary information. This allows you to see the metrics of each read along side the
decision performed by adaptive sampling.
The AS_decisions_x_x_x.csv file containing three columns - read_id , action
, and action_response
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 37
The AS_timmings_x_x_x.csv containing nine columns - channel , read_id ,
batch_time , samples , bases , barcode_arrangement , mean_qscore ,
time_to_package_and_send , and time_in_basecaller
Field
Description
read_id
An individual ID for each read, matching the read_ids provided by
the sequencing summary
action
Whether a read was accepted (sequence) or rejected (unblock)
action_response
Whether an action was successfully executed by MinKNOW (
SUCCESS / FAILED_READ_FINISHED / FAILED_READ_TOO_LONG )
channel
The channel in which the read was sequenced
batch_time
Batch time of when the read was processed by the Adaptive
Sampling script
samples
Number of samples received by the Adaptive Sampling script for
each read
bases
Number of bases basecalled from each read for the Adaptive
Sampling decision
barcode_arrangement
Barcode arrangement detected on first chunk (this will be empty
if not using a barcoding kit)
mean_qscore
Mean Q-score of the Adaptive Sampling first chunk basecalling
time_to_package_and_send
Time between the Adaptive Sampling script getting a read and
sending it to the basecaller
time_in_basecaller
Time between sending a read to the basecaller and getting it
back from the basecaller
How to verify that you are targeting the correct regions
Using the metrics available in the adaptive_sampling.csv in the “other reports” folder and the
sequencing_summary.txt , you can get an idea of the adaptive sampling performance and to
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 38
check whether you are targeting all the regions you intended with your .bed file.
If you know the size of all your regions of interest, you can sum these together to calculate your
total sequence target. Divide this value by the size of the genomes present in the sample (if you
have multiple genomes in the sample, take into account the prevalence of each genome) to
estimate the % of reads that should be getting the decision stop_receiving . There will always
be a variation of 10-20% depending on the prevalence of the regions targeted, efficiency of
ligation for different genome regions, q-score of particular regions of the genome, etc. However,
you can use this calculation as a first approximation for whether you are accepting the right
number of reads.
This check is worth doing if by looking at the read length histogram, you believe that the number
of reads being accepted is too high or too low based on the amount of the sample you believe
you are targeting.
If you are getting fewer stop_receiving reads than expected, the possible causes are:
Your buffer regions are too small
Incorrectly set lines in the .bed file. Incorrect lines are ignored by adaptive
sampling
Sequences are not correctly targeted from the reference
Sequences are not present in the sample
There are hard to sequence regions (e.g. repetitive regions) where the
aligner cannot decide on the position of the read. This is a very rare case.
Low q-scores for the reads
If you are getting more stop_receiving reads than expected, the possible causes are:
Your buffer regions are too large
You have used an incomplete FASTA reference that does not represent the
whole sample
You provided an invalid .bed file. In this case, the system defaults to
targeting the complete FASTA reference provided
There is an error in the .bed file coordinates of a particular region
16. MinKNOW UI and dialogs
During an adaptive sampling experiment, MinKNOW carries out basecalling and
alignment with adaptive sampling in parallel with live basecalling. The
MinKNOW user interface shows dialogs with information for both processes.
Here, we explain where you can find each type of information.
Firstly, there are separate sections in MinKNOW for uploading a live sequencing alignment
reference and .bed file, and an adaptive sampling alignment reference and .bed file. Both the
reference FASTA file and the .bed file can be the same in both sections (hence the Alignment
section is pre-populated with the files uploaded in the Adaptive Sampling section). Nevertheless,
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 39
it is important to understand the function of each file as you can get a better ongoing view of
coverage obtained throughout the run, by loading a different .bed file in the live alignment
section.
The adaptive sampling files are loaded in the 3. Run Options section under the section named
“Adaptive Sampling” - Figure 20, top section. These will be used for targeting your sample and will
affect the reads which get selected by MinKNOW for sequencing. The .bed file loaded in this
section should also contain a buffer region, when applicable. For more information on this, refer
to previous guide sections about buffers.
The live alignment files are loaded in the 4. Analysis section of the run setup in MinKNOW. The
purpose of the FASTA reference is to align the reads after live basecalling and therefore should be
the same file as the one loaded for the adaptive sampling decision. This will allow to output BAM
files containing the basecalled and aligned sequence in real time.
The .bed file in the 4. Analysis section is used for two different processes: Firstly, it provides an
identifier in the sequencing summary reporting whether the complete read hit the regions
described in the .bed file loaded in 4. Analysis. This is shown in the sequencing_summary.txt file
under the column bed_alignment and populated with a 0 or a 1, for whether it hits or does not hit
the .bed file. Secondly, this .bed file is used to check for the coverage obtained at each of the
regions described in the same .bed file. You can follow this live during the run in the Alignment
hits tab of MinKNOW.
To make the most of the live alignment feature and the coverage tracking feature, load the
buffered .bed file (bed file containing the ROI + buffer) in the 3. Run options Adaptive sampling
section, and the .bed file containing only ROI (unbuffered) in the 4. Analysis section. This
guarantees that you only track coverage on the targets of interest, and will give a more accurate
description of coverage on the ROIs. The .bed file provided in the alignment section does not
modify the run output and is not strictly necessary. Nevertheless, depending on the amount of
buffer added to each region in the adaptive sampling .bed, having a targets only (unbuffered)
.bed in the alignment section may provide a more accurate coverage report. Importantly, the
coverage tracking (and therefore the files provided in 4. Analysis) does not modify the
sequencing run in any way. It is a tool for real-time alignment and for checking during a run how
much coverage has already been obtained for each bed region. Lastly, note that the coverage
reported is referring to the percentage of sequence that has been basecalled. This means that if
the live basecalling is not keeping up, the coverage reported is only relative to the percentage
already basecalled.
Live alignment is a computationally demanding process which can easily affect the adaptive
sampling decision time. Therefore, please refer the tables of advised metrics on how many flow
cells you can run with this feature per device to avoid affecting enrichment rates. To prevent live
alignment being used, remove the reference sequence denoted “1” in Figure 20.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 40
Figure 20. MinKNOW dialogs for uploading the FASTA reference file and .bed file for the adaptive
sampling panel (top, sections 3 and 4) and the live basecalling panel (bottom, sections 1 and 2).
You can see which files are being used in each section in the first page of the run summary once
the run is started. An example of this panel is shown in Figure 21.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 41
Figure 21. MinKNOW front panel containing run summary details. Alignment information has
been labelled accordingly.
OXFORD NANOPORE TECHNOLOGIES | Adaptive sampling | Oxford Nanopore Technologies
PAGE 42

