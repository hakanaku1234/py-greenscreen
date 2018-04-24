import os
import os.path as osp
from typing import List, Tuple, Iterable

import matplotlib.pylab as pl
import numpy as np

imgDir = "res/img100"


def images() -> List[str]:
    return os.listdir(imgDir)


def create_training_img_arrays(img_name: str) -> Iterable[Tuple[np.array, np.array]]:
    fnamg = "bsp{}_0.png".format(img_name)
    fnamt = "bsp{}_1.png".format(img_name)
    img: np.array = pl.imread(osp.join(imgDir, fnamg))
    imt: np.array = pl.imread(osp.join(imgDir, fnamt))[:, :, -1:]  # use only the transparent value
    return img, imt


def core_indices(rows: int, cols: int, delta: int) -> Iterable[Tuple[int, int]]:
    for i in range(delta, rows - delta):
        for j in range(delta, cols - delta):
            yield (i, j)


def square_indices(delta: int) -> Iterable[Tuple[int, int]]:
    for i in range(-delta, delta + 1):
        for j in range(-delta, delta + 1):
            yield (i, j)


def create_training_data(name: str, delta: int) -> Iterable[np.array]:
    g, t = create_training_img_arrays(name)
    rows = g.shape[0]
    cols = g.shape[1]
    ci = core_indices(rows, cols, delta)
    for r, c in ci:
        transp = t[r, c, 0]
        greens = np.empty(0, dtype=float)
        for i, j in square_indices(delta):
            r1 = r + i
            c1 = c + j
            green = g[r1, c1]
            greens = np.hstack((greens, green))
        yield np.hstack((greens, transp))


# TODO Solve the flat map problem
# [filename for path in dirs for filename in os.listdir(path)]

a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
b = [[6, 5, 4, 3, 2], [6, 5, 4, 3, 2]]

x = [a1 for a1 in a for b1 in b]

print(x)

'''
for idx, line in enumerate(create_training_data('1', 10)):
    print("{} {}".format(idx, line))

for x, y in square_indices(7):
    print("{}, {}".format(x, y))


    
    
for i in range(0, 100):
    for j in range(0, 133):
        x = t[i, j]
        print("{} {} {}".format(i, j, x))



g, t = create_training_img_arrays('1')
dimg = g.shape[0:2]
print("green {}".format(dimg))
dimt = t.shape[0:2]
print("transp {}".format(dimt))


'''
