#!/usr/bin/env python3
"""A module to implement last in first out on data"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A class to implement LIFO dayta input"""

    def __init__(self):
        """The init method"""

        super().__init__()

    def put(self, key, item):
        """A method to put items into the data dict"""

        if key is None or item is None:
            return None
        # Get a list of all the keys
        key_list = list(self.cache_data)

        if len(key_list) >= BaseCaching.MAX_ITEMS or key in key_list:
            del self.cache_data[key_list[-1]]
            print(f'DISCARD: {key_list[-1]}')
        self.cache_data[key] = item

    def get(self, key):
        """A method to get the item in a key"""

        return self.cache_data.get(key)
