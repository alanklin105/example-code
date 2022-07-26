import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

"""
For yeast runs only
Creation of barplots depicting total number of peptides found and total number of unique peptides found by MaxQuant
"""



ms_yeast = pd.read_csv("evidence_yeast.txt", sep = "\t", low_memory = False)

ms_g06635_yeast_hcd28 = set()
ms_g06634_yeast_hcd28 = set()
ms_g06628_yeast_hcd35 = set()
ms_g06627_yeast_hcd35 = set()
ms_g06612_yeast_cid35 = set()
ms_g06611_yeast_cid35 = set()
ms_g06610_yeast_cid35 = set()

g06635_counter = 0
g06634_counter = 0
g06628_counter = 0
g06627_counter = 0
g06612_counter = 0
g06611_counter = 0
g06610_counter = 0



ms_yeast1 = ms_yeast[['Raw file','Sequence']]
for i in range(len(ms_yeast1)):
    if ms_yeast1.iloc[i,0] == "g06635_yeast_labelfree_hcd28":
        ms_g06635_yeast_hcd28.add(ms_yeast1.iloc[i,1])
        g06635_counter += 1
    elif ms_yeast1.iloc[i,0] == "g06634_yeast_labelfree_hcd28":
        ms_g06634_yeast_hcd28.add(ms_yeast1.iloc[i,1])
        g06634_counter += 1
    elif ms_yeast1.iloc[i,0] == "g06628_yeast_labelFree_hcd35":
        ms_g06628_yeast_hcd35.add(ms_yeast1.iloc[i,1])
        g06628_counter += 1
    elif ms_yeast1.iloc[i,0] == "g06627_yeast_labelFree_hcd35":
        ms_g06627_yeast_hcd35.add(ms_yeast1.iloc[i,1])
        g06627_counter += 1
    elif ms_yeast1.iloc[i,0] == "g06612_yeast_LabelFree":
        ms_g06612_yeast_cid35.add(ms_yeast1.iloc[i,1])
        g06612_counter += 1
    elif ms_yeast1.iloc[i,0] == "g06611_yeast_LabelFree":
        ms_g06611_yeast_cid35.add(ms_yeast1.iloc[i,1])
        g06611_counter += 1
    else:
        ms_g06610_yeast_cid35.add(ms_yeast1.iloc[i,1])
        g06610_counter += 1


hcd28 = st.mean([g06635_counter, g06634_counter])
hcd28er = st.stdev([g06635_counter, g06634_counter]) *2
hcd35 = st.mean([g06628_counter, g06627_counter])
hcd35er = st.stdev([g06628_counter, g06627_counter]) *2
cid35 = st.mean([g06612_counter, g06611_counter, g06610_counter])
cid35er = st.stdev([g06612_counter, g06611_counter, g06610_counter]) *2

g06635_len = len(ms_g06635_yeast_hcd28)
g06634_len = len(ms_g06634_yeast_hcd28)
g06628_len = len(ms_g06628_yeast_hcd35)
g06627_len = len(ms_g06627_yeast_hcd35)
g06612_len = len(ms_g06612_yeast_cid35)
g06611_len = len(ms_g06611_yeast_cid35)
g06610_len = len(ms_g06610_yeast_cid35)

hcd28_uni = st.mean([g06635_len, g06634_len])
hcd28_unier = st.stdev([g06635_len, g06634_len]) *2
hcd35_uni = st.mean([g06628_len, g06627_len])
hcd35_unier = st.stdev([g06628_len, g06627_len]) *2
cid35_uni = st.mean([g06612_len, g06611_len, g06610_len])
cid35_unier = st.stdev([g06612_len, g06611_len, g06610_len]) *2


plt1 = plt.figure()
plt.bar(['g06610','g06611','g06612','g06627','g06628','g06634','g06635'], [g06610_counter, g06611_counter, g06612_counter, g06627_counter, g06628_counter, g06634_counter, g06635_counter])
plt.title('Total Peptides found by MaxQuant in yeast Label-free Runs')
plt.xlabel('Run name')
plt.xticks(rotation = 90)
plt.savefig('yeast_labelfree_mq_totpep.png', bbox_inches = 'tight')

plt2 = plt.figure()
plt.bar(['hcd28','hcd35','cid35'], [hcd28,hcd35,cid35],color = ['mediumorchid','lightskyblue','mediumorchid'], yerr = [hcd28er,hcd35er,cid35er])

plt.title('Average of total peptides found by MaxQuant in duplicate yeast label-free runs')
plt.xlabel('Fragmentation Energy scheme')
plt.savefig('yeast_labelfree_mq_totpep1.png', bbox_inches = 'tight')


plt3 = plt.figure()
plt.bar(['g06610','g06611','g06612','g06627','g06628','g06634','g06635'], [g06610_len, g06611_len, g06612_len, g06627_len, g06628_len, g06634_len, g06635_len])
plt.title('Total unique peptides found by MaxQuant in yeast label-free runs')
plt.xlabel('Run name')
plt.xticks(rotation = 90)
plt.savefig('yeast_labelfree_mq_unipep.png', bbox_inches = 'tight')

pl4 = plt.figure()
plt.bar(['hcd28','hcd35','cid35'], [hcd28_uni,hcd35_uni,cid35_uni],color = ['mediumorchid','lightskyblue','mediumorchid'], yerr = [hcd28_unier,hcd35_unier,cid35_unier])

plt.title('Average of unique peptides found by MaxQuant in duplicate yeast label-free runs')
plt.xlabel('Fragmentation Energy scheme')
plt.savefig('yeast_labelfree_mq_unipep1.png', bbox_inches = 'tight')
