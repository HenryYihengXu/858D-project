import sys
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_k():
    df = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/lisa-query-result.csv")
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
    df = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/project/858D-project/result/lisa-query-result.csv")
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


def plot_querysa():
    df = pd.read_csv("/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/data/evaluate_querysa.csv")
    
    dfq64k0Naive = df[(df['k'] == 0) & (df['queryLength'] == 64) & (df['mode'] == 'naive')].copy()
    plt.figure()
    sns.lineplot(x='size(MB)', y='time(s)', data=dfq64k0Naive, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('reference size (MB)')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfq64k0Naive['size(MB)']))
    for x, y in zip(dfq64k0Naive['size(MB)'], dfq64k0Naive['time(s)']):
        plt.text(x, y, y)
    plt.title('reference size versus the time requried to do 1000 naive queries of length 64 without preftab')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_q64_k0_naive.pdf', bbox_inches="tight")

    dfk0Naive = df[(df['k'] == 0) & (df['mode'] == 'naive')].copy()
    plt.figure()
    sns.lineplot(x='size(MB)', y='time(s)', hue='queryLength', data=dfk0Naive, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('reference size (MB)')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfk0Naive['size(MB)']))
    plt.title('reference size versus the time requried to do 1000 naive queries without preftab')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_k0_naive.pdf', bbox_inches="tight")

    dfq128k0 = df[(df['k'] == 0) & (df['queryLength'] == 128)].copy()
    plt.figure()
    sns.lineplot(x='size(MB)', y='time(s)', hue='mode', data=dfq128k0, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('reference size (MB)')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfq128k0['size(MB)']))
    plt.title('reference size versus the time requried to do 1000 queries of length 128 without preftab')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_q128_k0.pdf', bbox_inches="tight")

    dfr64k0 = df[(df['k'] == 0) & (df['name'] == 'Pseudomonas')].copy()
    plt.figure()
    sns.lineplot(x='queryLength', y='time(s)', hue='mode', data=dfr64k0, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('queryLength')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfr64k0['queryLength']))
    plt.title('reference size versus the time requried to do 1000 queries on Pseudomonas without preftab')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_Pseudomonas_k0.pdf', bbox_inches="tight")

    dfq128k31 = df[(df['k'] == 31) & (df['queryLength'] == 128)].copy()
    plt.figure()
    sns.lineplot(x='size(MB)', y='time(s)', hue='mode', data=dfq128k31, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('reference size (MB)')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfq128k31['size(MB)']))
    plt.title('reference size versus the time requried to do 1000 queries of length 128 with preftab k = 31')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_q128_k31.pdf', bbox_inches="tight")

    dfr64k31 = df[(df['k'] == 31) & (df['name'] == 'Pseudomonas')].copy()
    plt.figure()
    sns.lineplot(x='queryLength', y='time(s)', hue='mode', data=dfr64k31, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('queryLength')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfr64k31['queryLength']))
    plt.title('reference size versus the time requried to do 1000 queries on Pseudomonas with preftab k = 31')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_Pseudomonas_k31.pdf', bbox_inches="tight")

    #
    #
    #
    #

    dfk0Naive = df[(df['k'] == 0) & (df['mode'] == 'naive')].copy()
    dfk0Simpaccel = df[(df['k'] == 0) & (df['mode'] == 'simpaccel')].copy()
    plt.figure()
    f, axs = plt.subplots(1,2,
                      figsize=(10,3),
                      sharey=True)
    sns.lineplot(x='size(MB)', y='time(s)', hue='queryLength', data=dfk0Naive, ax=axs[0], marker="o", dashes=False, legend=False)
    sns.lineplot(x='size(MB)', y='time(s)', hue='queryLength', data=dfk0Simpaccel, ax=axs[1], marker="o", dashes=False)
    axs[0].set(xlabel='reference size (MB) naive query')
    axs[1].set(xlabel='reference size (MB) simpaccel')
    axs[0].set(xticks=list(dfk0Naive['size(MB)']))
    axs[1].set(xticks=list(dfk0Simpaccel['size(MB)']))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_k0.pdf', bbox_inches="tight")


    dfk31Naive = df[(df['k'] == 31) & (df['mode'] == 'naive')].copy()
    dfk31Simpaccel = df[(df['k'] == 31) & (df['mode'] == 'simpaccel')].copy()
    plt.figure()
    f, axs = plt.subplots(1,2,
                      figsize=(10,3),
                      sharey=True)
    sns.lineplot(x='size(MB)', y='time(s)', hue='queryLength', data=dfk31Naive, ax=axs[0], marker="o", dashes=False, legend=False)
    sns.lineplot(x='size(MB)', y='time(s)', hue='queryLength', data=dfk31Simpaccel, ax=axs[1], marker="o", dashes=False)
    axs[0].set(xlabel='reference size (MB) naive query')
    axs[1].set(xlabel='reference size (MB) simpaccel')
    axs[0].set(xticks=list(dfk31Naive['size(MB)']))
    axs[1].set(xticks=list(dfk31Simpaccel['size(MB)']))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_k31.pdf', bbox_inches="tight")

    dfr64q128 = df[(df['queryLength'] == 128) & (df['name'] == 'Pseudomonas')].copy()
    plt.figure()
    sns.lineplot(x='k', y='time(s)', hue='mode', data=dfr64q128, marker="o", dashes=False)
    # plt.ticklabel_format(style='plain')
    plt.xlabel('k')
    plt.ylabel('time of 1000 query (s)')
    plt.xticks(list(dfr64q128['k']))
    plt.title('reference size versus the time requried to do 1000 queries of length 128 on Pseudomonas with different preftab k')
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_Pseudomonas_q128.pdf', bbox_inches="tight")


    dfq128Naive = df[(df['queryLength'] == 64) & (df['mode'] == 'naive')].copy()
    dfq128Simpaccel = df[(df['queryLength'] == 64) & (df['mode'] == 'simpaccel')].copy()
    plt.figure()
    f, axs = plt.subplots(1,2,
                      figsize=(10,3),
                      sharey=True)
    sns.lineplot(x='size(MB)', y='time(s)', hue='k', data=dfq128Naive, ax=axs[0], marker="o", dashes=False)
    sns.lineplot(x='size(MB)', y='time(s)', hue='k', data=dfq128Simpaccel, ax=axs[1], marker="o", dashes=False, legend=False)
    axs[0].set(xlabel='reference size (MB) naive query')
    axs[1].set(xlabel='reference size (MB) simpaccel')
    axs[0].set(xticks=list(dfk31Naive['size(MB)']))
    axs[1].set(xticks=list(dfk31Simpaccel['size(MB)']))
    plt.savefig('/Users/henryxu/Desktop/Sp2022/858D/858D-assignments/assign2/report/figs/evaluate_querysa_time_q128.pdf', bbox_inches="tight")
