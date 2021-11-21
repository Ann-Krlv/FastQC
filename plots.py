import seaborn as sns
import matplotlib.pyplot as plt
import stats
import pandas as pd
import numpy as np
import os
import statistics as st

pd.options.mode.chained_assignment = None  # default='warn'
min_len = 0
max_len = 0
mean_gc = 0


def basic_statistics(file, n, out):
    base_df = pd.DataFrame({'Measure': ['Filename', 'Encoding',
                                        'Total sequences',
                                        'Sequence length', '%GC'],
                            'Value': [file.split('/')[-1], 'Now it work as Sanger/Illumina 1.9 only',
                                      str(n),
                                      '{} - {}'.format(min_len, max_len), str(round(mean_gc, 2))]})
    base_df.to_csv(os.path.join(*out, 'tables', 'basic_statistics.tsv'), sep='\t')


def per_base_sequence_quality(out):
    fig = plt.figure(1, figsize=(30, 15), dpi=200)
    ax = fig.add_subplot(111)
    xticks = []
    xlabels = []
    count = 3
    for i in range(0, len(stats.base_qsc) - 1):
        if i + 1 <= 9:
            xticks.append(i)
            xlabels.append(str(i + 1))
        else:
            if count == 3:
                xticks.append(i + 1.5)
                if len(stats.base_qsc) - i < 4:
                    xlabels.append(str(i + 1) + ' - ' + str(len(stats.base_qsc)))
                else:
                    xlabels.append(str(i + 1) + ' - ' + str(i + 4))
                count -= 1
            elif 0 < count < 3:
                count -= 1
            elif count == 0:
                count = 3
    sns.boxplot(data=stats.base_qsc,
                saturation=0.75,
                showfliers=False,
                medianprops=dict(color="red", alpha=1),
                boxprops=dict(facecolor='gold', edgecolor='black', alpha=1),
                linewidth=0.7,
                whis=(10, 90))

    mean_var = [sum(i) / len(i) for i in stats.base_qsc]  # list with mean quality per position
    sns.lineplot(data=mean_var, legend=False, linewidth=0.5, alpha=1)  # add mean line plot

    plt.fill_between([0, len(stats.base_qsc)], [20, 20], color="lightcoral", alpha=0.2)
    plt.fill_between([0, len(stats.base_qsc)], [20, 20], [28, 28], color="yellow", alpha=0.2)
    plt.fill_between([0, len(stats.base_qsc)], [28, 28], [40, 40], color="lightgreen", alpha=0.2)

    for i in range(0, len(stats.base_qsc) - 1, 2):
        plt.fill_between([i+0.5, i + 1.5], [20, 20], color="lightcoral", alpha=0.1)
        plt.fill_between([i+0.5, i + 1.5], [20, 20], [28, 28], color="yellow", alpha=0.1)
        plt.fill_between([i+0.5, i + 1.5], [28, 28], [40, 40], color="lightgreen", alpha=0.1)

    ax.set_ylim(0, 40)
    ax.set_xlim(-0.5, xticks[-1])
    plt.xticks(xticks, xlabels, fontsize=17)
    plt.yticks(fontsize=17)
    plt.xlabel('Position in read (bp)', fontsize=20)
    # make title in the report 'Per base sequence quality'
    plt.title('Quality scores across all bases (Sanger / Illumina 1.9 encoding)', size=12)
    fig.savefig(os.path.join(*out, 'pictures', 'Per_base_quality.png'))
    plt.close()


def per_sequence_gc_content(out):
    global mean_gc
    cnt = len(stats.gc_content)
    mean_gc = sum(stats.gc_content)/cnt
    sd_gc = st.stdev(stats.gc_content)
    x = np.random.normal(mean_gc, sd_gc, cnt)
    plt.figure()
    sns.kdeplot(stats.gc_content, bw=0.3, color='red')
    sns.kdeplot(x, bw=0.5, color='blue')
    plt.xlabel('Mean GC content (%)')
    plt.legend(('GC count per read', 'Theoretical distribution'), loc='upper right')
    plt.suptitle('Per sequence GC content', fontweight='bold', color='darkred', horizontalalignment='right')
    plt.title('GC distribution over all sequences', size=4)

    plt.savefig(os.path.join(*out, 'pictures', 'GC_content.png'))
    plt.close()


def dicts_for_duplicated_reads():
    dup_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '>10': 0,
                '>50': 0, '>100': 0, '>500': 0, '>1k': 0, '>5k': 0, '>10k': 0}
    dedup_dict = dup_dict.copy()
    tmp_df = pd.DataFrame({'Sequence': stats.over_seq.keys(),
                           'count': stats.over_seq.values()})
    dup_ser = tmp_df['count'].value_counts().to_frame()
    dup_ser.reset_index(level=0, inplace=True)
    for i in range(len(dup_ser)):
        cur_bin = dup_ser.iat[i, 0]
        cur_count = dup_ser.iat[i, 1]
        if cur_bin-1 < 10:
            dup_dict[str(cur_bin-1)] += (cur_bin - 1) * cur_count
            dedup_dict[str(cur_bin-1)] += cur_count
        elif 10 <= cur_bin-1 < 50:
            dup_dict['>10'] += (cur_bin - 1) * cur_count
            dedup_dict['>10'] += cur_count
        elif 50 <= cur_bin-1 < 100:
            dup_dict['>50'] += (cur_bin - 1) * cur_count
            dedup_dict['>50'] += cur_count
        elif 100 <= cur_bin-1 < 500:
            dup_dict['>100'] += (cur_bin - 1) * cur_count
            dedup_dict['>100'] += cur_count
        elif 500 <= cur_bin-1 < 1000:
            dup_dict['>500'] += (cur_bin - 1) * cur_count
            dedup_dict['>500'] += cur_count
        elif 1000 <= cur_bin-1 < 5000:
            dup_dict['>1k'] += (cur_bin - 1) * cur_count
            dedup_dict['>1k'] += cur_count
        elif 5000 <= cur_bin-1 < 10000:
            dup_dict['>5k'] += (cur_bin - 1) * cur_count
            dedup_dict['>5k'] += cur_count
        elif 1000 <= cur_bin-1:
            dup_dict['>10k'] += (cur_bin - 1) * cur_count
            dedup_dict['>10k'] += cur_count
    return dup_dict, dedup_dict


def dup_plot_maker(counter, out):
    dup_dict, dedup_dict = dicts_for_duplicated_reads()
    dup_sum = sum(dup_dict.values())
    dedup_sum = sum(dedup_dict.values())
    if dup_sum and dedup_sum:
        fig, ax = plt.subplots()
        ax.plot(dup_dict.keys(), [i*100 / dup_sum for i in dup_dict.values()], color='blue')
        ax.plot(dup_dict.keys(), [i*100 / dedup_sum for i in dedup_dict.values()], color='red')
    else:
        fig, ax = plt.subplots()
        ax.plot(dup_dict.keys(), [0 for _ in range(len(dup_dict.keys()))], color='blue')
        ax.plot(dup_dict.keys(), [0 for _ in range(len(dup_dict.keys()))], color='red')
    ax.set_ylim(0, 100)
    for i in range(0, len(dup_dict.keys()) - 1, 2):
        plt.fill_between([i, i + 1], [100, 100], color="lightgrey")
    plt.legend(('% Total sequences', '% Deduplicated sequences'), loc='upper right')
    percentage = round((1 - dup_sum/counter)*100, 2)
    plt.title('Percent of seqs remaining if deduplicated {}%'.format(percentage))
    fig.savefig(os.path.join(*out, 'pictures', 'duplication_level.png'), figsize=(30, 10), dpi=200)
    plt.close()


def overrepresented_table(cnt, out):
    over_df = pd.DataFrame({'Sequence': stats.over_seq.keys(),
                            'Count': stats.over_seq.values(),
                            'Percentage': [i*100/cnt for i in stats.over_seq.values()]})
    res_df = over_df.loc[over_df['Percentage'] > 0.0999999999]
    res_df.sort_values('Count', ascending=False, inplace=True, ignore_index=True)
    res_df.set_index('Sequence', inplace=True)
    res_df.to_csv(os.path.join(*out, 'tables', 'overrepresented_sequences.tsv'), sep='\t')


def per_base_sequence_content(out):
    maximum = 100
    plt.figure()
    plt.plot([i['A']*100/sum(i.values()) for i in stats.base_pos.values()], color='limegreen')
    plt.plot([i['C']*100/sum(i.values()) for i in stats.base_pos.values()], color='blue')
    plt.plot([i['G']*100/sum(i.values()) for i in stats.base_pos.values()], color='black')
    plt.plot([i['T']*100/sum(i.values()) for i in stats.base_pos.values()], color='red')
    for i in range(0, len(stats.base_pos.keys()) - 1, 2):
        plt.fill_between([i, i + 1], [maximum, maximum], color="lightgrey")
    xticks = []
    xlabels = []
    count = 4
    for i in range(0, len(stats.base_pos.keys()) - 1):
        if i + 1 <= 9:
            j = i+0.5
            xticks.append(j)
            xlabels.append(str(i + 1))
        else:
            if count == 4:
                j = i+0.5
                xticks.append(j + 2)
                if len(stats.base_pos.keys()) - i < 5:
                    xlabels.append(str(i + 1) + ' - ' + str(len(stats.base_pos.keys())))
                else:
                    xlabels.append(str(i + 1) + ' - ' + str(i + 5))
                count -= 1
            elif 0 < count < 3:
                count -= 1
            elif count == 0:
                count = 4
    plt.xticks(xticks, xlabels, fontsize=5)
    plt.yticks(np.arange(0, maximum, 10), np.arange(0, maximum, 10), fontsize=5)
    plt.xlabel('Position in read (bp)', fontsize=5)
    plt.legend(('% A', '% C', '% G', '% T'), loc='upper right')
    plt.suptitle('Per base sequence content', fontweight='bold', color='darkred', horizontalalignment='right')
    plt.title('Sequence content across all bases', size=4)
    plt.savefig(os.path.join(*out, 'pictures', 'Per_base_sequence_content.png'), figsize=(30, 10), dpi=200, facecolor='white')
    plt.close()


def reads_length_distribution(out):
    global max_len
    global min_len
    max_len = max(stats.read_length.keys())
    min_len = min(stats.read_length.keys())
    stats.read_length[max_len + 1] = 0
    stats.read_length[min_len - 1] = 0
    plt.figure()
    maximum = max(stats.read_length.values())
    # sns.kdeplot(stats.read_length, bw=0.5, color='darkred')
    sns.lineplot(data=stats.read_length, legend=False, color='darkred')
    for i in range(min_len - 1, max_len + 1):
        if i % 2 == 0:
            plt.fill_between([i-0.5, i+0.5], [maximum, maximum], color='lightgrey')
    plt.xlim(min_len - 1, max_len + 1)
    plt.legend(labels=['Sequence length'], loc='upper right')
    plt.title('Distribution of sequence length over all sequences', fontsize=17)
    plt.xlabel('Sequence length base pare', fontsize=15)
    plt.savefig(os.path.join(*out, 'pictures', 'Sequence_length_distribution.png'), figsize=(30, 10), dpi=200, facecolor='white')
    plt.close()


def per_sequence_quality_score_print(out):   # plotting
    sns.set_style("darkgrid")
    qual_score = np.array(stats.mean_qual_score, dtype='int')
    scores, ditrib = np.unique(qual_score, return_counts=True)
    p = sns.lineplot(x =scores, y=ditrib, color="red")
    p.set_title("Quality score distribution over all sequences", fontsize=14)
    p.set_xlabel("Mean Sequence Quality", fontsize=14)
    plt.savefig(os.path.join(*out, 'pictures', "Per_Sequence_Quality_Scores.png"))
    plt.close()
