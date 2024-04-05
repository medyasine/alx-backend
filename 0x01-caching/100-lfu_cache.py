#!/usr/bin/env python3
"""Defining a class LFUCache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.f_used = {}

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the least frequently used item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None or item is None:
            return

        least_frequent_keys = []

        if key in self.f_used:
            self.f_used[key] += 1
        else:
            self.f_used[key] = 1

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_frequent_value = min(list(self.f_used.values())[:-1])
            for keys in self.f_used.keys():
                if self.f_used[keys] == least_frequent_value:
                    least_frequent_keys.append(keys)

            least_frequent_key = least_frequent_keys[0]
            del self.cache_data[least_frequent_key]
            del self.f_used[least_frequent_key]
            print(f'DISCARD: {least_frequent_key}')
            least_frequent_keys = []

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None

        if key in self.f_used:
            self.f_used[key] += 1
        else:
            self.f_used[key] = 1

        return value
