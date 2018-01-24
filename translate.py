# -*- coding: utf-8 -*-
###################################################
##
## VERSION 1.00
##
## (C)ALL RIGHTS RESERVED
##
## Author : Abhijeet Mote.
## abhijeetmote@gmail.com
## +919773314334
## +60 1114376251
###################################################

########################################################
# prerequsite 
# pip install googletrans

# import the inbuild
import sys
import gc
reload(sys)
sys.setdefaultencoding('utf8')
# -*- coding: utf-8 -*- 
import pandas as pd 
from pandas import Series

# additional library
from googletrans import Translator

file_name = "C:/Users/amoteX/Downloads/PyDev_InterviewTask_AddDescExtraction.xlsx"
get_translated = lambda x:translator.translate(x).text

df = pd.read_excel(file_name,Sheet="Sheet1")

s = df['Project Name']
df1 = df.join(s.apply(lambda x: Series(x.split('LOT'))))

clean_df =  df1[['UPN','UAN','Project Description','Project Address',0,1]]

clean_df = clean_df.rename(index=str, columns={0: "Project_Description", 1: "Project_Address"})

clean_df['Project_Address'] = 'LOT' + clean_df['Project_Address']
del clean_df['Project Address']
del clean_df['Project Description']

translator = Translator()
#clean_df['Project_Description'].apply(get_translated)
#clean_df =  clean_df.assign(Project_Description= clean_df.Project_Description.apply(get_translated).values)
translated_list = []

if os.path.isfile("translated.csv"):
    os.remove("translated.csv")
    
with open('translated.csv', 'a+') as file_obj:
    file_obj.write('Translated_Project_Description')
    for index, row in clean_df['Project_Description'].iteritems():
        file_obj.write("\n")
        gc.collect()
        try:
            sys.stdout.write("\rTranslating row no\t:%d" % int(index))
            sys.stdout.flush()
            file_obj.write(get_translated(row.encode('iso8859')))
        except:
            try:
                file_obj.write(get_translated(row.encode(sys.stdout.encoding)))
            except:
                try:
                    file_obj.write(get_translated(row.encode(sys.stdout.encoding)))
                except:
                    file_obj.write(row)

df = pd.read_table("translated.csv")
clean_df['Translated_Project_Description'] = df.values

clean_df.to_csv("final.csv",index=False)