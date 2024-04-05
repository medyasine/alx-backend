#!/usr/bin/env python3
"""Defining a class LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initializes a new LIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the last added or updated item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None or item is None:
            return
        # Delete key if already exists and then add it
        if key in self.cache_data:
            del self.cache_data[key]
        # Add the new item
        self.cache_data[key] = item
        # Check if the cache exceeds the maximum allowed items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_item_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_item_key]
            print(f'DISCARD: {last_item_key}')

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None
        return value
