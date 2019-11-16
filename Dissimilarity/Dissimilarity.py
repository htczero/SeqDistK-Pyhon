# -*- coding: UTF-8 -*-
# @File: Dissimilarity.py
# @Author: htczero
# @Create Data:  2019/11/16
# @Modify Data:  2019/11/16
# @Email: htczero@hotmail.com
import numpy as np
import numba as nb
from Data import SequenceData
from Data import Result
from typing import List


class Dissimilarity:
    @staticmethod
    @nb.jit('float64(int32[:],int32[:])', nopython=True)
    def _get_D2(ktuple_1: np.ndarray, ktuple_2: np.ndarray) -> np.float64:
        t = np.multiply(ktuple_1, ktuple_2).sum()
        p = np.sqrt(np.sum(np.square(ktuple_1))) * np.sqrt(np.sum(np.square(ktuple_2)))
        return 0.5 * (1 - t / p)

    @staticmethod
    def get_D2(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r: int = None) -> None:
        ktuple_1 = seq_x.get_ktuple(k)
        ktuple_2 = seq_y.get_ktuple(k)
        res = Dissimilarity._get_D2(ktuple_1, ktuple_2)
        key = 'D2_k{}'.format(k)
        result.add(key, seq_x.id, seq_y.id, res)

    @staticmethod
    @nb.jit('float64(int32[:],int32[:],int32,int32)', nopython=True)
    def _get_Ch(ktuple_1: np.ndarray, ktuple_2: np.ndarray, total_1: int, total_2: int) -> np.float64:
        ktuple_1 = np.divide(ktuple_1, total_1)
        ktuple_2 = np.divide(ktuple_2, total_2)
        res = np.abs(np.subtract(ktuple_1, ktuple_2)).max()  # type: np.float64
        return res

    @staticmethod
    def get_Ch(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r: int = None) -> None:
        ktuple_1 = seq_x.get_ktuple(k)
        ktuple_2 = seq_y.get_ktuple(k)
        res = Dissimilarity._get_Ch(ktuple_1, ktuple_2, seq_x.get_total(k), seq_y.get_total(k))
        key = 'Ch_k{}'.format(k)
        result.add(key, seq_x.id, seq_y.id, res)

    @staticmethod
    @nb.jit('float64(int32[:],int32[:],int32,int32)', nopython=True)
    def _get_Eu(ktuple_1: np.ndarray, ktuple_2: np.ndarray, total_1: int, total_2: int) -> np.float64:
        ktuple_1 = np.divide(ktuple_1, total_1)
        ktuple_2 = np.divide(ktuple_2, total_2)
        res = np.sqrt(np.sum(np.square(np.subtract(ktuple_1, ktuple_2))))  # type: np.float64
        return res

    @staticmethod
    def get_Eu(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r: int = None) -> None:
        ktuple_1 = seq_x.get_ktuple(k)
        ktuple_2 = seq_y.get_ktuple(k)
        res = Dissimilarity._get_Eu(ktuple_1, ktuple_2, seq_x.get_total(k), seq_y.get_total(k))
        key = 'Eu_k{}'.format(k)
        result.add(key, seq_x.id, seq_y.id, res)

    @staticmethod
    @nb.jit('float64(int32[:],int32[:],int32,int32)', nopython=True)
    def _get_Ma(ktuple_1: np.ndarray, ktuple_2: np.ndarray, total_1: int, total_2: int) -> np.float64:
        ktuple_1 = np.divide(ktuple_1, total_1)
        ktuple_2 = np.divide(ktuple_2, total_2)
        res = np.abs(np.subtract(ktuple_1, ktuple_2)).sum()  # type: np.float64
        return res

    @staticmethod
    def get_Ma(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r: int = None) -> None:
        ktuple_1 = seq_x.get_ktuple(k)
        ktuple_2 = seq_y.get_ktuple(k)
        res = Dissimilarity._get_Ma(ktuple_1, ktuple_2, seq_x.get_total(k), seq_y.get_total(k))
        key = 'Ma_k{}'.format(k)
        result.add(key, seq_x.id, seq_y.id, res)

    @staticmethod
    @nb.jit('float64(int32[:],int32[:],int32,int32,float64[:],float64[:])', nopython=True)
    def _get_D2S(ktuple_1: np.ndarray, ktuple_2: np.ndarray, total_1: int, total_2: int, markov_1: np.ndarray,
                 markov_2: np.ndarray) -> np.float64:
        tmp_x = np.subtract(ktuple_1, np.multiply(total_1, markov_1))
        tmp_y = np.subtract(ktuple_2, np.multiply(total_2, markov_2))
        tmp_1 = np.square(tmp_x)
        tmp_2 = np.square(tmp_y)
        tmp = np.sqrt(np.add(tmp_1, tmp_2))
        tmp[tmp == 0] = 1
        res = np.multiply(np.divide(tmp_x, tmp), tmp_y).sum()
        tmp_1 = np.sqrt(np.divide(tmp_1, tmp).sum())
        tmp_2 = np.sqrt(np.divide(tmp_2, tmp).sum())
        res = (1 - res / tmp_1 / tmp_2) * 0.5
        return res

    @staticmethod
    def get_D2S(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r_list: List[int]) -> None:
        for r in r_list:
            if k < r or k < 3:
                continue
            ktuple_1 = seq_x.get_ktuple(k)
            total_1 = seq_x.get_total(k)
            markov_1 = seq_x.get_markov(k, r)

            ktuple_2 = seq_y.get_ktuple(k)
            total_2 = seq_y.get_total(k)
            markov_2 = seq_y.get_markov(k, r)
            res = Dissimilarity._get_D2S(ktuple_1, ktuple_2, total_1, total_2, markov_1, markov_2)
            key = 'D2S_k{}_M{}'.format(k, r)
            result.add(key, seq_x.id, seq_y.id, res)

    @staticmethod
    @nb.jit('float64(int32[:],int32[:],int32,int32,float64[:],float64[:])', nopython=True)
    def _get_D2Star(ktuple_1: np.ndarray, ktuple_2: np.ndarray, total_1: int, total_2: int, markov_1: np.ndarray,
                    markov_2: np.ndarray) -> np.float64:
        tmp_x = np.multiply(total_1, markov_1)
        tmp_y = np.multiply(total_2, markov_2)
        tmp_x_bar = np.subtract(ktuple_1, tmp_x)
        tmp_y_bar = np.subtract(ktuple_2, tmp_y)
        tmp_1 = np.square(tmp_x_bar)
        tmp_2 = np.square(tmp_y_bar)

        tmp = np.multiply(np.sqrt(tmp_x), np.sqrt(tmp_y))
        index = tmp_x == 0
        tmp[index] = 1
        tmp_x[index] = 1
        index = tmp_y == 0
        tmp[index] = 1
        tmp_y[index] = 1
        res = np.multiply(np.divide(tmp_x_bar, tmp), tmp_y_bar).sum()
        tmp_1 = np.sqrt(np.divide(tmp_1, tmp_x).sum())
        tmp_2 = np.sqrt(np.divide(tmp_2, tmp_y).sum())
        res = (1 - res / tmp_1 / tmp_2) * 0.5
        return res

    @staticmethod
    def get_D2Star(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r_list: List[int]) -> None:
        for r in r_list:
            if k < r or k < 3:
                continue
            ktuple_1 = seq_x.get_ktuple(k)
            total_1 = seq_x.get_total(k)
            markov_1 = seq_x.get_markov(k, r)

            ktuple_2 = seq_y.get_ktuple(k)
            total_2 = seq_y.get_total(k)
            markov_2 = seq_y.get_markov(k, r)
            res = Dissimilarity._get_D2Star(ktuple_1, ktuple_2, total_1, total_2, markov_1, markov_2)
            key = 'D2Star_k{}_M{}'.format(k, r)
            result.add(key, seq_x.id, seq_y.id, res)

    @staticmethod
    @nb.jit('float64(int32[:],int32[:],int32,int32,float64[:],float64[:])', nopython=True)
    def _get_Hao(ktuple_1: np.ndarray, ktuple_2: np.ndarray, total_1: int, total_2: int, markov_1: np.ndarray,
                 markov_2: np.ndarray) -> np.float64:
        tmp_x = np.divide(ktuple_1, total_1)
        tmp_y = np.divide(ktuple_2, total_2)
        tmp1 = np.divide(tmp_x, markov_1) - 1
        tmp1[~np.isfinite(tmp1)] = -1
        tmp2 = np.divide(tmp_y, markov_2) - 1
        tmp2[~np.isfinite(tmp2)] = -1
        tmp_xy = np.multiply(tmp1, tmp2).sum()
        tmp_x = np.sqrt(np.square(tmp1).sum())
        tmp_y = np.sqrt(np.square(tmp2).sum())
        return (1 - tmp_xy / tmp_x / tmp_y) * 0.5

    @staticmethod
    def get_Hao(seq_x: SequenceData, seq_y: SequenceData, k: int, result: Result, r: int = None) -> None:
        if k < 2:
            return
        ktuple_1 = seq_x.get_ktuple(k)
        total_1 = seq_x.get_total(k)
        markov_1 = seq_x.get_markov(k, k - 2)

        ktuple_2 = seq_y.get_ktuple(k)
        total_2 = seq_y.get_total(k)
        markov_2 = seq_y.get_markov(k, k - 2)
        res = Dissimilarity._get_Hao(ktuple_1, ktuple_2, total_1, total_2, markov_1, markov_2)
        key = 'Hao_k{}'.format(k)
        result.add(key, seq_x.id, seq_y.id, res)
