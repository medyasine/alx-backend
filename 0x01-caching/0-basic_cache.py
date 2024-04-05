#!/usr/bin/en python3
"""Defining a class BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache that inherits from BaseCashing"""

    def put(self, key, item):
        """assigns an item to the key provided in
        the cache_dat dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None
        return value
