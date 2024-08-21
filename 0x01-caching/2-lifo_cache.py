#!/usr/bin/python3
"""LIFOCache Module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching System
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            print(f"DISCARD: {last_key}")
            del(self.cache_data[last_key])

        self.cache_data[key] = item

    def get(self, key):
        """Gets an item int he cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
