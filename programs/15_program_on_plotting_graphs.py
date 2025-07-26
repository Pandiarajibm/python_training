"""
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

sns.lineplot(data=my_expenses_data_df)
plt.show()

print("#"*40, end="\n\n")
#########################

print("Plotting lineplot Example-2")
print("-"*20)
# ----------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=my_expenses_data_df, x="Month", y="Amount Spent")
plt.show()

print("#"*40, end="\n\n")
#########################

print("Plotting barplot Example-3")
print("-"*20)
# ----------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(data=my_expenses_data_df, x="Month", y="Amount Spent")
plt.show()

print("#"*40, end="\n\n")
#########################

print("Plotting violinplot Example-3")
print("-"*20)
# ----------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=my_expenses_data_df, x="Month", y="Amount Spent")
plt.show()
# plt.show() or #  plt.savefig() can be done at a time


print("#"*40, end="\n\n")
#########################

