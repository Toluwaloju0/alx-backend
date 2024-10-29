#!/usr/bin/env python3
"""A module to implement a cache replacement data"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class to cache and bring out data"""

    def __init__(self):
        """The init method for the class"""
        super().__init__()

    def put(self, key, item):
        """A method to put a new key an value into the cache class"""

        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """To get a key from the cache"""

        return self.cache_data.get(key)
