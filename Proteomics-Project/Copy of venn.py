from matplotlib_venn import venn2_unweighted
import matplotlib.pyplot as plt

"""
Creation of venn diagrams associated with yeast runs with no filter, with and without correction, or mq1.py

"""


"""wo correction"""

"""g06635 yeast hcd28"""
plt1 = plt.figure(0)
venn2_unweighted(subsets = ("29403 or 60.01%", "8458 or 17.26%", "11139 or 22.73%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06635 label-free yeast run - hcd28')
plt.savefig('g06635venn_wo.png', bbox_inches = 'tight')


"""g06634 yeast hcd28"""
plt2 = plt.figure(1)
venn2_unweighted(subsets = ("28857 or 59.34%", "8484 or 17.45%", "11288 or 23.21%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06634 label-free yeast run - hcd28')
plt.savefig('g06634venn_wo.png', bbox_inches = 'tight')

"""g06628 yeast hcd35"""
plt3 = plt.figure(2)
venn2_unweighted(subsets = ("27685 or 59.76%","7866 or 16.98%","10774 or 23.25%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06628 label-free yeast run - hcd35')
plt.savefig('g06628venn_wo.png', bbox_inches = 'tight')

"""g06627 yeast hcd35"""
plt4 = plt.figure(3)
venn2_unweighted(subsets = ("27802 or 60.23%","7598 or 16.46%","10757 or 23.31%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06627 label-free yeast run - hcd35')
plt.savefig('g06627venn_wo.png', bbox_inches = 'tight')

"""g06612 yeast cid35"""
plt5 = plt.figure(4)
venn2_unweighted(subsets = ("45690 or 71.26%","7390 or 11.41%","11041 or 17.22%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06612 label-free yeast run - cid35')
plt.savefig('g06612venn_wo.png', bbox_inches = 'tight')

"""g06611 yeast cid35"""
plt6 = plt.figure(5)
venn2_unweighted(subsets = ("47043 or 71.03%", "7559 or 11.41%","11628 or 17.56%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06611 label-free yeast run - cid35')
plt.savefig('g06611venn_wo.png', bbox_inches = 'tight')

"""g06610 yeast cid35"""
plt7 = plt.figure(6)
venn2_unweighted(subsets = ("47212 or 71.52%", "7235 or 10.96%","11566 or 17.52%"), set_labels = ('Comet search without correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06610 label-free yeast run - cid35')
plt.savefig('g06610venn_wo.png', bbox_inches = 'tight')



"""with correction"""

"""g06635 yeast hcd28"""
plt8 = plt.figure(7)
venn2_unweighted(subsets = ("24182 or 55.24%","3186 or 7.28%","16411 or 37.49%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06635 label-free yeast run - hcd28')
plt.savefig('g06635venn_w.png', bbox_inches = 'tight')


"""g06634 yeast hcd28"""
plt9 = plt.figure(8)
venn2_unweighted(subsets = ("23644 or 54.46%","3258 or 7.50%","16514 or 38.04%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06634 label-free yeast run - hcd28')
plt.savefig('g06634venn_w.png', bbox_inches = 'tight')

"""g06628 yeast hcd35"""
plt10 = plt.figure(9)
venn2_unweighted(subsets = ("22886 or 55.11%","3030 or 7.30%","15610 or 37.59%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06628 label-free yeast run - hcd35')
plt.savefig('g06628venn_w.png', bbox_inches = 'tight')

"""g06627 yeast hcd35"""
plt11 = plt.figure(10)
venn2_unweighted(subsets = ("23046 or 55.67%","2819 or 6.81%","15536 or 37.53%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06627 label-free yeast run - hcd35')
plt.savefig('g06627venn_w.png', bbox_inches = 'tight')

"""g06612 yeast cid35"""
plt12 = plt.figure(11)
venn2_unweighted(subsets = ("41339 or 69.16%","3028 or 5.07%","15403 or 25.77%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06612 label-free yeast run - cid35')
plt.savefig('g06612venn_w.png', bbox_inches = 'tight')

"""g06611 yeast cid35"""
plt13 = plt.figure(12)
venn2_unweighted(subsets = ("42466 or 68.88%","2969 or 4.82%","16218 or 26.31%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06611 label-free yeast run - cid35')
plt.savefig('g06611venn_w.png', bbox_inches = 'tight')

"""g06610 yeast cid35"""
plt14 = plt.figure(13)
venn2_unweighted(subsets = ("42866 or 69.51%","2867 or 4.65%","15934 or 25.84%"), set_labels = ('Comet search with correction', 'MaxQuant search without correction'), set_colors = ('mediumorchid','lightskyblue'), alpha = 0.5)
plt.annotate('Percentage out of total peptides \n(Comet unique + MQ unique + shared)', xy = (0.5,0.4))
plt.title('Unfiltered Peptide Spectral Matches for g06610 label-free yeast run - cid35')
plt.savefig('g06610venn_w.png', bbox_inches = 'tight')
