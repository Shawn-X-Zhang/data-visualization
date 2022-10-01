
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")
print(tips)
x=tips["total_bill"]
print(sorted(x))

# Draw a single horizontal swarm plot:
ax = sns.swarmplot(x=tips["total_bill"], size=10) #can use size argument in all remaining plots
plt.show()

# Group the swarms by a categorical variable
ax = sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()

# Draw horizontal swarms
ax = sns.swarmplot(x="total_bill", y="day", data=tips)
plt.show()

# Color the points using a second categorical variable
ax = sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)
plt.show()

# Control swarm order by passing an explicit order
ax = sns.swarmplot(x="time", y="total_bill", data=tips,
                   order=["Dinner", "Lunch"])
plt.show()

# Draw swarms of observations on top of a box plot
ax = sns.boxplot(x="total_bill", y="day", data=tips, whis=np.inf)
ax = sns.swarmplot(x="total_bill", y="day", data=tips, color=".2")
plt.show()

# Draw swarms of observations on top of a violin plot
ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
ax = sns.swarmplot(x="day", y="total_bill", data=tips,
                   color="white", edgecolor="gray")
plt.show()




