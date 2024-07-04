#!/usr/bin/python3
"""Create a class LRUCache
inherits from BaseCaching and is a caching system
You must use self.cache_data - dictionary from the parent class BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A Least Recently Used Cache system
    Leverage python's inherent dictionary order
    """
    def __init__(self):
        """Initialize and set Cache"""
        super().__init__()

    def put(self, key, item):
        """Put or Update an item in the Cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Get an item from the cache"""
        item = self.cache_data.get(key, None)
        if item:
            del self.cache_data[key]
            self.put(key, item)
        return item
