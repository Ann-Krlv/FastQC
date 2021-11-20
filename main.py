import plots
import stats
from Bio.SeqIO.QualityIO import FastqGeneralIterator  # will need to go to requirements

counter = 0  # number of reads


def reader(fastq):
    global counter
    with open(fastq) as in_handle:
        for title, seq, qual in FastqGeneralIterator(in_handle):
            n = len(seq)
            counter += 1
            stats.quality_per_base(qual, n)
            stats.gc_counter(seq, n)
            stats.duplicate_counter(seq, n)
            stats.base_content(seq, n)
            # put other functions from stat.py here
            # they need to work with single read
            # vars: title (use for 'per tile quality'), seq (nucleotides), qual (phred33 quality)
            # n - length for certain read, "counter" count overall numbers of reads


def report_maker():
    plots.per_base_sequence_quality()
    plots.per_sequence_GC_content()
    plots.overrepresented_table(counter)
    plots.per_base_sequence_content()
    #plots.duplicated_reads()
    # add other functions from plots.py here (which create plots, tables for pdf, etc)


if __name__ == '__main__':
    fastq_file = input('Please, input file, \'short.fastq\' for example: ')
    reader(fastq_file)  # now it works with single file only from the same directory
    report_maker()
    print('There are', counter, 'reads in the file')
    print(stats.unique_Overrepr_counter)
