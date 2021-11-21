![QC-Terror](https://user-images.githubusercontent.com/71066938/142631946-18e9e670-1395-4050-8cf7-1acedd1b8687.png)
# *QC-TError* - FastQC program analogue
> Python tool for basic statistics on quality of raw Illumina reads

## Introduction
*__QC-TError__* is a tool that you can use to get basic statistics on your raw Illumina reads. With help of it you can obtain
information regarding:
* basic statistics
  * length of reads presented in the data
  * total number of reads
  * average content of GC in sequence
  * number of reads that have poor quality
* visualtisation of:
  * average per base quality of reads
  * sequence quality per tile
  * distribution of average read quality score
  * per base sequence content
  * per sequence GC content
 
## Start
To start working with QC-Terror tools please download our package to your computer. To run QC-TError tool please type 
`python main.py` (or use your python3 interpreter) in project directory. 

## Example
You can do a test run on the data presented as a *example.fastq*.  The data was taken from  
https://figshare.com/articles/dataset/amp_res_2_fastq_zip/10006541. This data was additionally corrected: it consist out of first 60 reads, some of them are also shorterned for purposes to see difference in the plot regarding reads_length.

### Usage


## Authors and acknowledgements:
* Anna Koroleva,https://github.com/Ann-Krlv    
  * Main Idea developer, contributed to quality_per_base, gc_counter, duplicate_counter,per_sequence_quality_score_print 
* Valeria Ladygina, https://github.com/ValeriiaLadyhina
  * Responsible for README.md, created Logo, contributed to quality_per_base ,gc_counter, base_content, read length
* Leonid Zhozhikov, https://github.com/LyonyaZhozhikov
  * responsible for the part of the tool that creates report
* Oxana Kolpakova, https://github.com/OxanaKolpakova 
  * Contributed to per_sequence_quality_score_print, requirements

## Feedback
 If you have any questions, bug reports or complains please approach the authors of FastQ Filtrator via email:

 *__valeriia.ladyhina@gmail.com__* - responsible for communication with clients
 
