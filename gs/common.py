import itertools as it
import os
import os.path as osp
from pathlib import Path
from typing import Tuple, Iterable, Any, List

import matplotlib.pylab as pl
import numpy as np


class Dim:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return "<Dim rows:{} cols:{}>".format(self.rows, self.cols)


# f: A function returning an Iterable
def flatmap(f, list_of_list: Iterable[Any]) -> Iterable[Any]:
    return it.chain.from_iterable(map(f, list_of_list))


def core_indices(rows: int, cols: int, delta: int) -> Iterable[Tuple[int, int]]:
    for i in range(delta, rows - delta):
        for j in range(delta, cols - delta):
            yield (i, j)


def square_indices_rows(delta: int) -> Iterable[Tuple[int, int]]:
    for i in range(-delta, delta + 1):
        for j in range(-delta, delta + 1):
            yield (i, j)


def square_indices_cols(delta: int) -> Iterable[Tuple[int, int]]:
    for i in range(-delta, delta + 1):
        for j in range(-delta, delta + 1):
            yield (j, i)


def square_indices_rows_cols(delta: int) -> Iterable[Tuple[int, int]]:
    return flatmap(lambda l: l, [square_indices_rows(delta), square_indices_cols(delta)])


def work_file(name: str, _dir: str = None) -> str:
    home_dir = Path.home()
    if _dir is None:
        work_dir = osp.join(home_dir, 'work', 'work-greenscreen')
    else:
        work_dir = osp.join(home_dir, 'work', 'work-greenscreen', _dir)
    if not osp.exists(work_dir):
        print("created work dir: '{}'".format(work_dir))
        os.makedirs(work_dir)
    return osp.join(work_dir, name)


def load_image(path: str, dim: Dim) -> np.array:
    def validate(img: np.array):
        rows = img.shape[0]
        cols = img.shape[1]
        if rows != dim.rows or cols != dim.cols:
            msg = "Illegal dimension of image {}: {}/{}. expected: {}/{}" \
                .format(path, rows, cols, dim.rows, dim.cols)
            raise AssertionError(msg)

    re = pl.imread(path)
    validate(re)
    return re


def create_features(img: np.array, row: int, col: int, idx_rel: List[Tuple[int, int]]) -> np.array:
    re = np.empty(0, dtype=float)
    for row_off, col_off in idx_rel:
        row1 = row + row_off
        col1 = col + col_off
        green = img[row1, col1]
        re = np.hstack((re, green))
    return re