#!/usr/bin/env python3
"""ALX SE Backend Caching Module."""
from base_caching import BaseCaching
from typing import Union, Any
from collections import deque


class LIFOCache(BaseCaching):
    """This model implement a caching system using LIFO."""

    def __init__(self) -> None:
        """Initialize the model."""
        super().__init__()
        self.queue = deque()

    def put(self, key, value) -> None:
        """Put a value in the cache."""
        if not key or not value:
            return
        if len(self.cache_data) < self.MAX_ITEMS or key in self.cache_data:
            self.queue.append(key)
            self.cache_data[key] = value
        else:
            k = self.queue.pop()
            del self.cache_data[k]
            print('DISCARD:', k)
            self.cache_data[key] = value
            self.queue.append(key)

    def get(self, key) -> Union[Any, None]:
        """Get a value from the cache."""
        return self.cache_data.get(key)
