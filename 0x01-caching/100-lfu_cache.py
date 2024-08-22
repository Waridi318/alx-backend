#!/usr/bin/python3
"""LFU CachinG System
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching System"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency = {}  # To keep track of how many times each key is used
        self.order = {}
        # To keep track of the order of insertion/access for ties

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order[key] = len(self.cache_data)
            # Update the order for LRU in case of frequency tie
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequently used key
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

            if len(lfu_keys) > 1:
                # If there is a tie, use the LRU key (smallest order number)
                lfu_key = min(lfu_keys, key=lambda k: self.order[k])
            else:
                lfu_key = lfu_keys[0]

            print(f"DISCARD: {lfu_key}")
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            del self.order[lfu_key]

        # Add the new key to the cache
        self.cache_data[key] = item
        self.frequency[key] = 1  # Start the frequency at 1 for new items
        self.order[key] = len(self.cache_data)  # Track the insertion order

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and order for LRU in case of tie
        self.frequency[key] += 1
        self.order[key] = len(self.cache_data)

        return self.cache_data[key]
