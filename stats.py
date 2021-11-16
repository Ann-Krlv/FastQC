# global variables
base_qsc = []  # base quality scores, perhaps it is better to use pandas dataframe
read_qsc = []  # read quality scores, perhaps it is better to use pandas


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


def gc_counter():
    pass


def quality_per_score():
    pass
