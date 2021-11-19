# global variables
base_qsc = []  # base quality scores, perhaps it is better to use pandas dataframe
read_qsc = []  # read quality scores, perhaps it is better to use pandas
gc_content = []  # read GC composition
seq_set = set()  # set for overrepresented and duplicated sequences (for check)
over_seq = {}  # dict for non-unique sequences


def quality_per_read(quality, n):
    sum_quality = sum([ord(i) - 33 for i in quality])
    read_qsc.append(sum_quality/n)


def quality_per_base(quality, n):
    """ make a list of lists = base_qs[position][list of scores] """
    for i in range(n):
        try:
            base_qsc[i] += [ord(quality[i]) - 33]
        except IndexError:
            base_qsc.append([ord(quality[i]) - 33])


def gc_counter(sequence, n):
    gc_content.append(((sequence.count('G')+sequence.count('C'))/n)*100)


def duplicate_counter(sequence, n, counter):
    """
    Add sequence (or its part if length > 75) in the dict if it non-unique
    (i.e. has match with first 100k sequences)
    """
    if n > 75:
        seq = sequence[:50]
    else:
        seq = sequence

    if seq in seq_set:
        if over_seq[seq]:
            over_seq[seq] += 1
        else:
            over_seq[seq] = 2

    if counter <= 100000:
        if seq not in seq_set:
            seq_set.add(seq)


def quality_per_score():
    pass
