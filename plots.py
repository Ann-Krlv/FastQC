import seaborn as sns
import matplotlib.pyplot as plt
import stats
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'


def basic_statistics():
    pass


def per_base_sequence_quality():
    plot1 = sns.boxplot(data=stats.base_qsc,
                        saturation=1,
                        showfliers=False,
                        color='yellow',
                        medianprops=dict(color="red"),
                        boxprops=dict(edgecolor='black'),
                        linewidth=0.2,
                        whis=(10, 90))
    mean_var = [sum(i) / len(i) for i in stats.base_qsc]  # list with mean quality per position
    sns.lineplot(data=mean_var, ax=plot1, legend=False, linewidth=0.3)  # add mean line plot
    plt.fill_between([0, len(stats.base_qsc)], [20, 20], color="lightcoral", alpha=0.1)
    plt.fill_between([0, len(stats.base_qsc)], [20, 20], [28, 28], color="yellow", alpha=0.1)
    plt.fill_between([0, len(stats.base_qsc)], [28, 28], [40, 40], color="lightgreen", alpha=0.1)
    for i in range(0, len(stats.base_qsc) - 1, 2):
        plt.fill_between([i, i + 1], [20, 20], color="lightcoral", alpha=0.1)
        plt.fill_between([i, i + 1], [20, 20], [28, 28], color="yellow", alpha=0.1)
        plt.fill_between([i, i + 1], [28, 28], [40, 40], color="lightgreen", alpha=0.1)
    ax = plt.axes()
    ax.set_facecolor(color='white')
    xticks = []
    xlabels = []
    count = 4
    for i in range(0, len(stats.base_qsc) - 1):
        if i + 1 <= 9:
            xticks.append(i)
            xlabels.append(str(i + 1))
        else:
            if count == 4:
                xticks.append(i + 2)
                if len(stats.base_qsc) - i < 5:
                    xlabels.append(str(i + 1) + ' - ' + str(len(stats.base_qsc)))
                else:
                    xlabels.append(str(i + 1) + ' - ' + str(i + 5))
                count -= 1
            elif 0 < count < 4:
                count -= 1
            elif count == 0:
                count = 4
    plt.xticks(xticks, xlabels, fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel('Position in read (bp)', fontsize=5)
    plt.title('Per base sequence quality', fontweight='bold', color='darkred', loc='left')
    plt.suptitle('\n\n\n\n\n\n\nQuality scores across all bases (Sanger / Illumina 1.9 encoding)', size=4)
    plot1.figure.savefig("Per_base_quality.png", figsize=(30, 10), dpi=200)


def per_sequence_GC_content():
    gc_content = pd.DataFrame(stats.gc_content, columns=['GC content'])
    gc_content.plot(kind='density')
    # plt.savefig("Per_sequence_GC_content.png", figsize=(30, 10), dpi=200)


'''
now it creates pandas.Series with amount of each duplication level value
you can draw plot from it but it will be differ with original in values (general shape will be same)
def duplicated_reads():
    tmp_df = pd.DataFrame({'Sequence': stats.over_seq.keys(),
                           'count': stats.over_seq.values()})

    dup_df = tmp_df['count'].value_counts()
    dup_df.to_csv('duplicated_sequences.tsv', sep='\t')
'''


def overrepresented_table(cnt):
    over_df = pd.DataFrame({'Sequence': stats.over_seq.keys(),
                            'Count': stats.over_seq.values(),
                            'Percentage': [i*100/cnt for i in stats.over_seq.values()]})
    res_df = over_df.loc[over_df['Percentage'] > 0.0999999999]
    res_df.sort_values('Count', ascending=False, inplace=True, ignore_index=True)
    res_df.set_index('Sequence', inplace=True)
    res_df.to_csv('overrepresented_sequences.tsv', sep='\t')

def per_base_sequence_content():
    maximum = max(max(stats.base_content_dict['A']),max(stats.base_content_dict['C']),max(stats.base_content_dict['G'])
                  ,max(stats.base_content_dict['T']))
    figure = plt.figure()
    plt.plot(stats.base_content_dict['A'],color='limegreen')
    plt.plot(stats.base_content_dict['C'],color='blue')
    plt.plot(stats.base_content_dict['G'],color='black')
    plt.plot(stats.base_content_dict['T'],color='red')
    for i in range(0, len(stats.base_content_dict['A']) - 1, 2):
        plt.fill_between([i, i + 1], [maximum, maximum], color="lightgrey")
    xticks = []
    xlabels = []
    count = 4
    for i in range(0, len(stats.base_content_dict['A']) - 1):
        if i + 1 <= 9:
            j=i+0.5
            xticks.append(j)
            xlabels.append(str(i + 1))
        else:
            if count == 4:
                j=i+0.5
                xticks.append(j + 2)
                if len(stats.base_content_dict['A']) - i < 5:
                    xlabels.append(str(i + 1) + ' - ' + str(len(stats.base_content_dict['A'])))
                else:
                    xlabels.append(str(i + 1) + ' - ' + str(i + 5))
                count -= 1
            elif 0 < count < 4:
                count -= 1
            elif count == 0:
                count = 4
    plt.xticks(xticks, xlabels, fontsize=5)
    plt.yticks(np.arange(0,maximum,10),np.arange(0,maximum,10),fontsize=5)
    plt.xlabel('Position in read (bp)', fontsize=5)
    plt.legend(('% A','% C','% G','% T'),loc = 'upper right')
    plt.suptitle('Per base sequence content', fontweight='bold', color='darkred', horizontalalignment='right')
    plt.title('Sequence content across all bases', size = 4)
    plt.savefig("Per_base_sequence_content.png", figsize=(30, 10), dpi=200, facecolor = 'white')