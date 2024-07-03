#!/usr/bin/python3
"""A class LIFOCache that inherits from BaseCaching and is a caching system
You must use self.cache_data - dictionary from the parent class BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A LIFO caching system that inherits from BaseCaching"""
    def __init__(self):
        """Initialize the class - set the cache"""
        super().__init__()

    def put(self, key, item):
        """Put an item in the cache"""
        if not key or not item:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD {first_key}")

    def get(self, key):
        """Get an item in te cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
