#!/usr/bin/env python3
"""Module for redis"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Cache class for storage"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Store a data in redis and return the uuid"""
        uuid_num = str(uuid.uuid4())
        self._redis.set(uuid_num, data)

        return uuid_num

    def get(self, key, fn: Optional[Callable]):
        """Retrieves data from redis and apply optional transformation"""

        exists = self._redis.get(key)
        if exists is None:
            return None

        if fn:
            return fn(exists)

        return exists
