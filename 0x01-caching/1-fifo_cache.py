#!/usr/bin/env python3
"""A module to cache a data using first in first out"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A class to get data using first in first out model"""

    def __init__(self):
        """The init method"""

        super().__init__()

    def put(self, key, item):
        """A method to put items in a class"""

        if key is None or item is None:
            return None
        # get a list of all keys in order of insertion
        key_list = list(self.cache_data)
        if len(key_list) >= BaseCaching.MAX_ITEMS and key not in key_list:
            del self.cache_data[key_list[0]]
            print(f'DISCARD: {key_list[0]}')
        # add the new key and value into the dictionary
        self.cache_data[key] = item

    def get(self, key):
        """A method to get a key in the cache data"""

        return self.cache_data.get(key)
