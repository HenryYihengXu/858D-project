from posixpath import split
import re
import numpy as np
import pandas as pd
import random
import glob
import subprocess
import sys
import math
import time

def main():
    pass
    parse_lisa_query_output()

def parse_lisa_query_output(path='/nfshomes/yhxu/scratch/858D/858D-project/result/query', human=True):
    dic = {
        'tool': [],
        'refName': [],
        'refLen': [],
        'pufferfishK': [],
        'lisaK': [],
        'lisaLeafNodes': [],
        'queryLen': [],
        'threads': [],
        'queryTime(ms)': [],
        'size(MB)': [],
        'NUM_IPBWT_BYTES': [],
        'ipbwtSize(MB)': [],
        'rmiParamSize(MB)': [],
        'trainingDataSize(MB)': [],
    }

    fileNames = glob.glob(path + '/*')
    fileNames = list(map(lambda x: x.split('/')[-1], fileNames))

    for fileName in fileNames:
        if fileName == 'analyzeLisa.py' or fileName == '':
            continue
        if human and fileName[0:5] != 'Human':
            continue
        configs = fileName.split('.')
        try:
            with open(fileName) as f:
                lines = f.readlines()
                dic['tool'].append('LISA')
                dic['refName'].append(configs[0])
                refLen = int(lines[3].split()[2])
                dic['refLen'].append(refLen)
                dic['pufferfishK'].append(None)
                dic['lisaK'].append(int(configs[1]))
                dic['lisaLeafNodes'].append(int(configs[2]))
                dic['queryLen'].append(int(configs[4]))
                dic['threads'].append(int(configs[3]))
                dic['queryTime(ms)'].append(float(lines[21].split()[2]) * 1000)
                NUM_IPBWT_BYTES = int(lines[7].split()[2])
                dic['NUM_IPBWT_BYTES'].append(NUM_IPBWT_BYTES)
                ipbwtSize = refLen * NUM_IPBWT_BYTES / 1024 / 1024
                dic['ipbwtSize(MB)'].append(ipbwtSize)

                rmiParamFile = lines[12].split()[2][:-2]
                process = subprocess.Popen('du -h ' + rmiParamFile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                out, err = process.communicate()
                rmiParamSize = str(out).split('\\')[0][2:]
                rmiParamSize = toMB(rmiParamSize)
                dic['rmiParamSize(MB)'].append(rmiParamSize)

                rmiParamFile = lines[8].split()[2][:-2]
                process = subprocess.Popen('du -h ' + rmiParamFile + '.f64', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                out, err = process.communicate()
                trainingDataSize = str(out).split('\\')[0][2:]
                trainingDataSize = toMB(trainingDataSize)
                dic['trainingDataSize(MB)'].append(trainingDataSize)

                dic['size(MB)'].append(rmiParamSize + ipbwtSize)

        except ValueError:
            print(fileName)

    for key, value in dic.items():
        print(key + ': ' + str(len(value)))

    data = pd.DataFrame.from_dict(dic)
    if human:
        data.to_csv(path + '/lisa-human-query-result.csv', index=False)
    else:
        data.to_csv(path + '/lisa-query-result.csv', index=False)
    return data

def sortLisa(file='/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/lisa-human-query-result.csv'):
    df = pd.read_csv(file)
    columns = [
        'tool',
        'refLen',
        'lisaK',
        'lisaLeafNodes',
        'queryLen',
        'threads',
    ]
    df.sort_values(by=columns, ascending=True, inplace=True)
    df.to_csv(file, index=False)
    return df
            

def toMB(size):
    unit = size[-1]
    # print(size)
    # print(unit)
    if unit == 'K':
        return float(size[:-1]) / 1024
    elif unit == 'M':
        return float(size[:-1])
    elif unit == 'G':
        return float(size[:-1]) * 1024
    else:
        return float(size) / 1024 / 1024

if __name__ == "__main__":
    pass
    # main()
            
            

