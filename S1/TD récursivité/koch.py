# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL.
"""

import koch_drawer as kd


def decoupe(pd, pf, n):
    # Trace le segment
    if n == 0:
        kd.draw(pd, pf)
        return None
    # Calcule les points p1/3, ps et p2/3 du schéma
    # Utiliser ces points pour les appels récursifs quand il le faut
    p1 = ((2 * pd[0] + pf[0]) / 3, (2 * pd[1] + pf[1]) / 3)
    p2 = ((pd[0] + 2 * pf[0]) / 3, (pd[1] + 2 * pf[1]) / 3)
    ps = ((pd[0] + pf[0]) / 2 - (pf[1] - pd[1]) / (2 * (3 ** 0.5)),
          (pd[1] + pf[1]) / 2 + (pf[0] - pd[0]) / (2 * (3 ** 0.5)))

    decoupe(pd, p1, n - 1)
    decoupe(p1, ps, n - 1)
    decoupe(ps, p2, n - 1)
    decoupe(p2, pf, n - 1)


def koch(flocon, n):
    for i in range(len(flocon)-1):
        decoupe(flocon[i], flocon[i+1], n)


if __name__ == "__main__":
    x = (0, 0)
    y = (1, 0)
    z = (0.5, 3 ** 0.5 / 2)
    courbe = [x, y]
    flocon = [x, z, y, x]

    n = 5

    # Pour découper 
    decoupe(x, y, n)

    # pour traiter le flocon :
    # ecrire une fonction koch(flocon, n)
    # qui découpe (n fois) chaque segment de la liste flocon

    # koch(flocon, n)

    print(kd.longueur())

    kd.draw_koch()
