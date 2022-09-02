+++
date = "2022-09-09T00:00:00"
title = "Accurate short variant calling from sequencing data with pangenomes and DeepVariant"
abstract = "Accurate identification of genomic variants is critical for genetic studies and, more and more, for clinical genetic testing. With genome sequencing technology, the whole-genome can be assessed and a comprehensive spectrum of genomic variants could in theory be called. Some genomics regions and variants are in practice still challenging to detect with the standard techniques, which is to first align the sequenced reads to a reference genome. A new approach has recently shown better results by a reference pangenome instead, i.e. a reference representing multiple genomes and incorporating information about known variants a priori. At the forefront of human pangenomics, the Human Pangenome Reference Consortium (HPRC) aims at producing high-quality phased de novo assemblies for more than 300 diverse individuals, and build a comprehensive and representative human pangenome. With its draft representing 45 individuals, we show that using the HPRC pangenome improves the mapping of short reads and, as a result, the identification of short variants in an individual. Our approach maps the short Illumina reads to the pangenome using vg Giraffe and calls short variants with DeepVariant using new models trained on the pangenome. We compared our approach to the standard technique of mapping reads to the linear reference genome with BWA-MEM, or the more recent Dragen pipeline. Using both the Genome in a Bottle and the Challenging Medically-Relevant Genes truthsets, we observed a better performance for our pangenomic approach. It makes about 34% less errors and is capable of calling short variants in a larger fraction of the genome, including in more challenging regions. As expected, the calling accuracy increases when trio sequencing data is available and is still superior when mapping the short-reads to the HPRC pangenome rather than to the linear reference genome or using the DragenGRAPH mapper. In addition to quantifying the benefit of this pangenomic approach, we share the resources and workflows to accurately call small variants from sequencing data using the HPRC draft pangenome."
abstract_short = ""
event = "AGBT Precision Health"
event_url = "https://www.agbt.org/events/precision-health/"
location = "San Diego, CA, USA"
selected = false
math = true
url_pdf = "slides/AGBTph2022-poster-HPRC-GiraffeDV.pdf"
url_slides = ""
url_video = ""
# Optional featured image (relative to `static/img/` folder).
[header]
# image = "headers/sandiego.jpg"
# caption = "My caption :smile:"
+++

Resources for the poster:

- [Human Pangenome Reference Consortium (HPRC)](https://humanpangenome.org/)
- *A Draft Human Pangenome Reference*. bioRxiv 2022 [DOI:10.1101/2022.07.09.499321](https://doi.org/10.1101/2022.07.09.499321)
- HPRC pangenomes resources index: https://github.com/human-pangenomics/hpp_pangenome_resources
- Variation graph toolkit (vg): https://github.com/vgteam/vg
- DeepVariant: https://github.com/google/deepvariant
- Workflows (WDL): 
    - WDLs are maintained on [GitHub](https://github.com/vgteam/vg_wdl) and deposited on [Dockstore](https://dockstore.org/workflows/github.com/vgteam/vg_wdl/GiraffeDeepVariantLite:giraffe-dv-dt-hprcy1?tab=info).
    - The versions used in the bioRxiv preprint is [DOI:10.5281/zenodo.6655968](https://doi.org/10.5281/zenodo.6655968)

