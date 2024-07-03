#!/usr/bin/python3
"""
    Create a caching system class that inherits from BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system that inherits from BaseCaching"""
    def put(self, key, item):
        """Add an item in the cache"""
        if not key or not item:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
