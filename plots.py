import seaborn as sns
import matplotlib.pyplot as plt
import stats

def basic_statistics():

'''
def per_base_sequence_quality():
    plot1 = sns.boxplot(data=stats.base_qsc,
                        saturation=1,
                        showfliers=False,
                        color='yellow',
                        medianprops=dict(color="red"),
                        boxprops=dict(edgecolor='black'),
                        linewidth=0.2,
                        whis=(10, 90))
    mean_var = [sum(i)/len(i) for i in stats.base_qsc]  # list with mean quality per position
    sns.lineplot(data=mean_var, ax=plot1, legend=False, linewidth=0.3)  # add mean line plot
    plot1.figure.savefig("Per_base_quality.png", figsize=(30, 10), dpi=200)
'''


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
    plt.suptitle('\n\n\n\n\n\n\nQuality scores across all bases (Sanger / Illumina 1.9 encoding)', size = 4)
    plot1.figure.savefig("Per_base_quality.png", figsize=(30, 10), dpi=200)
