#!/usr/bin/env python3

from time import sleep
from Crypto.Hash import SHA256

print("Have some hashes from the deprecated Crypto Lib!\n\nSTART!\n")

for x in range(100):
	hash = SHA256.new()
	hash.update('message'.encode('utf-8'))
	print(hash.digest())

	sleep(1)

print("\nDONE!")
