# encoding: utf-8
import hashlib
import os
test = hashlib.sha1(os.urandom(10)).hexdigest()
print test