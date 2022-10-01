
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
# user input for setting up the preference
p_value = 0.1
fold_change = 1.2
fc1 = np.log2(1/fold_change)
fc2 = np.log2(fold_change)
logP = -np.log10(p_value)
font_family = 'arial'
font_weight = 'bold'
font_size_tick = 16
font_size_label = 18
n_std = 2

# first column must be gene list,
# second column must be fold change without log transformation
# third column must be P value without log transformation

# input file types can be .xlsx, .txt, .tab and .csv
os.chdir("input")
input_file = "volcano_data.csv"

if input_file.endswith('.xlsx'):
    data = pd.read_excel(input_file)
elif input_file.endswith('.txt'):
    data = pd.read_csv(input_file)
elif input_file.endswith('.tab'):
    data = pd.read_table(input_file)
else:
    data = pd.read_csv(input_file)

# get column names of the input table
col1 = data.columns.to_list()[0]
col2 = data.columns.to_list()[1]
col3 = data.columns.to_list()[2]

data = data.dropna(axis=0, how='any')
# do log transformations
data["FC"] = np.log2(data[col2])
data["logP"] = -np.log10(data[col3])

lower_limit = np.mean(data["FC"]) - n_std* np.std(data["FC"])
upper_limit = np.mean(data["FC"]) + n_std* np.std(data["FC"])

os.chdir('../output/volcano/')
# set up output file name
output_file = "output_"+ input_file.split('.')[0] + ".csv"
data.to_csv(output_file, index=False)


# if lower than lower limit, let equal to lower limit
# if larger than upper limit, let equal to upper limit
data.loc[data["FC"]<lower_limit, 'FC'] = lower_limit
data.loc[data["FC"]>upper_limit, 'FC'] = upper_limit

plt.rcParams.update({'font.family':font_family})

plt.scatter(data["FC"], data["logP"], color='grey')
plt.scatter(data[(data["FC"]<fc1) & (data["logP"]>logP)]["FC"], data[(data["FC"]<fc1) & (data["logP"]>logP)]["logP"], marker='o', color='green')
plt.scatter(data[(data["FC"]>fc2) & (data["logP"]>logP)]["FC"], data[(data["FC"]>fc2) & (data["logP"]>logP)]["logP"], marker='o', color='red')
plt.axvline(x=fc1)
plt.axvline(x=fc2)
plt.axhline(y=logP)

max_limit = max(abs(lower_limit), abs(upper_limit))
plt.xlim([-max_limit, max_limit])
plt.xticks(fontsize=font_size_tick, fontweight= font_weight )
plt.yticks(fontsize=font_size_tick, fontweight=font_weight )
plt.xlabel('Fold change (log2)', fontsize=font_size_label, fontweight=font_weight)
plt.ylabel('-Log10 P-value', fontsize=font_size_label, fontweight=font_weight)
plt.savefig("valcano.jpg", dpi=600)
plt.show()
print(plt.rcParams['font.family'])
# plt.rcParams.update({'font.family':'arial'})
