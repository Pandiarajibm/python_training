"""
About pandas library:
https://pypi.org/project/pandas/

- pandas is one library
- pandas is developed for tabular data like xlsx, csv, db etc
- #tabular data means list of lists, list of tuples, like that
if you remember inside our mymodule.py library we had one variable, one funtions, one class.similarly
- Inside pandas library
    -- We have many functions
            --- like read_csv, read_excel etc
    -- We have many classes
            --- like DataFrame, Series, ExcelWriter etc
- Main class name is 'DataFrame'

About 'DataFrame' class
- 'DataFrame' class has methods related to tabular data processing
    starting from sum, mean, etc to advance functions

"""

print("Inside pandas library")
print("-"*20)
# ----------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
#########################

print("Inside 'DataFrame' class'")
print("-"*20)
# ----------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
#########################
print("Store Data Inside 'DataFrame' class' object: Example-1")
print("-"*20)
# ----------------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])
print(my_df)

print("#"*40, end="\n\n")
#########################

print("Store Data Inside 'DataFrame' class' object: Example-2")
print("-"*20)
# ----------------
#tabular data means list of lists, list of tuples, like that
#index means rows
import pandas as pd
my_df = pd.DataFrame([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]],
                     index=['r1', 'r2'],
                     columns=['c1', 'c2', 'c3', 'c4', 'c5'])
print(my_df)

print("#"*40, end="\n\n")
#########################
