import numpy as np
import numba as nb
from .KtupleData import KtupleData
from .MarkovData import MarkovData
import os


class SequenceData:
    Valid_Char = ['A', 'G', 'C', 'T', 'U', 'R', 'Y', 'K', 'M', 'S', 'W', 'B', 'D', 'H', 'V', 'N', 'X', '-']

    def __init__(self, file_path: str, seq_id: int):
        self._ktuple = KtupleData()
        self._markov = MarkovData()
        self._id = seq_id  # type: int
        self._seq = self._load_sequence(file_path)  # type: np.ndarray
        self._seq_length = len(self._seq)
        self._name = os.path.splitext(os.path.split(file_path)[-1])[0]

    @property
    def sequence(self):
        return self._seq

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @staticmethod
    def _load_sequence(file_path: str) -> np.ndarray:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        lst = np.concatenate(
            [np.array(line.strip('\n'), 'c') for line in lines if line[0] in SequenceData.Valid_Char])

        return SequenceData._convert(lst.view(np.uint8))

    @staticmethod
    @nb.jit('uint8[:](uint8[:])', nopython=True, fastmath=True)
    def _convert(char_list) -> np.ndarray:
        seq = np.zeros(len(char_list), dtype=np.uint8)
        for i, char in enumerate(char_list):
            if char == 65:  # A : 1
                seq[i] = 0
            elif char == 71:  # G : 1
                seq[i] = 1
            elif char == 67:  # C : 2
                seq[i] = 2
            elif char in [84, 85]:  # T U : 3
                seq[i] = 3
            elif char == 82:  # R -> G, A
                seq[i] = np.random.choice(np.array([0, 1], dtype=np.uint8))
            elif char == 89:  # Y -> T, C
                seq[i] = np.random.choice(np.array([2, 3], dtype=np.uint8))
            elif char == 75:  # K -> G, T
                seq[i] = np.random.choice(np.array([1, 3], dtype=np.uint8))
            elif char == 77:  # M -> A, C
                seq[i] = np.random.choice(np.array([0, 2], dtype=np.uint8))
            elif char == 83:  # S -> G, C
                seq[i] = np.random.choice(np.array([1, 2], dtype=np.uint8))
            elif char == 87:  # W -> A, T
                seq[i] = np.random.choice(np.array([0, 3], dtype=np.uint8))
            elif char == 66:  # B -> G, T, C
                seq[i] = np.random.choice(np.array([1, 2, 3], dtype=np.uint8))
            elif char == 68:  # D -> A, T
                seq[i] = np.random.choice(np.array([0, 1, 3], dtype=np.uint8))
            elif char == 72:  # H -> A, C, T
                seq[i] = np.random.choice(np.array([0, 2, 3], dtype=np.uint8))
            elif char == 86:  # V -> G, C, A
                seq[i] = np.random.choice(np.array([0, 1, 2], dtype=np.uint8))
            else:  # N, -, X -> A, G, C, T
                seq[i] = np.random.choice(np.array([0, 1, 2, 3], dtype=np.uint8))

        return seq

    def get_ktuple(self, k: int) -> np.ndarray:
        return self._ktuple.get_ktuple(self.sequence, k)

    def get_total(self, k: int) -> int:
        return self._seq_length - k + 1

    def get_markov(self, k: int, r: int) -> np.ndarray:
        if r == 0:
            ktuple_1 = np.zeros(1, dtype=np.int32)
            total_1 = self._seq_length
        else:
            ktuple_1 = self.get_ktuple(r)
            total_1 = self.get_total(r)
        ktuple_2 = self.get_ktuple(r + 1)
        return self._markov.get_markov_possibility(k, r, total_1, ktuple_1, ktuple_2)

    def clear(self, k: int, r: int = None):
        self._ktuple.clear(k)
        self._markov.clear(k)
        if r is not None:
            self._markov.clear_tmp()
