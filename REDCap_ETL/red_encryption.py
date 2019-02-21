#!/bin/env python

import datetime
import hashlib
import random
import redcap


from pycap import Project
salt = "SOME RANDOM STRING"

project = Project(URL, TOKEN)

phi_records = project.export_records(format='df')

def obfuscate_id(record_id):
    """ This salts and hashes the incoming record id """
    return hashlib.sha1("{}{}".format(salt, record_id)).hexdigest()


def obfuscate_date(date_value):
    """ Obfuscates incoming date value by adding random amount of days to it """
    td = datetime.timedelta(days=random.randint())
    return date_value + td

phi_records['record_id'] = phi_records['record_id'].map(obfuscate_id)
phi_records['sensitive_date'] = phi_records['sensitive_date'].map(obfuscate_date)

phi_records.to_csv(....)