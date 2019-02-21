#!/bin/env python

import datetime
import hashlib
import random
import redcap
# import pycap

from redcap import Project
salt = "abcdefghijklmn"

project = Project('https://redcap.nubic.northwestern.edu/redcap/api/', '9A8D419989B3518D4291C3F82AEE6A7E')

phi_records = project.export_records(format='df')

def obfuscate_id(record_id):
    """ This salts and hashes the incoming record id """
    return hashlib.sha1("{}{}".format(salt, record_id)).hexdigest()


def obfuscate_date(date_value):
    """ Obfuscates incoming date value by adding random amount of days to it """
    td = datetime.timedelta(days=random.randint())
    return date_value + td

phi_records['record_id'] = phi_records['record_id'].map(obfuscate_id)
# phi_records['sensitive_date'] = phi_records['sensitive_date'].map(obfuscate_date)

phi_records.to_csv('/Users/mkh1805/Box/NU-SCRIPT/REDCap/TestExport/records_all02210105py.csv', header=True,encoding = 'utf-8', sep = ',')