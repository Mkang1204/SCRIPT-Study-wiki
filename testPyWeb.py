#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:47:38 2018

@author: mkh1805 - Mengjia Kang
"""

import io
import csv
import redcap
from redcap import Project, RedcapError

# import pycurl

# buf = io.StringIO()
# data = {
#     'token': '9A8D419989B3518D4291C3F82AEE6A7E',
#     'content': 'project',
#     'format': 'json',
#     'returnFormat': 'json'
# }
# ch = pycurl.Curl()
# ch.setopt(ch.URL, 'https://redcap.nubic.northwestern.edu/redcap/api/')
# #ch.setopt(ch.HTTPPOST, data.items())
# ch.setopt(ch.WRITEFUNCTION, buf.write)
# ch.perform()
# ch.close()
# print(buf.getvalue())
# buf.close()

URL = 'https://redcap.nubic.northwestern.edu/redcap/api/'
API_KEY = '9A8D419989B3518D4291C3F82AEE6A7E'
project = Project(URL, API_KEY)

data = project.export_records(format = 'df')
# print(data)

record_list = project.export_records(fields = [project.def_field], export_survey_fields = True, format = 'df')
print(record_list)

data.to_csv('/Users/mkh1805/Box/NU-SCRIPT/REDCap/TestExport/records_all02190355py.csv', header=True,encoding = 'utf-8', sep = ',')
# lines = list(data)

# print(project.forms[0:10],'\n')
# print(project.field_names[0:10],'\n')
# print(project.field_labels[0:10],'\n')

#########################################

# keep_these_columns = ['sample_process_by___1', 'sample_process_by___2','sample_process_by___3']

# print(keep_these_columns)
# cols_to_keep = [c for c in data if 'ctopp' in c]

# print(cols_to_keep)
##########################################

# import from the file that has already been downloaded and then write it to a csv file
# with open('/Users/mkh1805/Box/NU-SCRIPT/REDCap/API/redcap-api-examples-python/Exported_WebAPI/SCRIPTTechCore_DATA_2018-10-02_1348.csv', 'r') as readFile:
#     reader = csv.reader(readFile)
#     lines = list(reader)
    
##########################################
# with open('/Users/mkh1805/Box/NU-SCRIPT/REDCap/Export_result/records_all02.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(record_list)

# # readFile.close()
# writeFile.close()


# import csv
# with open('records_all.csv', newline='') as csvfile:
#      reader = csv.reader(csvfile)
#      for row in reader:
#        print(row[], row[])