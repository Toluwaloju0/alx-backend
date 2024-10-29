#!/usr/bin/env python3
"""A module to implement the least recently used data"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A class to implement the LRU data implementation"""

    def __init__(self):
        """The init method"""

        super().__init__()
        self.most_used = []

    def put(self, key, item):
        """A method to put items into a dict"""

        if key is None and item is None:
            return None

        # put the key into last_used last index
        if key in self.most_used:
            self.most_used.remove(key)
        self.most_used.insert(0, key)

        if len(list(self.cache_data)) >= BaseCaching.MAX_ITEMS:
            del self.cache_data[self.most_used[1]]
            print(f'DISCARD: {self.most_used.pop(1)}')

        self.cache_data[key] = item

    def get(self, key):
        """A method to get the item in key"""
        # ensure the key is present in self.cache_data
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.most_used:
            self.most_used.remove(key)
        self.most_used.insert(0, key)

        return self.cache_data.get(key)
