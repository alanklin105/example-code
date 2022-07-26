import pandas as pd

"""
SPECIFICALLY FOR YEAST NO FILTER, WITH OR WITHOUT correction

This code utilizes set intersection to find mutual scan and peptide sequences, which are put into tuples.
It outputs the number of Comet-unique, MaxQuant-unique, and mutual matches, which can then be put into venn diagrams in another code
"""
"""MQ used raw files so no correction"""

ms_yeast = pd.read_csv("msms_yeast.txt", sep = "\t", low_memory = False)

ms_g06635_yeast_hcd28 = set()
ms_g06634_yeast_hcd28 = set()
ms_g06628_yeast_hcd35 = set()
ms_g06627_yeast_hcd35 = set()
ms_g06612_yeast_cid35 = set()
ms_g06611_yeast_cid35 = set()
ms_g06610_yeast_cid35 = set()

ms_yeast1 = ms_yeast[['Raw file','Sequence','Scan number']]
for i in range(len(ms_yeast1)):
    if ms_yeast1.iloc[i,0] == "g06635_yeast_labelfree_hcd28":
        ms_g06635_yeast_hcd28.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))
    elif ms_yeast1.iloc[i,0] == "g06634_yeast_labelfree_hcd28":
        ms_g06634_yeast_hcd28.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))
    elif ms_yeast1.iloc[i,0] == "g06628_yeast_labelFree_hcd35":
        ms_g06628_yeast_hcd35.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))
    elif ms_yeast1.iloc[i,0] == "g06627_yeast_labelFree_hcd35":
        ms_g06627_yeast_hcd35.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))
    elif ms_yeast1.iloc[i,0] == "g06612_yeast_LabelFree":
        ms_g06612_yeast_cid35.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))
    elif ms_yeast1.iloc[i,0] == "g06611_yeast_LabelFree":
        ms_g06611_yeast_cid35.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))
    else:
        ms_g06610_yeast_cid35.add((ms_yeast1.iloc[i,2], ms_yeast1.iloc[i,1]))

"""no monocle correction"""


g06635_yeast_wo = pd.read_csv("g06635_yeast_labelfree_hcd28_woCorrection.csv", sep = ",", low_memory = False)
g06634_yeast_wo = pd.read_csv("g06634_yeast_labelfree_hcd28_woCorrection.csv", sep = ",", low_memory = False)
g06628_yeast_wo = pd.read_csv("g06628_yeast_labelFree_hcd35_woCorrection.csv", sep = ",", low_memory = False)
g06627_yeast_wo = pd.read_csv("g06627_yeast_labelFree_hcd35_woCorrection.csv", sep = ",", low_memory = False)
g06612_yeast_wo = pd.read_csv("g06612_yeast_LabelFree_woCorrection.csv", sep = ",", low_memory = False)
g06611_yeast_wo = pd.read_csv("g06611_yeast_LabelFree_woCorrection.csv", sep = ",", low_memory = False)
g06610_yeast_wo = pd.read_csv("g06610_yeast_LabelFree_woCorrection.csv", sep = ",", low_memory = False)

def remove(peptide):
    peptide = peptide[2:]
    peptide = peptide[:len(peptide)-2]
    peptide = peptide.replace("*", "")
    return peptide

####################
g06635pep = g06635_yeast_wo['Peptide'].to_list()
g06635scan = g06635_yeast_wo['ScanF'].to_list()
g06635pep1 = [remove(peptide) for peptide in g06635pep]
g06635_merge = set(tuple(zip(g06635scan, g06635pep1)))

inter1 = len(g06635_merge.intersection(ms_g06635_yeast_hcd28))
merge1 = len(g06635_merge)
ms1 = len(ms_g06635_yeast_hcd28)


com1 = merge1 - inter1
msuni1 = ms1- inter1
total1 = com1 + msuni1 + inter1

com1per = com1/total1
int1per = inter1/total1
msuni1per = msuni1/total1
print("comet unique for g06635 is {},{}".format(com1,com1per))
print("intersection is {},{}".format(inter1, int1per))
print("mq unique is {},{}".format(msuni1, msuni1per))
print('\n')

###################
g06634pep = g06634_yeast_wo['Peptide'].to_list()
g06634scan = g06634_yeast_wo['ScanF'].to_list()
g06634pep1 = [remove(peptide) for peptide in g06634pep]
g06634_merge = set(tuple(zip(g06634scan, g06634pep1)))

inter2 = len(g06634_merge.intersection(ms_g06634_yeast_hcd28))
merge2 = len(g06634_merge)
ms2 = len(ms_g06634_yeast_hcd28)

com2 = merge2 - inter2
msuni2 = ms2 - inter2
total2 = com2 + msuni2 + inter2

com2per = com2/total2
int2per = inter2/total2
msuni2per = msuni2/total2
print("comet unique for g06634 is {},{}".format(com2,com2per))
print("intersection is {},{}".format(inter2, int2per))
print("mq unique is {},{}".format(msuni2, msuni2per))
print('\n')

#####################3
g06628pep = g06628_yeast_wo['Peptide'].to_list()
g06628scan = g06628_yeast_wo['ScanF'].to_list()
g06628pep1 = [remove(peptide) for peptide in g06628pep]
g06628_merge = set(tuple(zip(g06628scan, g06628pep1)))

inter3 = len(g06628_merge.intersection(ms_g06628_yeast_hcd35))
merge3 = len(g06628_merge)
ms3 = len(ms_g06628_yeast_hcd35)


com3 = merge3 - inter3
msuni3 = ms3 - inter3
total3 = com3 + msuni3 + inter3

com3per = com3/total3
int3per = inter3/total3
msuni3per = msuni3/total3
print("comet unique for g06628 is {},{}".format(com3,com3per))
print("intersection is {},{}".format(inter3, int3per))
print("mq unique is {},{}".format(msuni3, msuni3per))
print('\n')
#######################
g06627pep = g06627_yeast_wo['Peptide'].to_list()
g06627scan = g06627_yeast_wo['ScanF'].to_list()
g06627pep1 = [remove(peptide) for peptide in g06627pep]
g06627_merge = set(tuple(zip(g06627scan, g06627pep1)))

inter4 = len(g06627_merge.intersection(ms_g06627_yeast_hcd35))
merge4 = len(g06627_merge)
ms4 = len(ms_g06627_yeast_hcd35)

com4 = merge4 - inter4
msuni4 = ms4 - inter4
total4 = com4 + msuni4 + inter4

com4per = com4/total4
int4per = inter4/total4
msuni4per = msuni4/total4
print("comet unique for g06627 is {},{}".format(com4,com4per))
print("intersection is {},{}".format(inter4, int4per))
print("mq unique is {},{}".format(msuni4, msuni4per))
print('\n')
###################
g06612pep = g06612_yeast_wo['Peptide'].to_list()
g06612scan = g06612_yeast_wo['ScanF'].to_list()
g06612pep1 = [remove(peptide) for peptide in g06612pep]
g06612_merge = set(tuple(zip(g06612scan, g06612pep1)))

inter5 = len(g06612_merge.intersection(ms_g06612_yeast_cid35))
merge5 = len(g06612_merge)
ms5 = len(ms_g06612_yeast_cid35)

com5 = merge5 - inter5
msuni5 = ms5 - inter5
total5 = com5 + msuni5 + inter5

com5per = com5/total5
int5per = inter5/total5
msuni5per = msuni5/total5
print("comet unique for g06612 is {},{}".format(com5,com5per))
print("intersection is {},{}".format(inter5, int5per))
print("mq unique is {},{}".format(msuni5, msuni5per))
print("\n")
######################
g06611pep = g06611_yeast_wo['Peptide'].to_list()
g06611scan = g06611_yeast_wo['ScanF'].to_list()
g06611pep1 = [remove(peptide) for peptide in g06611pep]
g06611_merge = set(tuple(zip(g06611scan, g06611pep1)))

inter6 = len(g06611_merge.intersection(ms_g06611_yeast_cid35))
merge6 = len(g06611_merge)
ms6 = len(ms_g06611_yeast_cid35)

com6 = merge6 - inter6
msuni6 = ms6 - inter6
total6 = com6 + msuni6 + inter6

com6per = com6/total6
int6per = inter6/total6
msuni6per = msuni6/total6
print("comet unique for g06611 is {},{}".format(com6,com6per))
print("intersection is {},{}".format(inter6, int6per))
print("mq unique is {},{}".format(msuni6, msuni6per))
print("\n")
#################
g06610pep = g06610_yeast_wo['Peptide'].to_list()
g06610scan = g06610_yeast_wo['ScanF'].to_list()
g06610pep1 = [remove(peptide) for peptide in g06610pep]
g06610_merge = set(tuple(zip(g06610scan, g06610pep1)))

inter7 = len(g06610_merge.intersection(ms_g06610_yeast_cid35))
merge7 = len(g06610_merge)
ms7 = len(ms_g06610_yeast_cid35)

com7 = merge7 - inter7
msuni7 = ms7 - inter7
total7 = com7 + msuni7 + inter7

com7per = com7/total7
int7per = inter7/total7
msuni7per = msuni7/total7
print("comet unique for g06610 is {},{}".format(com7,com7per))
print("intersection is {},{}".format(inter7, int7per))
print("mq unique is {},{}".format(msuni7, msuni7per))
print("\n")
###################
print("now with correction")

"""with Monocle correction"""

g06635_yeast_w = pd.read_csv("g06635_yeast_labelfree_hcd28_MonocleCLI.csv", sep = ",", low_memory = False)
g06634_yeast_w = pd.read_csv("g06634_yeast_labelfree_hcd28_MonocleCLI.csv", sep = ",", low_memory = False)
g06628_yeast_w = pd.read_csv("g06628_yeast_labelFree_hcd35_MonocleCLI.csv", sep = ",", low_memory = False)
g06627_yeast_w = pd.read_csv("g06627_yeast_labelFree_hcd35_MonocleCLI.csv", sep = ",", low_memory = False)
g06612_yeast_w = pd.read_csv("g06612_yeast_LabelFree_MonocleCLI.csv", sep = ",", low_memory = False)
g06611_yeast_w = pd.read_csv("g06611_yeast_LabelFree_MonocleCLI.csv", sep = ",", low_memory = False)
g06610_yeast_w = pd.read_csv("g06610_yeast_LabelFree_MonocleCLI.csv", sep = ",", low_memory = False)


g06635pep_w = g06635_yeast_w['Peptide'].to_list()
g06635scan_w = g06635_yeast_w['ScanF'].to_list()
g06635pep1_w = [remove(peptide) for peptide in g06635pep_w]
g06635_merge_w = set(tuple(zip(g06635scan_w, g06635pep1_w)))

inter1_w = len(g06635_merge_w.intersection(ms_g06635_yeast_hcd28))
merge1_w = len(g06635_merge_w)
ms1 = len(ms_g06635_yeast_hcd28)


com1_w = merge1_w - inter1_w
msuni1_w = ms1 - inter1_w
total1_w = com1_w + msuni1_w + inter1_w

com1per_w = com1_w/total1_w
int1per_w = inter1_w/total1_w
msuni1per_w = msuni1_w/total1_w
print("comet unique for g06635 is {},{}".format(com1_w,com1per_w))
print("intersection is {},{}".format(inter1_w, int1per_w))
print("mq unique is {},{}".format(msuni1_w, msuni1per_w))
print('\n')
###################
g06634pep_w = g06634_yeast_w['Peptide'].to_list()
g06634scan_w = g06634_yeast_w['ScanF'].to_list()
g06634pep1_w = [remove(peptide) for peptide in g06634pep_w]
g06634_merge_w = set(tuple(zip(g06634scan_w, g06634pep1_w)))

inter2_w = len(g06634_merge_w.intersection(ms_g06634_yeast_hcd28))
merge2_w = len(g06634_merge_w)
ms2 = len(ms_g06634_yeast_hcd28)

com2_w = merge2_w - inter2_w
msuni2_w = ms2 - inter2_w
total2_w = com2_w + msuni2_w + inter2_w

com2per_w = com2_w/total2_w
int2per_w = inter2_w/total2_w
msuni2per_w = msuni2_w/total2_w
print("comet unique for g06634 is {},{}".format(com2_w,com2per_w))
print("intersection is {},{}".format(inter2_w, int2per_w))
print("mq unique is {},{}".format(msuni2_w, msuni2per_w))
print('\n')
#####################
g06628pep_w = g06628_yeast_w['Peptide'].to_list()
g06628scan_w = g06628_yeast_w['ScanF'].to_list()
g06628pep1_w = [remove(peptide) for peptide in g06628pep_w]
g06628_merge_w = set(tuple(zip(g06628scan_w, g06628pep1_w)))

inter3_w = len(g06628_merge_w.intersection(ms_g06628_yeast_hcd35))
merge3_w = len(g06628_merge_w)
ms3 = len(ms_g06628_yeast_hcd35)


com3_w = merge3_w - inter3_w
msuni3_w = ms3 - inter3_w
total3_w = com3_w + msuni3_w + inter3_w

com3per_w = com3_w/total3_w
int3per_w = inter3_w/total3_w
msuni3per_w = msuni3_w/total3_w
print("comet unique for g06628 is {},{}".format(com3_w,com3per_w))
print("intersection is {},{}".format(inter3_w, int3per_w))
print("mq unique is {},{}".format(msuni3_w, msuni3per_w))
print('\n')
#######################
g06627pep_w = g06627_yeast_w['Peptide'].to_list()
g06627scan_w = g06627_yeast_w['ScanF'].to_list()
g06627pep1_w = [remove(peptide) for peptide in g06627pep_w]
g06627_merge_w = set(tuple(zip(g06627scan_w, g06627pep1_w)))

inter4_w = len(g06627_merge_w.intersection(ms_g06627_yeast_hcd35))
merge4_w = len(g06627_merge_w)
ms4 = len(ms_g06627_yeast_hcd35)

com4_w = merge4_w - inter4_w
msuni4_w = ms4 - inter4_w
total4_w = com4_w + msuni4_w + inter4_w

com4per_w = com4_w/total4_w
int4per_w = inter4_w/total4_w
msuni4per_w = msuni4_w/total4_w
print("comet unique for g06627 is {},{}".format(com4_w,com4per_w))
print("intersection is {},{}".format(inter4_w, int4per_w))
print("mq unique is {},{}".format(msuni4_w, msuni4per_w))
print('\n')
###################
g06612pep_w = g06612_yeast_w['Peptide'].to_list()
g06612scan_w = g06612_yeast_w['ScanF'].to_list()
g06612pep1_w = [remove(peptide) for peptide in g06612pep_w]
g06612_merge_w = set(tuple(zip(g06612scan_w, g06612pep1_w)))

inter5_w = len(g06612_merge_w.intersection(ms_g06612_yeast_cid35))
merge5_w = len(g06612_merge_w)
ms5 = len(ms_g06612_yeast_cid35)

com5_w = merge5_w - inter5_w
msuni5_w = ms5 - inter5_w
total5_w = com5_w + msuni5_w + inter5_w

com5per_w = com5_w/total5_w
int5per_w = inter5_w/total5_w
msuni5per_w = msuni5_w/total5_w
print("comet unique for g06612 is {},{}".format(com5_w,com5per_w))
print("intersection is {},{}".format(inter5_w, int5per_w))
print("mq unique is {},{}".format(msuni5_w, msuni5per_w))
print('\n')
######################
g06611pep_w = g06611_yeast_w['Peptide'].to_list()
g06611scan_w = g06611_yeast_w['ScanF'].to_list()
g06611pep1_w = [remove(peptide) for peptide in g06611pep_w]
g06611_merge_w = set(tuple(zip(g06611scan_w, g06611pep1_w)))

inter6_w = len(g06611_merge_w.intersection(ms_g06611_yeast_cid35))
merge6_w = len(g06611_merge_w)
ms6 = len(ms_g06611_yeast_cid35)

com6_w = merge6_w - inter6_w
msuni6_w = ms6 - inter6_w
total6_w = com6_w + msuni6_w + inter6_w

com6per_w = com6_w/total6_w
int6per_w = inter6_w/total6_w
msuni6per_w = msuni6_w/total6_w
print("comet unique for g06611 is {},{}".format(com6_w,com6per_w))
print("intersection is {},{}".format(inter6_w, int6per_w))
print("mq unique is {},{}".format(msuni6_w, msuni6per_w))
print('\n')
#################
g06610pep_w = g06610_yeast_w['Peptide'].to_list()
g06610scan_w = g06610_yeast_w['ScanF'].to_list()
g06610pep1_w = [remove(peptide) for peptide in g06610pep_w]
g06610_merge_w = set(tuple(zip(g06610scan_w, g06610pep1_w)))

inter7_w = len(g06610_merge_w.intersection(ms_g06610_yeast_cid35))
merge7_w = len(g06610_merge_w)
ms7 = len(ms_g06610_yeast_cid35)

com7_w = merge7_w - inter7_w
msuni7_w = ms7 - inter7_w
total7_w = com7_w + msuni7_w + inter7_w

com7per_w = com7_w/total7_w
int7per_w = inter7_w/total7_w
msuni7per_w = msuni7_w/total7_w
print("comet unique for g06610 is {},{}".format(com7_w,com7per_w))
print("intersection is {},{}".format(inter7_w, int7per_w))
print("mq unique is {},{}".format(msuni7_w, msuni7per_w))
