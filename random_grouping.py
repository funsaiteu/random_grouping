#!/Users/saito/.pyenv/shims/python
# -*- coding:utf-8 -*-


'''
Last modified: Sat, 05 Jun 2021 17:56:10 +0900
author: Takaya Saito
github: funsaiteu
Sorry for the dirty hack.
'''


import argparse
import pathlib
import random
import numpy as np


def main():
    parser = argparse.ArgumentParser(description='for online party(e.g. % ./random_grouping.py -n 3 -m ./member -r 0)')
    parser.add_argument('-n', type=int, default='3', help="number of split u wanna(default='3')")
    parser.add_argument('-m', default='./member', help="member list's path(default='./member')")
    parser.add_argument('-r', type=int, default='0', help="random seed(default='0')")
    args = parser.parse_args()
    N = args.n
    path = pathlib.Path(args.m)
    seed = args.r
    with path.open() as f:
        member_list = [s.strip() for s in f.readlines()]
    random.seed(seed)
    member_list_random = random.sample(member_list, len(member_list))
    for i, name in enumerate(np.array_split(member_list_random, N)):
        print(f'group{i}: {name}')


if __name__ == '__main__':
    main()

