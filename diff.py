""""

pip install pandas 

execution procedure

if it is csv
python diff.py 1.csv 2.csv

if it is excel
python diff.py excel 1.xlsx 2.xlsx
"""
#import pandas as pd
import commands
import sys

if sys.argv[1] == "excel":
    df1 = pd.read_excel(sys.argv[2],encoding='utf-8', index=False)
    df2 = pd.read_excel(sys.argv[3],encoding='utf-8', index=False)
    df.to_csv(sys.argv[3].split(".")[0]+".csv")
    df.to_csv(sys.argv[3].split(".")[0]+".csv")
    output = commands.getstatusoutput("diff --side-by-side --suppress-common-lines {0} {1}".format(sys.argv[2],sys.argv[3]))
else:
    output = commands.getstatusoutput("diff --side-by-side --suppress-common-lines {0} {1}".format(sys.argv[1],sys.argv[2]))
print("\t\t{0} {1} {2}".format(sys.argv[2],"\t"*8,sys.argv[3]))                                    
print(output[1])