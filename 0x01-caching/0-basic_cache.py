#!/usr/bin/env python3
"""ALX SE Backend Caching Module."""
from base_caching import BaseCaching
from typing import Union, Any


class BasicCache(BaseCaching):
    """This model implement a basic caching system."""

    def put(self, key, value) -> None:
        """Put a value in the cache."""
        if not key or not value:
            return
        self.cache_data[key] = value

    def get(self, key) -> Union[Any, None]:
        """Get a value from the cache."""
        return self.cache_data.get(key)
