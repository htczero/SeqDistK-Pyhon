# -*- coding: UTF-8 -*-
# @File: KtupleData.py
# @Author: htczero
# @Create Data:  2019/11/16
# @Modify Data:  2019/11/16
# @Email: htczero@hotmail.com
from typing import Dict
import numpy as np
import numba as nb


class KtupleData:
    def __init__(self):
        self._ktuple_dic = dict()  # type: Dict[int, np.ndarray]

    def get_ktuple(self, sequence: np.ndarray, k: int) -> np.ndarray:
        if k not in self._ktuple_dic:
            self._ktuple_dic.setdefault(k, self._count_ktuple(sequence, k))
        return self._ktuple_dic[k]

    @staticmethod
    @nb.jit('int32[:](int32[:], int32)')
    def _count_ktuple(sequence: np.ndarray, k: int) -> np.ndarray:
        base = sequence.astype(dtype=np.int32)
        total = base
        ktuple_list = np.zeros(4 ** k, dtype=np.int32)
        for _ in range(k - 1):
            base = np.roll(base, -1)
            total = np.left_shift(total, 2) + base

        end = len(base) - k + 1

        for index in total[:end]:
            ktuple_list[index] += 1

        return ktuple_list

    def clear(self, k):
        if k in self._ktuple_dic:
            del self._ktuple_dic[k]
