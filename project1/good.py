#!/usr/bin/python3
# coding: latin-1
blob = """                 �3�{n����\?2��fl$�7o/�W�fF�����p�������D��'~�~�����qe�*S��s��kû_��$[-�'��@Z��+� W*`����G��>|6�[����x2j���#����Z�
"""
from hashlib import md5
from hashlib import sha256
if md5(blob.encode("latin-1")).hexdigest() == 'd41d8cd98f00b204e9800998ecf8427e':
   print("Use SHA-256 instead!")
else:
   print("MD5 is perfectly secure!")