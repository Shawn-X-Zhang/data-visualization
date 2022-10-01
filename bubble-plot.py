import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


# user set parameters here
os.chdir('input')
input_file_name = "bubble_data.xlsx"
#input_file_name = "BP JW 16 proteins.xlsx"
#input_file_name = "MF JW 16 proteins.xlsx"


font_family = 'arial'
font_weight = 'bold'
font_size_tick = 16
font_size_label = 16
x_tick_interval = 1
labelpad = 10   #: chnage the distance between the x-label and Y-label and tick label.  If want to ahve sepoarate diatqance, jsut add a x-labelpad and y-labelpad
figure_size = [16, 12]
spacing = 1


df = pd.read_excel(input_file_name)  # y-axis has to be the 1st column, and X-axis to be P-value

# transform P value as negative log10
#df['logP'] = -np.log10(df['P-Value'])
df['logP'] = -np.log10(df.iloc[:,2])
df.to_csv("output"+input_file_name.split(sep=".")[0]+".txt",sep="\t", index=False)
xlabel="-Log10"+" (P-value)"
ylabel=df.columns.to_list()[0] #0 is the 1st column
print(ylabel)

#print(df.iloc[:,0])
print(df)
# calculate lower and upper limits of X axis, may take 0 as lower limit
lower_limit = np.min(df['logP'])*0.8
upper_limit = np.max(df['logP'])*1.3

plt.rcParams.update({'font.family':font_family})

plt.figure(figsize=figure_size,tight_layout=True)
ax=plt.gca()
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.xaxis.set_tick_params(width=3)
ax.yaxis.set_tick_params(width=3)
ax.tick_params(direction='out', length=8, width=2, colors='black')

#plt.scatter(df["logP"], df["Pathway"],  s=df["Count"]*100, c=df["Count"]*100-100) #'PiYG'
print(df["Count"]*30)

# the following two lines code to make bubble sizes ranged between 1000 and 10000
bubble_sizes = (df["Count"] - df["Count"].min())/(df["Count"].max() - df["Count"].min())
bubble_sizes = bubble_sizes*9000+1000

fig = plt.scatter(df["logP"], df.iloc[:,0],  s=bubble_sizes, marker="^", c=df["Count"],cmap='prism', alpha=0.9) #'PiYG' 'RdPu_r'  C: color
#fig = plt.scatter(df["logP"], df["Pathway"],  s=df["Count"]*30, cmap='prism', alpha=0.9) #'PiYG' 'RdPu_r'  C: color
#plt.scatter(df["logP"], df["Pathway"],  s=df["Count"]*100, color="blue",alpha=0.8,edgecolors="black", )
# c: color; s: size.
for i in range(df.shape[0]):
 #plt.text(df.loc[i, "logP"],i,df.loc[i,"Count"],size=11,horizontalalignment='center')
 #plt.text(df.loc[i, "logP"], i, round(df.loc[i, "Ratio"],2), size=18, color="black", fontweight='bold', horizontalalignment='center', verticalalignment='center') # for change the font/color of the text inside the circles

 plt.text(df.loc[i, "logP"], i, round(df.iloc[i, 3],2), size=18, color="black", fontweight='bold',
          horizontalalignment='center',
          verticalalignment='center')  # for change the font/color of the text inside the circles; df.loc[i, "logP"]: x-axix: i: y-axis, round(df.iloc[i, 3],2): text inside the bubble
plt.tight_layout()
# can use ticks=[], and labels=[]
plt.xticks(np.arange(0, int(upper_limit), step=x_tick_interval), fontsize=font_size_tick, fontweight= font_weight )
plt.yticks(df.iloc[:,0], fontsize=font_size_tick, fontweight=font_weight )

#plt.xticks(fontsize=16, fontweight= 'bold' )
#plt.yticks(fontsize=16, fontweight='bold')   ctrl+?  t comment multiple lines
#plt.xlabel("-Log10 (P-value)", labelpad=labelpad, fontsize=font_size_label, fontweight=font_weight)
plt.xlabel(xlabel, labelpad=labelpad, fontsize=font_size_label, fontweight=font_weight)
# plt.ylabel("Pathway", fontsize=16, fontweight='bold')
plt.ylabel(ylabel, labelpad=labelpad,fontsize=font_size_label, fontweight=font_weight)
#plt.xlim([lower_limit, upper_limit])
plt.xlim([0, upper_limit])
plt.ylim(-1,df.shape[0])

#plt.set_linewidth(6)

output_file_name = "output_" + input_file_name.split(".")[0]
plt.savefig(output_file_name + ".jpg", dpi=600)
plt.savefig(output_file_name + ".tiff",bbox_inches='tight',dpi=300)
#
# plt.savefig("BP.jpg",bbox_inches='tight')
# plt.savefig("BP.tiff",bbox_inches='tight')
plt.show()
#print(plt.get_ylim())
#print(plt.rcParams['font.family'])

