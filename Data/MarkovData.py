# -*- coding: UTF-8 -*-
# @File: MarkovData.py
# @Author: htczero
# @Create Data:  2019/11/16
# @Modify Data:  2019/11/16
# @Email: htczero@hotmail.com
import numpy as np
from typing import Dict
import numba as nb


class MarkovData:
    def __init__(self):
        self._markov_dic = dict()  # type: Dict[int, Dict[int, np.ndarray]]
        self._markov_tmp = dict()  # type: Dict[int, np.ndarray]

    def get_markov_possibility(self, k: int, r: int, total_1: int, ktuple_1: np.ndarray,
                               ktuple_2: np.ndarray) -> np.ndarray:
        if k not in self._markov_dic or r not in self._markov_dic[k]:
            markov_tmp = self._get_markov_tmp(r, ktuple_2)
            self._markov_dic.setdefault(k, dict())
            self._markov_dic[k].setdefault(r, MarkovData._cal_markov_possibility(ktuple_1, total_1, markov_tmp, r, k))
        return self._markov_dic[k][r]

    @staticmethod
    @nb.jit('float64[:](int32[:],int32,float64[:],int32,int32)', nopython=True, fastmath=True, parallel=True)
    def _cal_markov_possibility(ktuple_1: np.ndarray, total_1: int, markov_tmp: np.ndarray, r: int,
                                k: int) -> np.ndarray:
        ktuple_k = np.arange(4 ** k)
        markov = np.ones(ktuple_k.size, dtype=np.float64)
        flag = 4 ** (r + 1) - 1
        for i in range(k - r):
            index = np.bitwise_and(np.right_shift(ktuple_k, i * 2), flag)
            markov = np.multiply(markov, markov_tmp[index])
        if r != 0:
            index = np.right_shift(ktuple_k, (k - r) * 2)
            markov = np.multiply(markov, np.divide(ktuple_1[index], total_1))
        return markov

    def _get_markov_tmp(self, r: int, ktuple: np.ndarray) -> np.ndarray:
        if r not in self._markov_tmp:
            self._markov_tmp.setdefault(r, self._cal_markov_tmp(ktuple))
        return self._markov_tmp[r]

    @staticmethod
    def _cal_markov_tmp(ktuple: np.ndarray) -> np.ndarray:
        tmp = ktuple.reshape(-1, 4).sum(axis=1)
        tmp = np.tile(tmp, (4, 1)).ravel('F')
        tmp = np.divide(ktuple, tmp)
        tmp[np.isinf(tmp)] = 0
        return tmp

    def clear_tmp(self, r):
        if r in self._markov_tmp:
            del self._markov_tmp[r]

    def clear(self, k: int):
        if k in self._markov_tmp:
            del self._markov_dic[k]
