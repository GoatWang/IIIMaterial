import matplotlib.pyplot as plt
from planar_utils import plot_decision_boundary, sigmoid, load_planar_dataset, load_extra_datasets
import numpy as np
import os



def load():
    X, Y = load_planar_dataset()
    name = 'flower'
    X = X.T
    Y = Y[0]
    # plt.scatter(X[:, 0], X[:, 1], c=Y , s=40, cmap=plt.cm.Spectral);
    # plt.title(name+'_original')
    # plt.savefig(os.path.join('pic', name+'_original'))
    # plt.show()



    # load dataset
    noisy_circles, noisy_moons, blobs, gaussian_quantiles, no_structure = load_extra_datasets()
    datasets = {"noisy_circles": noisy_circles,
                "noisy_moons": noisy_moons,
                "blobs": blobs,
                "gaussian_quantiles": gaussian_quantiles}

    datas = [(name, X, Y), ]
    for name, dataset in datasets.items():
        X, Y = datasets[name]
        datas.append((name, X, Y))

    #     print(X.shape)
    #     print(Y.shape)

        # Visualize the data
    #     plt.scatter(X[:, 0], X[:, 1], c=Y, s=40, cmap=plt.cm.Spectral)
    #     plt.title(name+'_original')
    #     plt.savefig(os.path.join('pic', name+'_original'))
    #     plt.show()
    return datas