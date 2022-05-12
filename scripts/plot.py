import sys
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_k():
    df = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/lisa-prokaryotics-query-result.csv")
    df = df[df['threads'] == 1].copy()
    
    df1 = df[(df['lisaLeafNodes'] == 16384) & (df['queryLen'] == 64)].copy()

    plt.figure()
    sns.lineplot(x='lisaK', y='queryTime(ms)', hue='refName', data=df1, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA k')
    plt.ylabel('time of 10000 queries (ms)')
    plt.xticks(list(df['lisaK']))
    plt.title('query time versus LISA k')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-time-k-ref.pdf', bbox_inches="tight")

    plt.figure()
    ax = plt.subplot(111)
    sns.lineplot(x='lisaK', y='ipbwtSize(MB)', hue='refName', data=df1, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA k')
    plt.ylabel('IPBWT size (MB)')
    plt.xticks(list(df['lisaK']))
    plt.title('IPBWT size versus LISA k')
    ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-size-k-ref.pdf', bbox_inches="tight")

    df2 = df[(df['lisaLeafNodes'] == 16384) & (df['refName'] == 'Ecoli')].copy()
    
    plt.figure()
    sns.lineplot(x='lisaK', y='queryTime(ms)', hue='queryLen', data=df2, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA k')
    plt.ylabel('time of 10000 queries (ms)')
    plt.xticks(list(df['lisaK']))
    plt.title('query time versus LISA k')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-time-k-queryLen.pdf', bbox_inches="tight")

    plt.figure()
    ax = plt.subplot(111)
    sns.lineplot(x='lisaK', y='ipbwtSize(MB)', hue='queryLen', data=df2, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA k')
    plt.ylabel('IPBWT size (MB)')
    plt.xticks(list(df['lisaK']))
    plt.title('IPBWT size versus LISA k')
    ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-size-k-queryLen.pdf', bbox_inches="tight")

def plot_rmi():
    df = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/lisa-prokaryotics-query-result.csv")
    df = df[df['threads'] == 1].copy()
    
    df1 = df[(df['lisaK'] == 16) & (df['queryLen'] == 64)].copy()
    
    plt.figure()
    ax = plt.subplot(111)
    sns.lineplot(x='lisaLeafNodes', y='queryTime(ms)', hue='refName', data=df1, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA RMI leaf nodes')
    plt.ylabel('time of 10000 queries (ms)')
    ax.set_xscale('log', base=2)
    plt.xticks(list(df['lisaLeafNodes']))
    plt.title('query time versus LISA RMI leaf nodes')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-time-rmi-ref.pdf', bbox_inches="tight")

    plt.figure()
    ax = plt.subplot(111)
    sns.lineplot(x='lisaLeafNodes', y='rmiParamSize(MB)', hue='refName', data=df1, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA k')
    plt.ylabel('RMI model size (MB)')
    ax.set_xscale('log', base=2)
    plt.xticks(list(df['lisaLeafNodes']))
    plt.title('RMI model size versus LISA RMI leaf nodes')
    # ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-size-rmi-ref.pdf', bbox_inches="tight")

    df2 = df[(df['lisaK'] == 16) & (df['refName'] == 'Ecoli')].copy()
    
    plt.figure()
    ax = plt.subplot(111)
    sns.lineplot(x='lisaLeafNodes', y='queryTime(ms)', hue='queryLen', data=df2, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA RMI leaf nodes')
    plt.ylabel('time of 10000 queries (ms)')
    ax.set_xscale('log', base=2)
    plt.xticks(list(df['lisaLeafNodes']))
    plt.title('query time versus LISA RMI leaf nodes')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-time-rmi-queryLen.pdf', bbox_inches="tight")

    plt.figure()
    ax = plt.subplot(111)
    sns.lineplot(x='lisaLeafNodes', y='rmiParamSize(MB)', hue='queryLen', data=df2, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('LISA k')
    plt.ylabel('RMI model size (MB)')
    ax.set_xscale('log', base=2)
    plt.xticks(list(df['lisaLeafNodes']))
    plt.title('RMI model size versus LISA RMI leaf nodes')
    # ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/lisa-size-rmi-queryLen.pdf', bbox_inches="tight")

    # plt.figure()
    # sns.lineplot(x='size(MB)', y='serial-size(MB)', data=df, marker="o", dashes=False)
    # # plt.ticklabel_format(style='plain')
    # plt.xlabel('reference size (MB)')
    # plt.ylabel('size of serialized suffix array (MB)')
    # plt.xticks(list(df['size(MB)']))
    # for x, y in zip(df['size(MB)'], df['serial-size(MB)']):
    #     plt.text(x, y, y)
    # plt.title('reference size versus size of the serialized corresponding suffix array')
    # plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_buildsa_size_k0.pdf', bbox_inches="tight")
