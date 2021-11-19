# QC-TError - FastQC program analogue
> Python tools for basic statistics on quality of raw Illumina reads

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
You can do a test run on the data presented as a *example.fastq*.  The data was taken from from 
https://figshare.com/articles/dataset/amp_res_2_fastq_zip/10006541

To see example of output you can type:
![FastQC] (https://raw.githubusercontent.com/QCTerror/FastQC/main/.ipynb_checkpoints/Per_base_quality.png)


You can see the example of  created report *example.report* via

## Сontribution of each project participant:

* Anna Koroleva,https://github.com/Ann-Krlv (...)
*  Valeria Ladygina, https://github.com/ValeriiaLadyhina (...)
*  Leonid Zhozhikov, (...)
*  Oxana Kolpakova, https://github.com/OxanaKolpakova (...)

## Brief description of the project:
1. recognition fastQ format, read file
2. transforme the quality symbols into numbers by position according to the ASCII table
3. make graphs and tables according to ASCII quality data
4. basic statistics (length, GC, duplicates, overrepresented ....)
5. parsing command line arguments
6. instruction
7. requrements.txt with required dependencies, OS and python versions on which the program was tested
8. Markdown project report
9. create a common repository
10. checkout for PEP8 in github actions

Data were taken from https://figshare.com/articles/dataset/amp_res_2_fastq_zip/10006541

### Usage
0. General notes: now you can get the number of reads and ugly plot only
1. To run program type `python main.py` (or use your python3 interpreter) in project directory
2. When program ask you, print fastq file name (or path, but probably it doesn't work :))
3. Program will count the number of reads, create Per_base_quality.png file with plot and exit
4. Enjoy :)
