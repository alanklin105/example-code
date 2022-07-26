import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

"""
For hela runs only
Creation of barplots depicting total number of peptides found and total number of unique peptides found by MaxQuant
"""


ms_hela = pd.read_csv("evidence_hela.txt", sep = "\t", low_memory = False)

ms_g06638_hela_hcd28 = set()
ms_g06637_hela_hcd28 = set()
ms_g06630_hela_hcd35 = set()
ms_g06629_hela_hcd35 = set()
ms_g06608_hela_cid35 = set()
ms_g06607_hela_cid35 = set()
ms_g06606_hela_cid35 = set()

g06638_counter = 0
g06637_counter = 0
g06630_counter = 0
g06629_counter = 0
g06608_counter = 0
g06607_counter = 0
g06606_counter = 0



ms_hela1 = ms_hela[['Raw file','Sequence']]
for i in range(len(ms_hela1)):
    if ms_hela1.iloc[i,0] == "g06638_hela_labelfree_hcd28":
        ms_g06638_hela_hcd28.add(ms_hela1.iloc[i,1])
        g06638_counter += 1
    elif ms_hela1.iloc[i,0] == "g06637_hela_labelfree_hcd28":
        ms_g06637_hela_hcd28.add(ms_hela1.iloc[i,1])
        g06637_counter += 1
    elif ms_hela1.iloc[i,0] == "g06630_hela_labelFree_hcd35":
        ms_g06630_hela_hcd35.add(ms_hela1.iloc[i,1])
        g06630_counter += 1
    elif ms_hela1.iloc[i,0] == "g06629_hela_labelFree_hcd35":
        ms_g06629_hela_hcd35.add(ms_hela1.iloc[i,1])
        g06629_counter += 1
    elif ms_hela1.iloc[i,0] == "g06608_hela_LabelFree":
        ms_g06608_hela_cid35.add(ms_hela1.iloc[i,1])
        g06608_counter += 1
    elif ms_hela1.iloc[i,0] == "g06607_hela_LabelFree":
        ms_g06607_hela_cid35.add(ms_hela1.iloc[i,1])
        g06607_counter += 1
    else:
        ms_g06606_hela_cid35.add(ms_hela1.iloc[i,1])
        g06606_counter += 1


hcd28 = st.mean([g06638_counter, g06637_counter])
hcd28er = st.stdev([g06638_counter, g06637_counter]) *2
hcd35 = st.mean([g06630_counter, g06629_counter])
hcd35er = st.stdev([g06630_counter, g06629_counter]) *2
cid35 = st.mean([g06608_counter, g06607_counter, g06606_counter])
cid35er = st.stdev([g06608_counter, g06607_counter, g06606_counter]) *2

g06638_len = len(ms_g06638_hela_hcd28)
g06637_len = len(ms_g06637_hela_hcd28)
g06630_len = len(ms_g06630_hela_hcd35)
g06629_len = len(ms_g06629_hela_hcd35)
g06608_len = len(ms_g06608_hela_cid35)
g06607_len = len(ms_g06607_hela_cid35)
g06606_len = len(ms_g06606_hela_cid35)

hcd28_uni = st.mean([g06638_len, g06637_len])
hcd28_unier = st.stdev([g06638_len, g06637_len]) *2
hcd35_uni = st.mean([g06630_len, g06629_len])
hcd35_unier = st.stdev([g06630_len, g06629_len]) *2
cid35_uni = st.mean([g06608_len, g06607_len, g06606_len])
cid35_unier = st.stdev([g06608_len, g06607_len, g06606_len]) *2


plt1 = plt.figure()
plt.bar(['g06606','g06607','g06608','g06629','g06630','g06637','g06638'], [g06606_counter, g06607_counter, g06608_counter, g06629_counter, g06630_counter, g06637_counter, g06638_counter])
plt.title('Total Peptides found by MaxQuant in Hela Label-free Runs')
plt.xlabel('Run name')
plt.xticks(rotation = 90)
plt.savefig('hela_labelfree_mq_totpep.png', bbox_inches = 'tight')

plt2 = plt.figure()
plt.bar(['hcd28','hcd35','cid35'], [hcd28,hcd35,cid35],color = ['mediumorchid','lightskyblue','mediumorchid'], yerr = [hcd28er,hcd35er,cid35er])

plt.title('Average of total peptides found by MaxQuant in duplicate HeLa label-free runs')
plt.xlabel('Fragmentation Energy scheme')
plt.savefig('hela_labelfree_mq_totpep1.png', bbox_inches = 'tight')


plt3 = plt.figure()
plt.bar(['g06606','g06607','g06608','g06629','g06630','g06637','g06638'], [g06606_len, g06607_len, g06608_len, g06629_len, g06630_len, g06637_len, g06638_len])
plt.title('Total unique peptides found by MaxQuant in HeLa label-free runs')
plt.xlabel('Run name')
plt.xticks(rotation = 90)
plt.savefig('hela_labelfree_mq_unipep.png', bbox_inches = 'tight')

pl4 = plt.figure()
plt.bar(['hcd28','hcd35','cid35'], [hcd28_uni,hcd35_uni,cid35_uni],color = ['mediumorchid','lightskyblue','mediumorchid'], yerr = [hcd28_unier,hcd35_unier,cid35_unier])

plt.title('Average of unique peptides found by MaxQuant in duplicate HeLa label-free runs')
plt.xlabel('Fragmentation Energy scheme')
plt.savefig('hela_labelfree_mq_unipep1.png', bbox_inches = 'tight')
