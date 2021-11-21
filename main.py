import plots
import stats
# import amateur_reporter
from Bio.SeqIO.QualityIO import FastqGeneralIterator  # will need to go to requirements
import argparse
import os
import numpy as np
out_dir = '.'
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
            stats.quality_per_read(qual, n)
            stats.length_of_reads(n)

            # put other functions from stat.py here
            # they need to work with single read
            # vars: title (use for 'per tile quality'), seq (nucleotides), qual (phred33 quality)
            # n - length for certain read, "counter" count overall numbers of reads


def dir_maker(out):
    if '\\' in out:
        path = out.split('\\')
        os.makedirs(os.path.join(*path, 'QCTerror_res', 'reports'), exist_ok=True)
        os.makedirs(os.path.join(*path, 'QCTerror_res', 'pictures'), exist_ok=True)
        os.makedirs(os.path.join(*path, 'QCTerror_res', 'tables'), exist_ok=True)
    else:
        path = out.split('/')
        os.makedirs(os.path.join(*path, 'QCTerror_res', 'reports'), exist_ok=True)
        os.makedirs(os.path.join(*path, 'QCTerror_res', 'pictures'), exist_ok=True)
        os.makedirs(os.path.join(*path, 'QCTerror_res', 'tables'), exist_ok=True)
    return path + ['QCTerror_res']


def amateur_reporter(out, file):
    """
    each plot need to be save in 'out' directory, so, it must be in all plots.funs
    """
    out = dir_maker(out)
    plots.per_base_sequence_quality(out)
    plots.per_sequence_gc_content(out)
    plots.overrepresented_table(counter, out)
    plots.dup_plot_maker(counter, out)
    plots.per_base_sequence_content(out)
    plots.per_sequence_quality_score_print(out)
    plots.reads_length_distribution(out)
    plots.basic_statistics(file, counter, out)
    exec(open("./amateur_reporter.py").read(), {'out': out})
    # add other functions from plots.py here (which create plots, tables for pdf, etc)


def start_parsing():
    parser = argparse.ArgumentParser(description='Read one fastq file and save some statistics about.')
    parser.add_argument('--input', '-i', help='Input fastq file (in the current dir or path to its).')
    parser.add_argument('--output', '-o', default='.', help='Choose existing output directory (default=".").')
    return parser.parse_args()


def per_title_sequence_quality_data(fastq_file, out):   # data preparation
    x = open(fastq_file, 'r')  # read file
    all_fastq = x.readlines()
    x.close
    max_len = len(max(all_fastq, key=len))
    num_str = sum(1 for _ in all_fastq)
    num_reads = int(num_str / 4)
    ord_arr = np.zeros((num_reads, max_len))
    for i in range(1, num_str + 1, 4):  # for every quality string
        quality = all_fastq[i + 2]
        len_quality = len(quality)
        nread = int((i+3)/4)
        for j in range(len_quality):  # quality count
            ord_arr[nread-1][j] = ord(quality[j]) - 33
    plots.per_tile_sequence_quality_plot(ord_arr, out)


if __name__ == '__main__':
    args = start_parsing()
    fastq_file = args.input  # path to input file
    out_dir = args.output  # string means path to output directory
    reader(fastq_file)  # now it works with single file only from the same directory
    amateur_reporter(out_dir, fastq_file)
    # per_title_sequence_quality_data(fastq_file, out_dir)
