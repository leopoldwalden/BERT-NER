import argparse
import os
import shutil
from ner_label import *
from split_single_label import select_singel_label
from data_process import wyy
import pandas as pd
import pysnooper
import tqdm
from tqdm import tqdm
from random import shuffle
from tqdm._tqdm import trange

# parser = argparse.ArgumentParser()
# parser.add_argument("--data_cut" , default = "False", required=True)
# parser.add_argument("--data_size", default=120, type=int, required=False)
# args = parser.parse_args()

# @pysnooper.snoop()
def devide(length, scale):
    sum = scale[0]+scale[1]+scale[2]
    per = [x/sum for x in scale]
    range1 = int(per[0] * length)
    range2 = int(per[1] * length) + range1
    return range1,range2

def data_devide(df,scale):
    length = len(df)
    print(length)
    range1, range2 = devide(length, scale)
    print(range1,range2)
    train = df[0:range1]
    # print("length train_data:", len(train))
    test = df[range1:range2]
    # print("length test_data:", len(test))
    validation = df[range2:length]
    # print("length valid_data:", len(validation))
    return train, test, validation

def process(data_list, name):
    root = os.getcwd()
    tmp_list = []
    data = []
    for line in data_list:
        # print(line)
        if line != "":
            tmp_list.append(line)
        else:
            data.append(tmp_list)
            tmp_list =[]
    shuffle(data)
    # print(len(data))

    path = '/train_data/' + name + '.txt'
    name = root + path
    length = 0
    with open(name, 'w+') as f:
        # print(data,file = f)
        for line in data:
            for cha in line:
                print(cha, file = f)
            print("", file = f)
            length += 1
    return length

def fjl_process(data_list, name):
    name = './train_data/' + name + '.txt'
    length = 0
    data = []
    if True:
    # with open(name, 'w+') as f:
    #     print("-DOCSTART- O\n",file = f)
        # print(data_list.__class__)
        for line in tqdm(data_list):
            if tag(line) != []:
                out = tag(line)
                for element in out:
                    # print(element[0]+" "+element[1], file = f)
                    line = str(element[0]) + " " + str(element[1])
                    data.append(line.strip("\n"))
                data.append("")
                # print('', file = f)
                length +=1
    # f.close()
    return length, data

def wyy_process(data_list, name):
    name = './train_data/' + name + '.txt'
    length = 0
    data =[]
    if True:
        for line in tqdm(data_list):
            data.append(line.strip("\n"))
            length +=1
    return length, data

def mjz_process(file_name, name):
    name = './train_data/' + name + '.txt'
    length = 0
    data = []
    with open(file_name, "r") as f1:
        for line in tqdm(f1):
            data.append(line.strip("\n"))
            length += 1
    f1.close()
    return length, data


if __name__ == '__main__':
    root = os.getcwd()
    print(root)
    # root = "~/PycharmProjects/BERT_NER"
    path = "/regex_test.xlsx"

    # print("args.data_cut:",args.data_cut)

    data = pd.read_excel(root + path)
    wyy_train, wyy_test, wyy_validation = wyy()
    # print(data)
    data = select_singel_label(data)
    shuffle(data)
    # print(len(data))

    # if args.data_cut == True:
    #     print("args.data_size:",args.data_size)
    #     data = data[:args.data_size]

    # df = pd.read_csv(path)

    scale = (8, 1, 1)
    fjl_train, fjl_test, fjl_validation = data_devide(data, scale)

    if os.path.isdir(root+"/train_data"):
        shutil.rmtree(root + "/train_data/")
    os.mkdir(root + "/train_data")

    name = "train"
    fjl_train_data_length, fjl_train_data = fjl_process(fjl_train, name)
    # mjz_train_data_length, mjz_train_data = mjz_process("example.train", name)
    wyy_train_data_length, wyy_train_data = wyy_process(wyy_train, name)
    train_data = fjl_train_data + wyy_train_data # + mjz_train_data
    # print("train_data:", len(train_data))
    # shuffle(train_data)
    train_data_length = process(train_data, name)

    name = "test"
    fjl_test_data_length, fjl_test_data = fjl_process(fjl_test, name)
    # mjz_test_data_length, mjz_test_data = mjz_process("example.test", name)
    wyy_test_data_length, wyy_test_data = wyy_process(wyy_test, name)
    test_data = fjl_test_data + wyy_test_data #  + mjz_test_data
    # shuffle(test_data)
    test_data_length = process(test_data, name)


    name = "dev"
    fjl_dev_data_length, fjl_dev_data = fjl_process(fjl_validation, name)
    # mjz_dev_data_length, mjz_dev_data = mjz_process("example.dev", name)
    wyy_dev_data_length, wyy_dev_data = wyy_process(wyy_validation, name)
    dev_data = fjl_dev_data + wyy_dev_data #  + mjz_dev_data
    # shuffle(dev_data)
    dev_data_length = process(dev_data, name)

    print(len(wyy_train_data))
    # print(len(mjz_train_data))
    print(len(fjl_train_data))



    print("length train_data:", train_data_length)
    print("length test_data:", test_data_length)
    print("length dev_data:", dev_data_length)

    #
    # print(len(train_data))
    # print(len(test_data))
    # print(len(validation_data))


    # data = process(data, name = "dump")
    # print(data)
