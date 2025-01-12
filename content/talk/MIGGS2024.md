+++
date = "2024-09-23T00:00:00"
title = "Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit"
abstract = ""
abstract_short = ""
event = " Methods for Interfacing with Graphs of Genomic Sequences Symposium"
event_url = "https://miggs.mathnum.inrae.fr/evenements"
location = "Lille, France"

selected = false
math = true

url_pdf = ""
url_slides = "https://jmonlong.github.io/manu-vggafannot/vggafannot-miggs24.html"
url_video = ""

# Optional featured image (relative to `static/img/` folder).
[header]
image = "headers/lille.jpg"
# caption = "My caption :smile:"

+++

The preprint associated with this presentation came out a bit later: [Novak et al. bioRxiv 2024](https://doi.org/10.1101/2024.10.12.618009).

## Abstract


**Jean Monlong**$^{1}$, Adam M. Novak$^2$, Dickson Chung$^2$, Glenn Hickey$^2$, Toshiyuki T. Yokoyama$^3$, Erik Garrison$^4$, Benedict Paten$^2$

1. Institut de Recherche en Santé Digestive, INSERM, Toulouse, France
1. UC Santa Cruz Genomics Institute, Santa Cruz, CA, USA
3. Department of Computational Biology and Medical Sciences, University of Tokyo, Chiba, Japan.
4. University of Tennessee Health Science Center, Memphis, TN, USA


The current reference genome is the backbone of diverse and rich annotations. 
To enable similar enrichment of a pangenome reference, there is a dire need for tools and formats for pangenomic annotation. 
Simple text formats, like VCF or BED, have been widely adopted and helped this critical exchange of genomic information. 
The Graph Alignment Format (GAF) text format, which was proposed to represent alignments, could be used to represent any type of annotation in a pangenome graph.
Here I review how some features of the `vg` ecosystem can already provide indexing, querying, and visualization capabilities for annotations represented as paths.

I will first explain how GAF files can be sorted, indexed and queried to extract annotations overlapping a subgraph.
<!-- First, to address the need for fast querying of the annotations, we updated the vg toolkit to be able to sort GAF files, index them, and query them to extract alignments covering a subgraph or region on a path.  -->
Alignments are currently sorted based on the covered node IDs, similar to the approach for sorting read alignments in the GAM format, a binary format used previously by the `vg` toolkit. 
To index the bgzipped GAF file, we extended HTSlib/tabix to work with the GAF format. 
Second, `vg annotate` was recently updated to better produce graph annotations as paths, starting from annotation files relative to linear references. 
More precisely, it can to take annotations in BED or GFF3 files, written relative to reference paths or haplotypes, and produce GAF files representing the equivalent paths through the pangenome.

To showcase these commands, I projected annotations for all haplotypes in the latest draft human pangenome (HPRC v1.1 GRCh38-based Minigraph-Cactus pangenome). 
This included genes, segmental duplications, tandem repeats and repeats annotations. 
`vg annotate` can annotate ~4M gene annotations in ~16 mins, and ~5.5M repeats from RepeatMasker in ~9 mins on a single-threaded machine. 
Finally, these rich annotations can then be quickly queried with `vg` and visualized using existing tools like the sequenceTubeMap or Bandage.

After this overview of the current "`vg`" options, it is clear that more needs to be done to make it a useful solution for the community.
For example, we are assuming that we have annotations of the different haplotypes in the pangenome.
There is still no clear solution to lift annotations from one reference/haplotype to other haplotypes, except through reanalysis/reannotation of each haplotype.
Another limitation is that the annotation information is currently reduced to a single label. 
For many annotations, it would be useful to keep the metadata organized, so that the user can access/use it within visualization tools.
Overall, we are also in need for visualization tools that can efficiently layout and organize many *paths* through a pangenome.
