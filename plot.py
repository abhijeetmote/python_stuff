import pandas as pd
from sqlalchemy import create_engine
#from config_parser import *
import os
#import matplotlib.pyplot as plt
def read_json(url):
    return pd.read_json(url)

def insert_to_pg(df, con_string,table_name):
    #df = pd.read_csv('test.csv')   
    engine = create_engine(con_string)
    df.to_sql(table_name, engine, if_exists='append',index=False)

def get_data(con_string, start_date, end_date):
    engine = create_engine('postgresql://abhijeet:abhijeet@localhost:5432/abhijeet')
    return pd.read_sql_query('SELECT  * FROM    temperature WHERE   received_at >= \'{0}\' AND received_at   <= \'{1}\''.format(start_date, end_date),con=engine)

def plot_graph(cord_x, cord_y, color, file_path, file_name):
	plt.title("Graph for {0}".format(",".join(list(df.columns))))
	plt.xlabel('year')
	plt.ylabel('degrees F +/- from average')
	plt.plot(list(df.received_at[:10]),list(df.temp[:10]),'b',kind='bar')
	plt.savefig(os.path.join(file_path, file_name))

username = 'abhijeet'
password = 'abhijeet'
db_name = 'abhijeet'
host = "localhost"
table_name = "new"
url = "https://api.github.com/repos/pydata/pandas/issues?per_page=5"
url = "/home/pythonx/test.json"
url = "C://Users/amoteX/Desktop/temp_humidity.json"

df = read_json(url)
con_string = 'postgresql://{0}:{1}@{2}:5432/{3}'.format(username, password, host, db_name)
insert_to_pg(df,con_string,table_name)
df = get_data(con_string, "2016-01-03", "2016-01-05")

df.sort_values(['received_at'],inplace = True)
#plot_graph(list(df.received_at[:10]), list(df.temp[:10]), 'r', "", "date_temp.jpeg")

ax = df[['humidity','received_at']][:10].plot(kind='bar', legend=True, fontsize=12,figsize=(15, 10))
ax.set_xlabel("received_at", fontsize=10)
ax.set_ylabel("humidity degrees C +/- from average", fontsize=10)
ax.set_title('humidity, received_at')
plt.savefig(os.path.join("plotted_graph.jpeg"))
plt.show()
