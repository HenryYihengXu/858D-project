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

prokaryotics = [
        "Chlamydia",
        "Coxiella",
        "Caulobacter",
        "Ecoli",
        "Pseudomonas",
    ]

human = [
        "Human18",
        "Human19",
        "Human20",
        "Human21",
        "Human22",
    ]

def main():
    pass
    runLisaProkaryotics()

def buildLisaProkaryotics():
    for k in [4, 8, 16]:
        for numLeafNode in [2**8, 2**10, 2**12, 2**14, 2**16, 2**18, 2**22, 2**20, 2**24, 2**26]:
            for ref in prokaryotics:
                command = '/nfshomes/yhxu/scratch/858D/Trans-Omics-Acceleration-Library/LISA/build-index-forward-only-lisa.o'
                command += ' /nfshomes/yhxu/scratch/858D/data/fasta/' + ref + '.fasta ' 
                command += str(k) + ' ' + str(numLeafNode)
                command += ' &> /nfshomes/yhxu/scratch/858D/858D-project/result/build/' + ref + '.' + str(k) + '.' + str(numLeafNode)
                subprocess.run(command, shell=True)

def buildLisaHuman():
    for k in [16]:
        for numLeafNode in [2**20]:
            for ref in human:
                command = '/nfshomes/yhxu/scratch/858D/Trans-Omics-Acceleration-Library/LISA/build-index-forward-only-lisa.o'
                command += ' /nfshomes/yhxu/scratch/858D/858D-project/data/fasta/' + ref + '.fasta ' 
                command += str(k) + ' ' + str(numLeafNode)
                command += ' &> /nfshomes/yhxu/scratch/858D/858D-project/result/build/' + ref + '.' + str(k) + '.' + str(numLeafNode)
                subprocess.run(command, shell=True)


def runLisaProkaryotics():
    subprocess.run('export OMP_NUM_THREADS=16', shell=True)
    for k in [4, 8, 16]:
        for numLeafNode in [2**8, 2**10, 2**12, 2**14, 2**16, 2**18, 2**20, 2**22, 2**24, 2**26]:
            for numThreads in [1,2,4,8,16]:
                for ref in prokaryotics:
                    for queryLen in [32, 64, 96, 128]:
                        command = '/nfshomes/yhxu/scratch/858D/Trans-Omics-Acceleration-Library/LISA/exact-search-lisa.o'
                        command += ' /nfshomes/yhxu/scratch/858D/data/fasta/' + ref + '.fasta' 
                        command += ' /nfshomes/yhxu/scratch/858D/data/query/' + ref + '.' + str(queryLen) + '.query '
                        command += str(k) + ' ' + str(numLeafNode) + ' ' + str(numThreads)
                        command += ' &> /nfshomes/yhxu/scratch/858D/858D-project/result/query/'
                        command += ref + '.' + str(k) + '.' + str(numLeafNode) + '.' + str(numThreads) + '.' + str(queryLen)
                        subprocess.run(command, shell=True)
                    pass

def runLisaHuman():
    subprocess.run('export OMP_NUM_THREADS=16', shell=True)
    for k in [16]:
        for numLeafNode in [2**20]:
            for numThreads in [1]:
                for ref in human:
                    for queryLen in [32, 64, 96, 128]:
                        command = '/nfshomes/yhxu/scratch/858D/Trans-Omics-Acceleration-Library/LISA/exact-search-lisa.o'
                        command += ' /nfshomes/yhxu/scratch/858D/858D-project/data/fasta/' + ref + '.fasta' 
                        command += ' /nfshomes/yhxu/scratch/858D/858D-project/data/query/' + ref + '.' + str(queryLen) + '.query '
                        command += str(k) + ' ' + str(numLeafNode) + ' ' + str(numThreads)
                        command += ' &> /nfshomes/yhxu/scratch/858D/858D-project/result/query/'
                        command += ref + '.' + str(k) + '.' + str(numLeafNode) + '.' + str(numThreads) + '.' + str(queryLen)
                        subprocess.run(command, shell=True)
                    pass
                    
if __name__ == "__main__":
    pass
    main()
