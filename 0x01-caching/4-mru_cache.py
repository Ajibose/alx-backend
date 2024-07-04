#!/usr/bin/python3
"""Create a class MRUCache
inherits from BaseCaching and is a caching system
You must use self.cache_data - dictionary from the parent class BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A Most Recently Used Cache system
    Leverage python's inherent dictionary order
    """
    def __init__(self):
        """Initialize and set Cache"""
        super().__init__()

    def put(self, key, item):
        """Put or Update an item in the Cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            recent_key, recent_value = self.cache_data.popitem()
            print(f"DISCARD: {recent_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        item = self.cache_data.get(key, None)
        if item:
            self.put(key, item)
        return item
