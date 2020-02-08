# -*- coding: UTF-8 -*-
# @File: main.py
# @Author: htczero
# @Create Data:  2019/11/16
# @Modify Data:  2019/11/16
# @Email: htczero@hotmail.com
from Core import Core
import os
from typing import List, Optional

dic = dict()

def get_k_list(k_str: str) -> Optional[List[int]]:
    try:
        tmp = k_str.split('-')
        if len(tmp) == 1:
            return [int(tmp[0])]
        elif len(tmp) == 3:
            return list(range(int(tmp[0]), int(tmp[1]) + 1, int(tmp[2])))
        else:
            raise ValueError('k should be integer')
    except:
        print('Check your k-inputs please')
        return None


def get_dissimilarity_list(diss_str: str) -> Optional[List[str]]:
    try:
        func_lst = ['Ma', 'Ch', 'Eu', 'd2', 'Hao', 'd2S', 'd2Star']
        return [func_lst[int(i)] for i in diss_str.split(',')]
    except:
        print('Check your dissimilarity-inputs please')
        return None


def get_r_list(r_str: Optional[str]) ->Optional[List[int]]:
    try:
        return [int(r_) for r_ in r_str.split(',')] if r_str is not None else None
    except:
        print('Check your markov-inputs please')
        return None


if __name__ == '__main__':
    dic = dict()
    while True:
        # directory of sequences
        print('Input the directory path of sequences : ')
        path = input()
        dic.setdefault('path', path)
        print('\n\n')
        # endregion

        # k
        print('Input the k')
        print('\t1. For single k, input a integer(>0)')
        print(
            "\t2. For a series of k, input kmin-kmax-step. For example(without quotation marks), '2-10-2', it means, [2, 4, 6, 8, 10]")
        print('Input the k : ')
        k = input()
        dic.setdefault('k', k)
        print('\n\n')
        # endregion

        # dissimilarity
        print('Select the dissimilarities')
        print('0. Ma')
        print('1. Ch')
        print('2. Eu')
        print('3. d2')
        print('4. Hao')
        print('5. d2S')
        print('6. d2Star')
        print("For example(without quotation marks), '1,2,3,4'")
        print('Input the dissimilarities : ')
        func = input()
        dic.setdefault('func', func)
        print('\n\n')
        # endregion

        # region markov
        if '5' in func or '6' in func:
            print('Markov possibility order')
            print('For single order, input a interger(>=0)')
            print("For a series of order, separation with ','. For example(without quotation marks), '0, 1, 2, 3'")
            print('Input the possibility order : ')
            r = input()
            dic.setdefault('r', r)
            print('\n\n')
        else:
            dic.setdefault('r', None)
        # endregion

        # save path
        print('Input the path you want to save : ')
        save_path = input()
        dic.setdefault('save', save_path)
        print('\n\n')
        # endregion

        # region show inputs and conform
        print('dir_path : ' + dic['path'])
        print('k : ' + str(get_k_list(dic['k'])))
        print('Dissimilarities : ' + str(get_dissimilarity_list(dic['func'])))
        print('Save path : ' + dic['save'])

        if dic['r'] is not None:
            print('Markov possibility order : ' + str(get_r_list(dic['r'])))
        print('\n\n')
        print("Check the parameters : 'yes' or 'no'")
        result = input()
        if result == 'yes':
            Core.star(get_k_list(dic['k']), dic['path'], get_dissimilarity_list(dic['func']), dic['save'],
                 get_r_list(dic['r']))
        else:
            dic.clear()
        # endregion

        print('Want to exit?(yes/no)')
        if input() == 'yes':
            exit(0)
