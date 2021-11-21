import pygtrie

# global variables
base_qsc = []  # base quality scores, perhaps it is better to use pandas dataframe
read_qsc = []  # read quality scores, perhaps it is better to use pandas
gc_content = []  # read GC composition
seq_set = pygtrie.Trie()  # Trie structure for overrepresented and duplicated sequences (for check)
over_seq = {}  # dict for non-unique sequences
unique_Overrepr_counter = 0
base_pos = {}  # {position1(int): {'A':,'C':,'G':,'T':}, ...}
read_length = []


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


def duplicate_counter(sequence, n):
    """
    Add sequence (or its part if length > 75) in the dict if it non-unique,
    i.e. has match with first 100k _unique_ sequences
    NB: the subsequence search is too long in-built set(), so I use Trie dict-like container
    """
    global unique_Overrepr_counter
    if n > 75:
        seq = sequence[0:50]
    else:
        seq = sequence

    if seq_set.has_subtrie(seq):
        if seq in over_seq:
            over_seq[seq] += 1
        else:
            over_seq[seq] = 2
    elif unique_Overrepr_counter <= 100000:
        seq_set[sequence] = 1
        unique_Overrepr_counter += 1


def quality_per_score():
    pass


def base_content(seq, n):
    for i in range(n):
        if i in base_pos:
            if seq[i] in 'AGCT':  # there can be other letters in seq (I see 'N' for example)
                base_pos[i][seq[i]] += 1
        else:
            base_pos[i] = {'A': 0, 'G': 0, 'C': 0, 'T': 0}  # create new dict for position


def length_of_reads(n):
    read_length.append(n)
