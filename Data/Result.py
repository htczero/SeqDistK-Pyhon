from typing import Dict, List
import numpy as np
import os
from multiprocessing import Lock
from queue import Queue


class Result:
    def __init__(self, size: int):
        self._dic_result = dict()
        self._size = size
        self._lock = Lock()  # type: Lock

    def add(self, key: str, idx: int, idy: int, result: float):
        with self._lock:
            self._dic_result.setdefault(key, np.zeros((self._size, self._size), dtype=np.float64))
            self._dic_result[key][idx][idy] = result
            self._dic_result[key][idy][idx] = result

    def save_to_file(self, save_dir: str, name_list: List[str]):
        head = 'name/name'
        for name in name_list:
            head += ',' + name
        for key, matrix in self._dic_result.items():
            path = os.path.join(save_dir, key + '.csv')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(head + '\n')
                for i in range(self._size):
                    row = name_list[i]
                    for j in range(self._size):
                        row += ',' + str(matrix[i, j])
                    f.write(row + '\n')
