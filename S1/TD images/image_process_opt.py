#!/usr/bin/python3

"""Fonctions de traitement d'images.
Version optimisée.

.. codeauthor:: R. Moitié
"""

import numpy as np

from scipy.ndimage.filters import convolve


def copy(img):
    """Copie la couleur (3 valeurs) de chaque pixel.

    Parameters
    ----------
    img : numpy.array
        Image source.

    Returns
    -------
    res : numpy.array
        Image résultat
    """
    res = img.copy()
    return res


def negative(img):
    return 255 - img


def h_flip(img):
    res = copy(img)
    res[:] = np.flipud(res[:])
    return res


def v_flip(img):
    res = copy(img)
    res[:] = np.fliplr(res[:])
    return res


def red(img):
    res = np.zeros(img.shape, dtype=np.uint8)
    res[:, :, 2] = img[:, :, 2]
    return res


def green(img):
    res = np.zeros(img.shape, dtype=np.uint8)
    res[:, :, 1] = img[:, :, 1]
    return res


def blue(img):
    res = np.zeros(img.shape, dtype=np.uint8)
    res[:, :, 0] = img[:, :, 0]
    return res


def convol(img, W):
    res = convolve(img, W, cval=0.0)
    return res.astype(np.uint8)


def blur(img):
    res = copy(img)
    W = np.ones((3, 3))
    for i in range(3): res[:, :, i] = convol(img[:, :, i], 1/9 * W)
    return res


def zoom(img):
    res = np.zeros(img.shape, dtype=np.uint8)
    return res


def edge(img):
    h1 = np.asarray([[-.5, -1, -.5], [0, 0, 0], [.5, 1, .5]])
    h2 = np.asarray([[-.5, 0, .5], [-1, 0, 1], [-.5, 0, .5]])
    G1 = copy(img)
    G2 = copy(img)

    for i in range(3): G1[:, :, i] = convol(img[:, :, i], h1)
    for i in range(3): G2[:, :, i] = convol(img[:, :, i], h2)

    res = abs(G1) + abs(G2)
    res = res % 255
    return res
