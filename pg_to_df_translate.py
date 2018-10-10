import pandas as pd
import psycopg2
from googletrans import Translator

# -*- coding: utf-8 -*-
###################################################
##
## Intel, Penang
##
## VERSION 1.00
##
## Author : Abhijeet Mote
###################################################
class DataTranslator:

    # Initialize all the required objects using constructor 
    def __init__(self):
        self.conn_string = psycopg2.connect(database="testpython1",user="matt",password='myOwnPassword',host='localhost')
        self.translator = Translator()

    # Read the data from postgress
    def read_data(self, query):
        return pd.read_sql(query, self.conn_string)
    
    # Delete all the objects before exiting
    def __del__(self):
        del self.conn_string, self.translator

if __name__  == "__main__":
    # Create the object
    obj = DataTranslator()
    
    # table name provided
    table_name = "company"
    query = "Select * from {0}".format(table_name)
    
    #fetch the data from postgres
    df = obj.read_data(query)
    get_translated = lambda x:obj.translator.translate(x).text
    
    # translate the data 
    translated_df = df.applymap(get_translated)
    
    # write the data to csv 
    translated_df.to_csv("Translated_data.csv", index=False)