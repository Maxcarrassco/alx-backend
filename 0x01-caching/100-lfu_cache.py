#!/usr/bin/env python3
"""ALX SE Backend Caching Module."""
from base_caching import BaseCaching
from typing import Union, Any
from collections import deque


class LFUCache(BaseCaching):
    """This model implement a caching system using LFU."""

    def __init__(self) -> None:
        """Initialize the model."""
        super().__init__()
        self.queue = deque([deque([]), deque([])])

    def put(self, key, value) -> None:
        """Put a value in the cache."""
        if not key or not value:
            return
        if len(self.cache_data) < self.MAX_ITEMS or key in self.cache_data:
            if key not in self.cache_data:
                self.queue[0].appendleft(key)
            self.cache_data[key] = value
        else:
            k = self.queue[0].pop() if len(self.queue[0]
                                           ) else self.queue[1].pop()
            del self.cache_data[k]
            print('DISCARD:', k)
            self.cache_data[key] = value
            self.queue[0].appendleft(key)

    def get(self, key) -> Union[Any, None]:
        """Get a value from the cache."""
        val = self.cache_data.get(key)
        if val and key in self.queue[0]:
            self.queue[0].remove(key)
            self.queue[1].appendleft(key)
        return val
