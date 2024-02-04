
import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import PercentFormatter
from sklearn import datasets
from pandas.plotting import scatter_matrix
from pathlib import Path
import hydra 


def scatter_plot (dataframe, res_path, features, species):
    fig = plt.figure()
    # Automatic creation
    # axes = plt.subplots(4,4)
    # plt.subplots_adjust(wspace=0, hspace=0)
    # Manual creation (with changed access type!):
    gs = plt.GridSpec(4, 4, wspace=0, hspace=0)
    axes = [[fig.add_subplot(gs[i : i + 1, j : j + 1]) for j in range(4)] for i in range(4)]

    for i, f1 in enumerate(features):
        for j, f2 in enumerate(features):
            # Scatterplots
            axes[i][j].sharey(axes[i][0 if i else 1])
            if i != j:
                axes[i][j].sharex(axes[0 if j else 1][j])
            axes[i][j].yaxis.set_visible(j == 0)
            axes[i][j].xaxis.set_visible(i == len(features) - 1)
            axes[i][j].set_ylabel(features[f1]["name"])
            axes[i][j].set_xlabel(features[f2]["name"])

            if i == j:
                continue

            for s in species:
                axes[i][j].scatter(
                    dataframe[dataframe["Class"] == s][f2],
                    dataframe[dataframe["Class"] == s][f1],
                    color=species[s]["color"],
                    label=species[s]["name"],
                    alpha=0.5,
                )

        # Histogram
        ax_hist = axes[i][i].twinx()
        ax_r = axes[i][3].twinx()

        # Rightmost plots have shared twin axes with histograms to add labels
        ax_r.sharey(ax_hist)
        ax_hist.xaxis.set_visible(False)
        ax_hist.yaxis.set_visible(False)
        ax_r.xaxis.set_visible(False)
        ax_r.yaxis.set_visible(True)
        ax_r.set_ylabel("Percent in dataset")
        # This creates percentages
        ax_r.yaxis.set_major_formatter(PercentFormatter(1))

        for s in species:
            # Weights required for percentages (to ensure sum == 0)
            data = dataframe[dataframe["Class"] == s][f1]
            ax_hist.hist(
                data,
                color=species[s]["color"],
                alpha=0.5,
                weights=np.full(len(data), 1/len(data)),
                label=species[s]["name"],
            )

        if i == 0:
            ax_hist.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":

    # Opening CSV file
    try:
        dataframe = pd.read_csv("iris.csv")
    except IOError:
        pass

    # Loading dataset from sklearn package
    iris = datasets.load_iris()
    # Creating data frame for pandas
    dataframe = pd.DataFrame(iris["data"], columns=iris["feature_names"])

    # Download from the internet
    csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    # Requires setting column names manually
    col_names = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width", "Class"]
    dataframe = pd.read_csv(csv_url, names=col_names)

    # Colors were obtained via np.unique(scatter_matrix[0][1].get_children()[0].get_facecolor(), axis = 0)
    species = {
        "Iris-setosa": {
            "name": "Setosa",
            "color": (0.267004, 0.004874, 0.329415, 0.8),
        },
        "Iris-versicolor": {
            "name": "Versicolor",
            "color": (0.127568, 0.566949, 0.550556, 0.8),
        },
        "Iris-virginica": {
            "name": "Virginica",
            "color": (0.993248, 0.906157, 0.143936, 0.8),
        },
    }

    # Mostly unused
    features = {
        "Sepal_Length": {
            "name": "Sepal length (cm)",
        },
        "Sepal_Width": {
            "name": "Sepal width (cm)",
        },
        "Petal_Length": {
            "name": "Petal length (cm)",
        },
        "Petal_Width": {
            "name": "Petal width (cm)",
        },
    }
    for e, c in zip(features.values(), cm.rainbow(np.linspace(0, 1, len(features)))):
        e["color"] = c

    # General settings
    plt.rcParams.update({"font.size": 16})
    plt.rcParams["figure.figsize"] = (20, 20)

    scatter_plot(dataframe, Path("res.jpg"), features, species)
else:
    print(f"My __name__ is {__name__}")
