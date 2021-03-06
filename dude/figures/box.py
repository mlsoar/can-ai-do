#%%
import json
import numpy as np
import pandas as pd
from pathlib import Path

# need seaborn support `positions` https://github.com/0ut0fcontrol/seaborn/commit/f1d6a3ead56e2e6398484a4ed159fc0efce1230b
import matplotlib
# matplotlib.use("nbAgg")
from matplotlib import pyplot as plt
print(plt.get_backend())
import seaborn as sns

# https://ipython-books.github.io/61-using-matplotlib-styles/
# print(matplotlib.style.available)
# matplotlib.style.use('seaborn-whitegrid')
#%%
print(Path.cwd())
root = Path('dude/figures')
files = {
    'DUD-E\nRandom CV': 'full.random3fold.None.csv',
    'DUD-E (rmMW>500)\nRandom CV': 'full.random3fold.rmMW500.csv',
    'DUD-E\nCross-Class CV': 'full.family3fold.None.csv',
    'DUD-E (rmMW>500)\nCross-Class CV': 'full.family3fold.rmMW500.csv',
}
dfs = {}
for k, v in files.items():
    dfs[k] = pd.read_csv(root / 'result' / v)
df = pd.concat(dfs, names=['dataset']).reset_index()
N = len(dfs)

#%%
offset = 0.2
d = df.loc[df['feat'] == 'prop']
roc = d.loc[df['metric'] == 'ROC']
ef1 = d.loc[df['metric'] == 'EF1']
fig, ax = plt.subplots()
ax2 = ax.twinx()
width = 0.4
colors = sns.color_palette("Set2")
sns.boxplot(
    x='dataset',
    y='value',
    data=ef1,
    ax=ax,
    # showfliers=False,
    positions=np.arange(N) - offset,
    width=0.35,
    color=colors[0],
)

sns.boxplot(
    x='dataset',
    y='value',
    data=roc,
    ax=ax2,
    # showfliers=False,
    positions=np.arange(N) + offset,
    width=0.35,
    # palette="Set2",
    color=colors[1],
)

ax.set_xlabel('')
ax.set_ylabel('$EF_1$')
ef1_l, ef1_u = 0, 62
ef1_diff = ef1_u - ef1_l
ax.set_ylim([ef1_l - ef1_diff * 0.2, ef1_u + ef1_diff * 0.05])
ax.set_yticks(np.linspace(0, 60, 7))
ax2.set_ylabel('$AUC$')
auc_l, auc_u = 0.5, 1.0
auc_diff = auc_u - auc_l
ax2.set_ylim([auc_l - auc_diff * 0.2, auc_u + auc_diff * 0.05])
ax2.set_yticks(np.linspace(0.4, 1, 7))

ax.set_title("PROP+RF Performance on DUD-E (102 Targets)")


# https://github.com/0ut0fcontrol/seaborn/blob/master/seaborn/categorical.py
def add_legend_data(ax, color, label):
    """Add a dummy patch object so we can get legend data."""
    rect = plt.Rectangle([0, 0],
                         0,
                         0,
                         edgecolor='gray',
                         facecolor=color,
                         label=label)
    ax.add_patch(rect)


add_legend_data(ax, colors[0], '$EF_1$')
add_legend_data(ax, colors[1], '$AUC$')
ax.legend(frameon=False, loc='lower center', ncol=2)
fig.savefig(root / 'PROP.jpg', dpi=300)

#%%
offset = 0.2
d = df.loc[df['feat'] == 'fp']
roc = d.loc[df['metric'] == 'ROC']
ef1 = d.loc[df['metric'] == 'EF1']
fig, ax = plt.subplots()
ax2 = ax.twinx()
width = 0.4
colors = sns.color_palette("Set2")
sns.boxplot(
    x='dataset',
    y='value',
    data=ef1,
    ax=ax,
    # showfliers=False,
    positions=np.arange(N) - offset,
    width=0.35,
    color=colors[0],
)

sns.boxplot(
    x='dataset',
    y='value',
    data=roc,
    ax=ax2,
    # showfliers=False,
    positions=np.arange(N) + offset,
    width=0.35,
    # palette="Set2",
    color=colors[1],
)

ax.set_xlabel('')
ax.set_ylabel('$EF_1$')
ef1_l, ef1_u = 0, 62
ef1_diff = ef1_u - ef1_l
ax.set_ylim([ef1_l - ef1_diff * 0.2, ef1_u + ef1_diff * 0.05])
ax.set_yticks(np.linspace(0, 60, 7))
ax2.set_ylabel('$AUC$')
auc_l, auc_u = 0.5, 1.0
auc_diff = auc_u - auc_l
ax2.set_ylim([auc_l - auc_diff * 0.2, auc_u + auc_diff * 0.05])
ax2.set_yticks(np.linspace(0.4, 1, 7))

ax.set_title("FP+RF Performance on DUD-E (102 Targets)")


# https://github.com/0ut0fcontrol/seaborn/blob/master/seaborn/categorical.py
def add_legend_data(ax, color, label):
    """Add a dummy patch object so we can get legend data."""
    rect = plt.Rectangle([0, 0],
                         0,
                         0,
                         edgecolor='gray',
                         facecolor=color,
                         label=label)
    ax.add_patch(rect)


add_legend_data(ax, colors[0], '$EF_1$')
add_legend_data(ax, colors[1], '$AUC$')
ax.legend(frameon=False, loc='lower center', ncol=2)
fig.savefig(root / 'FP.jpg', dpi=300)

#%%
