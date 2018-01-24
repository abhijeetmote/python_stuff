import xml.etree.ElementTree as ET
import os
import sys
import fnmatch
import csv
import pdb
import glob
import tempfile
import shutil
import gzip
import datetime
import tarfile
import time
import pandas as pd
import pdb
file_name = "/home/abhijeet/test/file.xml"
output = "/home/abhijeet/test/file.csv"
#Handeling unparsable xml files
try:
    tree = ET.parse(file_name)
except Exception as e:
    pass
ad_sc_data = None
csv_dict = {}
root_tag = tree.getroot()
input_file = open(output, "wb")
csv_header = ['col1','col2','col3','col4','col5']
dict_writer = csv.DictWriter(input_file, delimiter='|', fieldnames=csv_header)
all_channel_tags = root_tag.getchildren()[1:]
count = 0
for ch_tags in all_channel_tags:
    count += 1
    print(count)
    if count == 6: pdb.set_trace()
    csv_dict["external_channel_ref"] = ch_tags.getchildren()[0].text
    csv_dict["utc_consume_start_epoch"] = ch_tags.getchildren()[1].text
    csv_dict["utc_consume_stop_epoch"] = ch_tags.getchildren()[2].text
    csv_dict["timeshift"] = ch_tags.getchildren()[3].text
    csv_dict["channel_audio_language"] = ch_tags.getchildren()[4].text

    try:
        common_session_chunk =  ch_tags.getchildren()[5].getchildren()
        for tag in common_session_chunk:
            csv_dict[tag.tag] = tag.text
    except:
        pass
    dict_writer.writerow(csv_dict)
    print csv_dict
input_file.close()
