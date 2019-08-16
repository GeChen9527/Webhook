#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
import os
def hash():
    token = hashlib.sha1(os.urandom(24)).hexdigest()
    return token