# encoding: utf-8
import hashlib
import os
token = hashlib.sha1(os.urandom(24)).hexdigest()
