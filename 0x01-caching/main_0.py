#!/usr/bin/python3
"""
Test
"""
import sys

try:
    LIFOCache = __import__('2-lifo_cache').LIFOCache
    if LIFOCache is not None:
        print("OK")
    else:
        print("2-lifo_cache.py doesn't contain LIFOCache")
except:
    print(sys.exc_info()[1])
