import csv
import statistics

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

"""
This code outputs png files that graph the number of total peptides, number of unique peptides, and total proteins found by Comet from a
file that has columns associated with each of the stats mentioned above. 
"""

with open('search_stats_hela_labelfree.csv') as file1:
    reader1 = csv.reader(file1, delimiter = ',')


    hela = list(reader1)

    """grab the total peptide numbers from file, change them into integers from strings
    and find mean/standard dev, then add as error by multiplying stdev by 2"""
    tot_pep = [item[18] for item in hela]
    tot_pep.pop(0)

    for i in range(len(tot_pep)):
        tot_pep[i] = int(tot_pep[i])


    cid35wo_totpepmean = statistics.mean(tot_pep[0:3])
    cid35wi_totpepmean = statistics.mean(tot_pep[3:6])
    hcd28wo_totpepmean = statistics.mean(tot_pep[8:10])
    hcd28wi_totpepmean = statistics.mean(tot_pep[6:8])
    hcd35wo_totpepmean = statistics.mean(tot_pep[10:12])
    hcd35wi_totpepmean = statistics.mean(tot_pep[12:14])


    cid35wo_totpeperror = statistics.stdev(tot_pep[0:3])
    cid35wi_totpeperror = statistics.stdev(tot_pep[3:6])
    hcd28wo_totpeperror = statistics.stdev(tot_pep[8:10])
    hcd28wi_totpeperror = statistics.stdev(tot_pep[6:8])
    hcd35wo_totpeperror = statistics.stdev(tot_pep[10:12])
    hcd35wi_totpeperror = statistics.stdev(tot_pep[12:14])

    cid35 = [ cid35wo_totpepmean, cid35wo_totpeperror*2, cid35wi_totpepmean, cid35wi_totpeperror*2]
    hcd28 = [ hcd28wo_totpepmean, hcd28wo_totpeperror*2, hcd28wi_totpepmean, hcd28wi_totpeperror*2]
    hcd35 = [ hcd35wo_totpepmean, hcd35wo_totpeperror*2, hcd35wi_totpepmean, hcd35wi_totpeperror*2]

    df_totpep = pd.DataFrame([cid35, hcd28, hcd35], columns = ['Without Monocle', 'std1', 'With Monocle','std2'], index = ['cid35','hcd28','hcd35'])

    df_totpep[['Without Monocle','With Monocle']].plot(kind = 'bar', yerr = df_totpep[['std1','std2']].values.T, title = 'Total Peptides found in Hela Label-free Runs', color = ['mediumorchid','lightskyblue'])
    plt.xlabel('Fragmentation')
    plt.savefig('hela_labelfree_comet_totpep.png', bbox_inches = 'tight')


    uni_pep = [item[19] for item in hela]
    uni_pep.pop(0)

    for i in range(len(uni_pep)):
        uni_pep[i] = int(uni_pep[i])

    cid35wo_unipepmean = statistics.mean(uni_pep[0:3])
    cid35wi_unipepmean = statistics.mean(uni_pep[3:6])
    hcd28wo_unipepmean = statistics.mean(uni_pep[8:10])
    hcd28wi_unipepmean = statistics.mean(uni_pep[6:8])
    hcd35wo_unipepmean = statistics.mean(uni_pep[10:12])
    hcd35wi_unipepmean = statistics.mean(uni_pep[12:14])

    cid35wo_unipeperror = statistics.stdev(uni_pep[0:3])
    cid35wi_unipeperror = statistics.stdev(uni_pep[3:6])
    hcd28wo_unipeperror = statistics.stdev(uni_pep[8:10])
    hcd28wi_unipeperror = statistics.stdev(uni_pep[6:8])
    hcd35wo_unipeperror = statistics.stdev(uni_pep[10:12])
    hcd35wi_unipeperror = statistics.stdev(uni_pep[12:14])

    cid35_1 = [ cid35wo_unipepmean, cid35wo_unipeperror*2, cid35wi_unipepmean, cid35wi_unipeperror*2]
    hcd28_1 = [ hcd28wo_unipepmean, hcd28wo_unipeperror*2, hcd28wi_unipepmean, hcd28wi_unipeperror*2]
    hcd35_1 = [ hcd35wo_unipepmean, hcd35wo_unipeperror*2, hcd35wi_unipepmean, hcd35wi_unipeperror*2]

    df_unipep = pd.DataFrame([cid35_1, hcd28_1, hcd35_1], columns = ['Without Monocle', 'std1', 'With Monocle','std2'], index = ['cid35','hcd28','hcd35'])

    df_unipep[['Without Monocle','With Monocle']].plot(kind = 'bar', yerr = df_unipep[['std1','std2']].values.T, title = 'Unique Peptides found in Hela Label-free Runs', color = ['mediumorchid','lightskyblue'])
    plt.xlabel('Fragmentation')
    plt.savefig('hela_labelfree_comet_unipep.png', bbox_inches = 'tight')


    tot_pro = [item[20] for item in hela]
    tot_pro.pop(0)

    for i in range(len(tot_pro)):
        tot_pro[i] = int(tot_pro[i])


    cid35wo_totpromean = statistics.mean(tot_pro[0:3])
    cid35wi_totpromean = statistics.mean(tot_pro[3:6])
    hcd28wo_totpromean = statistics.mean(tot_pro[8:10])
    hcd28wi_totpromean = statistics.mean(tot_pro[6:8])
    hcd35wo_totpromean = statistics.mean(tot_pro[10:12])
    hcd35wi_totpromean = statistics.mean(tot_pro[12:14])

    cid35wo_totproerror = statistics.stdev(tot_pro[0:3])
    cid35wi_totproerror = statistics.stdev(tot_pro[3:6])
    hcd28wo_totproerror = statistics.stdev(tot_pro[8:10])
    hcd28wi_totproerror = statistics.stdev(tot_pro[6:8])
    hcd35wo_totproerror = statistics.stdev(tot_pro[10:12])
    hcd35wi_totproerror = statistics.stdev(tot_pro[12:14])

    cid35_2 = [ cid35wo_totpromean, cid35wo_totproerror*2, cid35wi_totpromean, cid35wi_totproerror*2]
    hcd28_2 = [ hcd28wo_totpromean, hcd28wo_totproerror*2, hcd28wi_totpromean, hcd28wi_totproerror*2]
    hcd35_2 = [ hcd35wo_totpromean, hcd35wo_totproerror*2, hcd35wi_totpromean, hcd35wi_totproerror*2]

    df_totpro = pd.DataFrame([cid35_2, hcd28_2, hcd35_2], columns = ['Without Monocle', 'std1', 'With Monocle','std2'], index = ['cid35','hcd28','hcd35'])

    df_totpro[['Without Monocle','With Monocle']].plot(kind = 'bar', yerr = df_totpro[['std1','std2']].values.T, title = 'Total Proteins found in Hela Label-free Runs', color = ['mediumorchid','lightskyblue'])
    plt.ylim(0,4000)
    plt.xlabel('Fragmentation')
    plt.annotate("Black error bars are two \nstdev from the mean of runs", xy = (0,3500))
    plt.savefig('hela_labelfree_comet_totpro.png', bbox_inches = 'tight')




with open('search_stats_yeast_labelfree.csv') as file2:
    reader2 = csv.reader(file2, delimiter = ',')

    yeast = list(reader2)

    """grab the total peptide numbers from file, change them into integers from strings, and find mean/standard dev"""
    tot_pep = [item[18] for item in yeast]
    tot_pep.pop(0)

    for i in range(len(tot_pep)):
        tot_pep[i] = int(tot_pep[i])


    cid35wo_totpepmean = statistics.mean(tot_pep[0:3])
    cid35wi_totpepmean = statistics.mean(tot_pep[3:6])
    hcd28wo_totpepmean = statistics.mean(tot_pep[8:10])
    hcd28wi_totpepmean = statistics.mean(tot_pep[6:8])
    hcd35wo_totpepmean = statistics.mean(tot_pep[10:12])
    hcd35wi_totpepmean = statistics.mean(tot_pep[12:14])


    cid35wo_totpeperror = statistics.stdev(tot_pep[0:3])
    cid35wi_totpeperror = statistics.stdev(tot_pep[3:6])
    hcd28wo_totpeperror = statistics.stdev(tot_pep[8:10])
    hcd28wi_totpeperror = statistics.stdev(tot_pep[6:8])
    hcd35wo_totpeperror = statistics.stdev(tot_pep[10:12])
    hcd35wi_totpeperror = statistics.stdev(tot_pep[12:14])

    cid35 = [ cid35wo_totpepmean, cid35wo_totpeperror*2, cid35wi_totpepmean, cid35wi_totpeperror*2]
    hcd28 = [ hcd28wo_totpepmean, hcd28wo_totpeperror*2, hcd28wi_totpepmean, hcd28wi_totpeperror*2]
    hcd35 = [ hcd35wo_totpepmean, hcd35wo_totpeperror*2, hcd35wi_totpepmean, hcd35wi_totpeperror*2]

    df_totpep = pd.DataFrame([cid35, hcd28, hcd35], columns = ['Without Monocle', 'std1', 'With Monocle','std2'], index = ['cid35','hcd28','hcd35'])

    df_totpep[['Without Monocle','With Monocle']].plot(kind = 'bar', yerr = df_totpep[['std1','std2']].values.T, title = 'Total Peptides found in Yeast Label-free Runs', color = ['mediumorchid','lightskyblue'])
    plt.xlabel('Fragmentation')
    plt.savefig('yeast_labelfree_comet_totpep.png', bbox_inches = 'tight')


    uni_pep = [item[19] for item in yeast]
    uni_pep.pop(0)

    for i in range(len(uni_pep)):
        uni_pep[i] = int(uni_pep[i])

    cid35wo_unipepmean = statistics.mean(uni_pep[0:3])
    cid35wi_unipepmean = statistics.mean(uni_pep[3:6])
    hcd28wo_unipepmean = statistics.mean(uni_pep[8:10])
    hcd28wi_unipepmean = statistics.mean(uni_pep[6:8])
    hcd35wo_unipepmean = statistics.mean(uni_pep[10:12])
    hcd35wi_unipepmean = statistics.mean(uni_pep[12:14])

    cid35wo_unipeperror = statistics.stdev(uni_pep[0:3])
    cid35wi_unipeperror = statistics.stdev(uni_pep[3:6])
    hcd28wo_unipeperror = statistics.stdev(uni_pep[8:10])
    hcd28wi_unipeperror = statistics.stdev(uni_pep[6:8])
    hcd35wo_unipeperror = statistics.stdev(uni_pep[10:12])
    hcd35wi_unipeperror = statistics.stdev(uni_pep[12:14])

    cid35_1 = [ cid35wo_unipepmean, cid35wo_unipeperror*2, cid35wi_unipepmean, cid35wi_unipeperror*2]
    hcd28_1 = [ hcd28wo_unipepmean, hcd28wo_unipeperror*2, hcd28wi_unipepmean, hcd28wi_unipeperror*2]
    hcd35_1 = [ hcd35wo_unipepmean, hcd35wo_unipeperror*2, hcd35wi_unipepmean, hcd35wi_unipeperror*2]

    df_unipep = pd.DataFrame([cid35_1, hcd28_1, hcd35_1], columns = ['Without Monocle', 'std1', 'With Monocle','std2'], index = ['cid35','hcd28','hcd35'])

    df_unipep[['Without Monocle','With Monocle']].plot(kind = 'bar', yerr = df_unipep[['std1','std2']].values.T, title = 'Unique Peptides found in Yeast Label-free Runs', color = ['mediumorchid','lightskyblue'])
    plt.xlabel('Fragmentation')
    plt.savefig('yeast_labelfree_comet_unipep.png', bbox_inches = 'tight')


    tot_pro = [item[20] for item in yeast]
    tot_pro.pop(0)

    for i in range(len(tot_pro)):
        tot_pro[i] = int(tot_pro[i])


    cid35wo_totpromean = statistics.mean(tot_pro[0:3])
    cid35wi_totpromean = statistics.mean(tot_pro[3:6])
    hcd28wo_totpromean = statistics.mean(tot_pro[8:10])
    hcd28wi_totpromean = statistics.mean(tot_pro[6:8])
    hcd35wo_totpromean = statistics.mean(tot_pro[10:12])
    hcd35wi_totpromean = statistics.mean(tot_pro[12:14])

    cid35wo_totproerror = statistics.stdev(tot_pro[0:3])
    cid35wi_totproerror = statistics.stdev(tot_pro[3:6])
    hcd28wo_totproerror = statistics.stdev(tot_pro[8:10])
    hcd28wi_totproerror = statistics.stdev(tot_pro[6:8])
    hcd35wo_totproerror = statistics.stdev(tot_pro[10:12])
    hcd35wi_totproerror = statistics.stdev(tot_pro[12:14])

    cid35_2 = [ cid35wo_totpromean, cid35wo_totproerror*2, cid35wi_totpromean, cid35wi_totproerror*2]
    hcd28_2 = [ hcd28wo_totpromean, hcd28wo_totproerror*2, hcd28wi_totpromean, hcd28wi_totproerror*2]
    hcd35_2 = [ hcd35wo_totpromean, hcd35wo_totproerror*2, hcd35wi_totpromean, hcd35wi_totproerror*2]

    df_totpro = pd.DataFrame([cid35_2, hcd28_2, hcd35_2], columns = ['Without Monocle', 'std1', 'With Monocle','std2'], index = ['cid35','hcd28','hcd35'])

    df_totpro[['Without Monocle','With Monocle']].plot(kind = 'bar', yerr = df_totpro[['std1','std2']].values.T, title = 'Total Proteins found in Yeast Label-free Runs', color = ['mediumorchid','lightskyblue'])
    plt.ylim(0,4000)
    plt.xlabel('Fragmentation')
    plt.savefig('yeast_labelfree_comet_totpro.png', bbox_inches = 'tight')
