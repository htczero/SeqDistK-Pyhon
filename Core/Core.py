from concurrent.futures import ThreadPoolExecutor
from typing import List
from Data import SequenceData
from Data import Result
from Dissimilarity import Dissimilarity
from tqdm import tqdm


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

    def star(self):
        names =  [seq.name for seq in self._seq_list]
        for i in tqdm(range(len(self._seq_list) - 1)):  # type: int
            self.one_to_all(self._seq_list[i], self._seq_list[i + 1:])
            self._seq_list[i] = None
        self._result.save_to_file(self._save_dir, names)

    def one_to_all(self, one: SequenceData, others: List[SequenceData]):
        for seq in tqdm(others):
            [func(one, seq, k, self._result, self._markov_list) for k in self._k_list for func in self._dissimilarity]

    def _clear(self, k: int, r: int = None):
        if 'd2S' in self._dissimilarity_names or 'd2Star' in self._dissimilarity_names:
            if k in self._markov_list:
                return
        if 'Hao' in self._dissimilarity_names:
            k -= 3
        for seq in self._seq_list:
            seq.clear(k)
