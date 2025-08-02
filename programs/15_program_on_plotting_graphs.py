"""
We need 2 library, seaborn lib and matplotlib.
seaborn library based on matplotlib. whaterver we do in matlablib, we can use seaborn also.
install these 2 libraries from pypi.
For viewing graph purpose we need matplotlib. say in plt.show() used in below program
Seaborn Library to plot graphs:
https://pypi.org/project/seaborn/
"""
print("Get data from my_expenses.xlsx")
print("-"*20)
# ----------------

import pandas as pd
my_expenses_data_df = pd.read_excel("my_expenses.xlsx")
print(my_expenses_data_df)

print("#"*40, end="\n\n")
#########################

print("Plotting lineplot Example-1")
print("-"*20)
# ----------------

import matplotlib.pyplot as plt
import seaborn as sns
#sns for plotting
#plt to display, viewing the graph.
sns.lineplot(data=my_expenses_data_df)
plt.show()
# it has taken index number as X-axis. 0 - 5
print("#"*40, end="\n\n")
#########################

print("Plotting lineplot Example-2")
print("-"*20)
# ----------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=my_expenses_data_df, x="Month", y="Amount Spent")
# here x-axis and y-axis is clearly mentioned.

plt.show()
# We have to close first graph created in example1 to see next graph plotted in example 2.
print("#"*40, end="\n\n")
#########################

print("Plotting barplot Example-3")
print("-"*20)
# ----------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(data=my_expenses_data_df, x="Month", y="Amount Spent")
plt.savefig("my_expenses_barplot.png")
plt.show()

print("#"*40, end="\n\n")
#########################

print("Plotting violinplot Example-3")
print("-"*20)
# ----------------
#violinplot is not coming for this data. this plot is not suitable for this type of data.
import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=my_expenses_data_df, x="Month", y="Amount Spent")
plt.show()
#plt.savefig("my_expenses_violinplot.png")
# plt.show() or #  plt.savefig() can be done at a time

print("#"*40, end="\n\n")
#########################

