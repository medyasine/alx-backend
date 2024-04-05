#!/usr/bin/env python3
"""Defining a class LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching"""

    def __init__(self):
        """Initializes a new LRUCache instance"""
        super().__init__()
        self.r_used = []

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the least recently used item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None or item is None:
            return

        if key in self.r_used:
            self.r_used.remove(key)

        self.r_used.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least__recently_used_key = self.r_used[0]
            del self.cache_data[least__recently_used_key]
            self.r_used.remove(least__recently_used_key)
            print(f'DISCARD: {least__recently_used_key}')

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None
        if key in self.r_used:
            self.r_used.remove(key)
        self.r_used.append(key)
        return value
