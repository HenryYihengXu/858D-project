#!/usr/bin/env python3

import sys
import os
import subprocess

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

def main(argv):
    pass
    if argv == "build":
        buildPufferfishProkaryotics()
        buildPufferfishHuman()
    elif argv == "query":
        runPufferfishProkaryotics()
        runPufferfishHuman()
    else:
        print("not a valid command")


def buildPufferfishProkaryotics():
    for ref in prokaryotics:
        command = '../build/src/pufferfish index -r data/fasta/' + ref + '.fasta -o ' + ref + '/' + ref + '_pi > buildIndex_output/' + ref + '.index_output'
        subprocess.run(command, shell=True)


def buildPufferfishHuman():
    for ref in human:
        command = '../build/src/pufferfish index -r data/fasta/' + ref + '.fasta -o ' + ref + '/' + ref + '_pi > ./buildIndex_output/' + ref + '.index_output'
        subprocess.run(command, shell=True)


def runPufferfishProkaryotics():
    for numThreads in [1]:
        for ref in prokaryotics:
            for queryLen in [32, 64, 96, 128]:
                command = '../build/src/pufferfish kquery -i ' + ref + '/' + ref + '_pi -p ' + str(numThreads) + ' -q data/query/' + ref + '.' + str(queryLen) + '.query > ./queryTime_output/' + ref + '.' + str(queryLen) + '.time' 
                subprocess.run(command, shell=True)
                pass
    for numThreads in [1]:
        for ref in prokaryotics:
            for queryLen in [32, 64, 96, 128]:
                command = 'python3 pufferfish_calculateTime.py queryTime_output/' + ref + '.' + str(queryLen) + '.time'   
                subprocess.run(command, shell=True)
                pass

def runPufferfishHuman():
    for numThreads in [1]:
        for ref in human:
            for queryLen in [32, 64, 96, 128]:
                command = '../build/src/pufferfish kquery -i ' + ref + '/' + ref + '_pi -p ' + str(numThreads) + ' -q data/query/' + ref + '.' + str(queryLen) + '.query > ./queryTime_output/' + ref + '.' + str(queryLen) + '.time' 
                subprocess.run(command, shell=True)
                pass
    for numThreads in [1]:
        for ref in human:
            for queryLen in [32, 64, 96, 128]:
                command = 'python3 pufferfish_calculateTime.py queryTime_output/' + ref + '.' + str(queryLen) + '.time'   
                subprocess.run(command, shell=True)
                pass
                    
if __name__ == "__main__":
    pass
    main(sys.argv[1])
