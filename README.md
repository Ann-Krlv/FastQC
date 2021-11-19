# The FastQC program analogue
This is our team work. We created an analogue of FastQC program. It will work correctly.

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
