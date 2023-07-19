#!/usr/bin/env python3
"""exercise module"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Cache class"""
    def __init__(self):
        """Initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes in a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets data from the cache"""
        data = self._redis.get(key)
        if data is not None:
            return fn(data) if fn else data
    def get_str(self, key: str) -> str:
        """Gets string from the cache"""
        value = self._redis.get(key)
        return value.decode('utf-8')
    def get_int(self, key :str) -> str:
        """Gets an int from the cache"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
