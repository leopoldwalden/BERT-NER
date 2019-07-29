#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import random
import re

def mjz_data():
    df = pd.read_csv('a_drug_data.csv')

    def get_ner(txt, patterns, typs):
        lab = ['O']*len(txt)
        for i in range(len(patterns)):
            for match in re.finditer(patterns[i], txt):
                start, end = match.span()
                lab[start:end] = ['B-{}'.format(typs[i])] + ['I-{}'.format(typs[i])] * (end-start-1)
        return '\n'.join(['{} {}'.format(i,j) for i, j in zip(txt, lab)])

    medicine = pd.read_csv('a_drug_index.csv')
    medicine_list = np.unique([key for key in medicine['名称']])
    med_re = '|'.join(medicine_list)

    for i in range(len(df)):
        if df.loc[i,'内容'] != df.loc[i,'内容']:
            continue
        txts = re.split('。|\s+', df.loc[i,'内容'])
        for t in txts:
            t = re.sub('\s','',t)
            if t == '' or not re.search(med_re, t):
                continue
            add = get_ner(t, [med_re], ['DRUG']) + '\n\n'

            # if random.random() < 0.1:
            #     test = open('medical_data/test_data_drug.txt', 'a')
            #     test.write(add)
            #     test.close()
            # else:
            #     train = open('medical_data/train_data_drug.txt', 'a')
            #     train.write(add)
            #     train.close()
    add = add.split("\n")
    return add
data = mjz_data()
print(data.__class__)
for line in data:
    print(data)



