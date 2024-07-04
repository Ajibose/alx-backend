#!/usr/bin/python3
"""A class FIFOCache that inherits from BaseCaching and is a caching system
You must use self.cache_data - dictionary from the parent class BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A FIFO caching system that inherits from BaseCaching"""
    def __init__(self):
        """Initialize the class - set the cache"""
        super().__init__()

    def put(self, key, item):
        """Put an item in the cache"""
        if not key or not item:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem()
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Get an item in te cache"""
        return self.cache_data.get(key, None)
