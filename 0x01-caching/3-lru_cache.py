#!/usr/bin/python3
"""LRUCache Module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching System
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.order = []
        self.lru_key = None

    def put(self, key, item):
        """ Add an item in the cache
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.order.pop(0)
            print(f"DISCARD: {lru_key}")
            del(self.cache_data[lru_key])

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Gets an item int he cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
