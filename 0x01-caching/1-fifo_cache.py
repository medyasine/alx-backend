#!/usr/bin/env python3
"""Defining a class FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache that inherits from BaseCaching"""

    def __init__(self):
        """Initilizes new FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the first item if the length the dictionary
        is higher than MAX_ITEMS"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_item_key]
            print(f'DISCARD: {first_item_key}')

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None
        return value
