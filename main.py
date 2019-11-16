from Core import Core
import os
from typing import List

dic = dict()


def get_files_path(dir_path: str) -> List[str]:
    return [os.path.join(dir_path, path) for path in os.listdir(dir_path)]


def get_k_list(k_str: str) -> List[int]:
    tmp = k_str.split('-')
    if len(tmp) == 1:
        return [int(tmp[0])]
    elif len(tmp) == 3:
        return list(range(int(tmp[0]), int(tmp[1]) + 1, step=int(tmp[2])))
    else:
        raise ValueError('k should be integer')


def get_dissimilarity_list(diss_str: str) -> List[str]:
    func_lst = ['Ma', 'Ch', 'Eu', 'd2', 'Hao', 'd2S', 'd2Star']
    return [func_lst[int(i)] for i in diss_str.split(',')]


def get_r_list(r_str: str or None) -> List[int]:
    return [int(r_) for r_ in r_str.split(',')] if r_str is not None else None


if __name__ == '__main__':
    dic = dict()
    while True:
        print('Input the directory path of sequences : ')
        path = input()
        dic.setdefault('path', path)
        print('\n\n')
        print('Input the k')
        print('\t1. For single k, input a integer(>0)')
        print(
            "\t2. For a series of k, input kmin-kmax-step. For example(without quotation marks), '2-10-2', it means, [2, 4, 6, 8, 10]")
        print('Input the k : ')
        k = input()
        dic.setdefault('k', k)
        print('\n\n')
        print('Select the dissimilarities')
        print('1. Ma')
        print('2. Ch')
        print('3. Eu')
        print('4. d2')
        print('5. Hao')
        print('6. d2S')
        print('7. d2Star')
        print("For example(without quotation marks), '1,2,3,4'")
        print('Input the dissimilarities : ')
        func = input()
        dic.setdefault('func', func)
        print('\n\n')
        if '6' in func or '7' in func:
            print('Markov possibility order')
            print('For single order, input a interger(>=0)')
            print("For a series of order, separation with ','. For example(without quotation marks), '0, 1, 2, 3'")
            print('Input the possibility order:')
            r = input()
            dic.setdefault('r', r)
        else:
            dic.setdefault('r', None)

        print('\n\n')
        print('dir_path : ' + dic['path'])
        print('k : ' + str(get_k_list(dic['k'])))
        print('Dissimilarities : ' + str(get_dissimilarity_list[dic['func']]))

        print('Input the path you want to save : ')
        save_path = input()
        dic.setdefault('save', save_path)
        if dic['r'] is not None:
            print('Markov possibility order : ' + str(get_r_list(dic['r'])))
        print('\n\n')
        print("Check the parameters : 'yes' or 'no'")
        result = input()
        if result == 'yes':
            Core(get_k_list(dic['k']), get_files_path(dic['path']), get_dissimilarity_list(dic['func']), dic['save'],
                 get_r_list(dic['r'])).star()
        else:
            dic.clear()
