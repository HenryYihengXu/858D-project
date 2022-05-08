import sys
import os
import numpy as np
import pandas as pd
import random
import glob
import subprocess
import sys
import math
import time

refs = [
        "Chlamydia",
        "Coxiella",
        "Caulobacter",
        "Ecoli",
        "Pseudomonas",
    ]

def main():
    buildLisa()

def buildLisa():
    for k in [4, 8, 12, 16, 20, 24, 28, 32]:
        for numLeafNode in [2**10, 2**15, 2**20, 2**25]:
            for ref in refs:
                command = '/nfshomes/yhxu/scratch/858D/Trans-Omics-Acceleration-Library/LISA/build-index-forward-only-lisa.o'
                command += ' /nfshomes/yhxu/scratch/858D/data/fasta/' + ref + '.fasta ' 
                command += str(k) + ' ' + str(numLeafNode)
                command += ' &> /nfshomes/yhxu/scratch/858D/result/build/' + ref + '.' + str(k) + '.' + str(numLeafNode)
                subprocess.run(command, shell=True)

def runLisa():
    subprocess.run('export OMP_NUM_THREADS=16', shell=True)
    for k in [4, 8, 16]:
        for numLeafNode in [2**10, 2**15, 2**20, 2**25]:
            for numThreads in [1,2,4,8,16]:
                for ref in refs:
                    for queryLen in [32, 64, 96, 128]:
                        command = '/nfshomes/yhxu/scratch/858D/Trans-Omics-Acceleration-Library/LISA/exact-search-lisa.o'
                        command += ' /nfshomes/yhxu/scratch/858D/data/fasta/' + ref + '.fasta' 
                        command += ' /nfshomes/yhxu/scratch/858D/data/query/' + ref + '.' + str(queryLen) + 'query '
                        command += str(k) + ' ' + str(numLeafNode) + ' ' + str(numThreads)
                        command += ' &> /nfshomes/yhxu/scratch/858D/result/query/'
                        command += ref + '.' + str(k) + '.' + str(numLeafNode) + '.' + str(numThreads) + '.' + str(queryLen)
                        subprocess.run(command, shell=True)
                    pass
                    
if __name__ == "__main__":
    pass
    main()
