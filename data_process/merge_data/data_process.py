#!/usr/bin/env python
# coding: utf-8

# In[37]:

def wyy():
    with open('dict.txt',mode='r',encoding='utf-8') as f:
        dic=f.readlines()

    with open('corpus.txt',mode='r',encoding='utf-8') as f:
        corp=f.readlines()


    dic=[i.strip('\n') for i in dic]#词表
    corp=[i.strip('\n') for i in corp]#文本

    res=[]

    for c in corp:
        tmp='O'*len(c)#结果
        for d in dic:
            seapos=0
            while c.find(d,seapos)!=-1:#反复搜索c直到找不到d
                pos=c.find(d,seapos)
                seapos=pos+len(d)
                if tmp[pos:pos+len(d)]=='O'*len(d):
                    #print('pass')
                    tmp=tmp[:pos]+'B'+'I'*(len(d)-1)+tmp[pos+len(d):]#标记
        res.append(tmp)

    scale = (8, 1, 1)
    def devide(length, scale):
        sum = scale[0] + scale[1] + scale[2]
        per = [x / sum for x in scale]
        range1 = int(per[0] * length)
        range2 = int(per[1] * length) + range1
        return range1, range2

    def data_devide(df, scale):
        length = len(df)
        print(length)
        range1, range2 = devide(length, scale)
        print(range1, range2)
        train = df[0:range1]
        # print("length train_data:", len(train))
        test = df[range1:range2]
        # print("length test_data:", len(test))
        validation = df[range2:length]
        # print("length valid_data:", len(validation))
        return train, test, validation

    train, test, validation = data_devide(res, scale)

    # [print(t) for t in res]
    data = []
    def write_down(res):
        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j]=='B':
                    # f.write(corp[i][j]+' '+'B-CHEMICAL'+'\n')
                    data.append(corp[i][j]+' '+'B-CHEMICAL')
                elif res[i][j]=='I':
                    # f.write(corp[i][j]+' '+'I-CHEMICAL'+'\n')
                    data.append(corp[i][j] + ' ' + 'I-CHEMICAL')
                else:
                    # f.write(corp[i][j]+' '+'O'+'\n')
                    data.append(corp[i][j] + ' ' + 'O')
            # f.write('\n')
            data.append("")
            return data

    train = write_down(train)
    test = write_down(test)
    validation = write_down(validation)
    return train, test, validation

# data = wyy()
# print(data)
    # In[ ]:




