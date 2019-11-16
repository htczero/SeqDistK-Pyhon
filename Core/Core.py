# -*- coding: UTF-8 -*-
# @File: Core.py
# @Author: htczero
# @Create Data:  2019/11/16
# @Modify Data:  2019/11/16
# @Email: htczero@hotmail.com
from typing import List, Callable
from Data import SequenceData
from Data import Result
from Dissimilarity import Dissimilarity
from tqdm import tqdm
import os


class Core:
    _DIC_FUNC = {
        'd2': Dissimilarity.get_D2,
        'Ch': Dissimilarity.get_Ch,
        'Eu': Dissimilarity.get_Eu,
        'Ma': Dissimilarity.get_Ma,
        'd2S': Dissimilarity.get_D2S,
        'd2Star': Dissimilarity.get_D2Star,
        'Hao': Dissimilarity.get_Hao
    }

    def __init__(self, k_list: List[int], seq_file_list: List[str], dissimilirary_list: List[str],
                 save_dir: str, markov_list: List[int] = None):
        self._k_list = k_list
        self._seq_list = [SequenceData(seq_file_list[i], i) for i in range(len(seq_file_list))]
        self._dissimilarity = [self._DIC_FUNC[name] for name in dissimilirary_list]
        self._markov_list = markov_list
        self._dissimilarity_names = dissimilirary_list
        self._result = Result(len(seq_file_list))
        self._save_dir = save_dir

    def n_to_n(self):
        names = [seq.name for seq in self._seq_list]
        for i in tqdm(range(len(self._seq_list) - 1)):  # type: int
            self.one_to_n(self._seq_list[i], self._seq_list[i + 1:])
            self._seq_list[i] = None
        self._result.save_to_file(self._save_dir, names)

    def one_to_n(self, one: SequenceData, others: List[SequenceData]):
        for seq in others:
            Core._one_to_one(one, seq, self._k_list, self._dissimilarity, self._result, self._markov_list)

    @staticmethod
    def _one_to_one(seq_x: SequenceData, seq_y: SequenceData, k_list: List[int], func_list: List[Callable],
                    result: Result, markov_list: List[int]):
        for k in k_list:
            [func(seq_x, seq_y, k, result, markov_list) for func in func_list]

    def _clear(self, k: int, r: int = None):
        if 'd2S' in self._dissimilarity_names or 'd2Star' in self._dissimilarity_names:
            if k in self._markov_list:
                return
        if 'Hao' in self._dissimilarity_names:
            k -= 3
        for seq in self._seq_list:
            seq.clear(k)

    @staticmethod
    def star(k_list: List[int], seq_dir_list: str, dissimilirary_list: List[str],
             save_dir: str, markov_list: List[int] = None):
        dirs = Core.recurrence_load(seq_dir_list)
        for dir_ in dirs:
            name = os.path.split(dir_)[-1]
            print('{} start.................'.format(name))
            seq_file_list = Core.get_file_path(dir_)
            save = os.path.join(save_dir, name)
            os.makedirs(save) if not os.path.exists(save) else None
            Core(k_list, seq_file_list, dissimilirary_list, save, markov_list).n_to_n()

    @staticmethod
    def recurrence_load(dir_path: str):
        dirs = []

        def _rec_load(path: str):
            tmps = os.listdir(path)
            p = os.path.join(path, tmps[0])
            if os.path.isfile(p):
                dirs.append(path)
            elif os.path.isdir(p):
                [_rec_load(os.path.join(path, sub_path)) for sub_path in tmps]
            else:
                return

        _rec_load(dir_path)
        return dirs

    @staticmethod
    def get_file_path(dir_path: str) -> List[str]:
        tmps = os.listdir(dir_path)
        return [os.path.join(dir_path, sub_path) for sub_path in tmps]
