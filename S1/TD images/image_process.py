#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Fonctions de traitement d'images.
Version non optimisée.

.. codeauthor:: R. Moitié
"""

import numpy as np


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
    res = np.zeros(img.shape, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                res[i, j, k] = img[i, j, k]
    return res


def negative(img):
    res = copy(img)
    return 255 - res


def h_flip(img):
    temp = copy(img)
    res = np.zeros(img.shape, dtype=np.uint8)
    sh = res.shape
    for i in range(1, sh[0]):
        for j in range(sh[1]):
            for k in range(sh[2]):
                res[i, j, k] = temp[sh[0]-i, j, k]
    return res


def v_flip(img):
    temp = copy(img)
    res = np.zeros(img.shape, dtype=np.uint8)
    sh = res.shape
    for i in range(sh[0]):
        for j in range(1, sh[1]):
            for k in range(sh[2]):
                res[i, j, k] = temp[i, sh[1]-j, k]
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


def rotate_colors(img):
    res = copy(img)
    res[:, :, 0] = np.roll(res[:, :, 0], 1)
    print(res)
    return res


def zoom(img):
    w, h, lay = img.shape
    res = np.zeros(img.shape, dtype=np.uint8)
    tmp = img[3*w//8:5*w//8, 3*h//8:5*h//8, :]
    for i in range(w//4):
        for j in range(h//4):
            for k in range(lay):
                res[2*i, 2*j, k] = tmp[i, j, k]
                res[2 * i + 1, 2 * j, k] = tmp[i, j, k]
                res[2 * i, 2 * j + 1, k] = tmp[i, j, k]
                res[2 * i + 1, 2 * j + 1, k] = tmp[i, j, k]
    return res

