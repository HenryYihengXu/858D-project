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

def plot_both():
    pufferfish = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/pufferfish-query-result.csv")
    pufferfish = pufferfish[pufferfish['refName'].str.contains('Human')].copy()
    lisa = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/lisa-human-query-result.csv")
    
    df = pd.concat([pufferfish, lisa])

    df1 = df[df['queryLen'] == 32].copy()
        
    plt.figure()
    sns.lineplot(x='refLen', y='queryTime(ms)', hue='tool', data=df1, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('reference lenght')
    plt.ylabel('time of 10000 queries (ms)')
    plt.xticks(list(df1['refLen']))
    plt.title('query time versus reference length')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/time-refLen-tool.pdf', bbox_inches="tight")

    plt.figure()
    sns.lineplot(x='refLen', y='size(MB)', hue='tool', data=df1, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('reference lenght')
    plt.ylabel('Main components size (ms)')
    plt.xticks(list(df1['refLen']))
    plt.title('Main components size versus reference length')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/size-refLen-tool.pdf', bbox_inches="tight")

    plt.figure()
    f, axs = plt.subplots(1,2,
                      figsize=(10,3),
                      sharey=True)
    sns.lineplot(x='refLen', y='queryTime(ms)', hue='queryLen', data=pufferfish, ax=axs[0], marker="o", dashes=False, legend=False)
    sns.lineplot(x='refLen', y='queryTime(ms)', hue='queryLen', data=lisa, ax=axs[1], marker="o", dashes=False)
    axs[0].set(xlabel='Pufferfish query time (ms)')
    axs[1].set(xlabel='LISA query time (ms)')
    axs[0].set(xticks=list(pufferfish['refLen']))
    axs[1].set(xticks=list(lisa['refLen']))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/time-refLen.pdf', bbox_inches="tight")

    plt.figure()
    f, axs = plt.subplots(1,2,
                      figsize=(10,3),
                      sharey=True)
    sns.lineplot(x='refLen', y='size(MB)', hue='queryLen', data=pufferfish, ax=axs[0], marker="o", dashes=False, legend=False)
    sns.lineplot(x='refLen', y='size(MB)', hue='queryLen', data=lisa, ax=axs[1], marker="o", dashes=False)
    axs[0].set(xlabel='Pufferfish main components size (MB)')
    axs[1].set(xlabel='LISA main components size (MB)')
    axs[0].set(xticks=list(pufferfish['refLen']))
    axs[1].set(xticks=list(lisa['refLen']))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/figs/size-refLen.pdf', bbox_inches="tight")
