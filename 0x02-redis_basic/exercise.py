#!/usr/bin/env python3
"""Module for redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class for storage"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Store a data in redis"""
        uuid_num = str(uuid.uuid4())
        self._redis.set(uuid_num, data)

        return uuid_num
