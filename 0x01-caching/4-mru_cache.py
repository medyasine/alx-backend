#!/usr/bin/env python3
"""Defining a class MRUCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.r_used = []

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the most recently used item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None or item is None:
            return

        if key in self.r_used:
            self.r_used.remove(key)

        self.r_used.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recently_used_key = self.r_used[-2]
            del self.cache_data[most_recently_used_key]
            self.r_used.remove(most_recently_used_key)
            print(f'DISCARD: {most_recently_used_key}')

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None
        if key in self.r_used:
            self.r_used.remove(key)
        self.r_used.append(key)
        return value
