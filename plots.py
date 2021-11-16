import seaborn as sns
import matplotlib.pyplot as plt
import stats


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
