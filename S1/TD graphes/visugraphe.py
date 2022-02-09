import matplotlib.pyplot as plt
import numpy as np


def visu_graphe_simple(g):
    ax = plt.axes()
    nbn = len(g.nodes)

    x = np.cos(np.pi / 2 + np.arange(0, 2 * np.pi - np.pi / nbn, 2 * np.pi / nbn))
    y = np.sin(np.pi / 2 + np.arange(0, 2 * np.pi - np.pi / nbn, 2 * np.pi / nbn))

    for i, n in enumerate(g.nodes):
        for nn in n.neighbors:
            j = g.nodes.index(nn)
            plt.plot([x[i], x[j]], [y[i], y[j]], 'k')

    plt.plot(x, y, 'o', ms=20)
    for i in range(len(x)):
        ax.annotate(g.nodes[i].name, xy=(x[i], y[i]), xytext=(1.15 * x[i], 1.15 * y[i]),
                    horizontalalignment='center', verticalalignment='center')
        # plt.text(x[i]*1.1, y[i]*1.1, g.nodes[i].name)
    plt.xlim(-1.2, 1.25)
    plt.ylim(-1.2, 1.25)
    plt.show()


def visu_graphe_color(g):
    ax = plt.axes()
    nbn = len(g.nodes)

    x = np.cos(np.pi / 2 + np.arange(0, 2 * np.pi - np.pi / nbn, 2 * np.pi / nbn))
    y = np.sin(np.pi / 2 + np.arange(0, 2 * np.pi - np.pi / nbn, 2 * np.pi / nbn))

    for i, n in enumerate(g.nodes):
        for nn in n.neighbors:
            j = g.nodes.index(nn)
            plt.plot([x[i], x[j]], [y[i], y[j]], 'k')

    maxcoul = max([n.color for n in g.nodes])
    for c in range(maxcoul + 1):
        ind = [i for i in range(nbn) if g.nodes[i].color == c]
        plt.plot(x[ind], y[ind], 'o', ms=20)
    for i in range(len(x)):
        ax.annotate(g.nodes[i].name, xy=(x[i], y[i]), xytext=(1.15 * x[i], 1.15 * y[i]),
                    horizontalalignment='center', verticalalignment='center')
    plt.xlim(-1.2, 1.25)
    plt.ylim(-1.2, 1.25)
    plt.show()


def visu_graphe_coord(g):
    ax = plt.axes()
    nbn = len(g.nodes)

    x = np.array([n.x for n in g.nodes])
    y = np.array([n.y for n in g.nodes])
    print(x)
    print(y)
    xmin = np.min(x)
    xmax = np.max(x)
    ymin = np.min(y)
    ymax = np.max(y)
    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2
    d = max(xmax - xmin, ymax - ymin) / 15
    for i, n in enumerate(g.nodes):
        for nn in n.neighbors:
            j = g.nodes.index(nn)
            plt.plot([x[i], x[j]], [y[i], y[j]], 'k')

    maxcoul = max([n.color for n in g.nodes])
    for c in range(maxcoul + 1):
        ind = [i for i in range(nbn) if g.nodes[i].color == c]
        plt.plot(x[ind], y[ind], 'o', ms=20)
    for i in range(len(x)):
        theta = np.arctan2(y[i] - cy, x[i] - cx)
        ax.annotate(g.nodes[i].name, xy=(x[i], y[i]),
                    xytext=(x[i] + d * np.cos(theta) * 0, y[i] + d * np.sin(theta) * 0),
                    horizontalalignment='center', verticalalignment='center')
    plt.xlim(xmin - 2 * d, xmax + 2 * d)
    plt.ylim(ymin - 2 * d, ymax + 2 * d)
    plt.show()
