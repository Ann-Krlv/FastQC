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

## Example
You can do a test run on the data presented as a *example.fastq*.  The data was taken from  
https://figshare.com/articles/dataset/amp_res_2_fastq_zip/10006541. This data was additionally corrected: it consist out of first 60 reads, some of them are also shorterned for purposes to see difference in the plot regarding reads_length.

## Installation
* clone this repository into you local
* it is better to use virtual environment (conda or virtualenv)
* before first start run `pip install -r requirements.txt` in the terminal (in your virtual environment better)
* then you can start

* *the correct work had been cheched for Ubuntu 20.4 and Windows 10, but if you can choise, Ubuntu is better*
* *the script works correct with python 3.8*

## Usage
* To run program type python main.py -i file.fastq (or use your python3 interpreter) in project directory
* If you want, you can specify output directory: python main.py -i file.fastq -o path/to/dir
* Program will count the number of reads, create folder QCTerror_res and exit
* All pictures and tables into QCTerror_res/pictures/ and QCTerror_res/tables/ folders
* The pdf report generation takes some time, so you can take a coffee break or just comment (#) last 
string in amateur_maker() (in main.py)
* Enjoy :)

## Authors and acknowledgements:
* Anna Koroleva,https://github.com/Ann-Krlv    
  * Contributed to quality_per_base, gc_counter, duplicate_counter,per_sequence_quality_score_print, testing - __IDEA DEVELOPER__
* Valeria Ladygina, https://github.com/ValeriiaLadyhina
  * Responsible for README.md, created Logo, contributed to quality_per_base ,gc_counter, base_content, read length, flake 8 - __PLOT BEAUTIMAKER__
* Leonid Zhozhikov, https://github.com/LyonyaZhozhikov
  * responsible for the part of the tool that creates report - __GOD of REPORTS__
* Oxana Kolpakova, https://github.com/OxanaKolpakova 
  * Contributed to per_sequence_quality_score_print, requirements, last fixes for flake 8, testing - __SUPER TESTER__

## Feedback
 If you have any questions, bug reports or complains please approach the authors of FastQ Filtrator via email:

 *__valeriia.ladyhina@gmail.com__* - responsible for communication with clients
 
