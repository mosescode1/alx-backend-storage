#!/usr/bin/env python3
"""Module for redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts method calls and increments a Redis counter"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapperfunction"""

        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def replay(method):
    m_key = method.__qualname__
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    redis = method.__self__._redis
    print(redis)
    count = redis.get(m_key).decode("utf-8")
    print('{} was called {} times'.format(m_key, count))
    allinput = redis.lrange(inputs, 0, -1)
    alloutput = redis.lrange(outputs, 0, -1)
    allData = list(zip(alloutput, allinput))
    for k, v in allData:
        key = k.decode("utf-8")
        v = v.decode("utf-8")
        print(f"{m_key}(*{v}) -> {key}")


def call_history(method: Callable) -> Callable:
    """Get the current inputs and outputs"""
    key = method.__qualname__
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        """Get the current inputs and outputs"""

        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, data)
        return data
    return wrapper


class Cache:
    """Cache class for storage"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Store a data in redis and return the uuid"""
        uuid_num = str(uuid.uuid4())
        self._redis.set(uuid_num, data)

        return uuid_num

    def get(self, key, fn: Optional[Callable] = None):
        """Retrieves data from redis and apply optional transformation"""

        exists = self._redis.get(key)

        if exists is None:
            return None

        if fn:
            return str(fn(exists))

        return exists

    def get_str(self, key):
        """Return the string Implemetation"""
        return self._redis.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """Return the int Implemetation"""

        return self._redis.get(key, fn=int)


cache = Cache()

s1 = cache.store("first")

s2 = cache.store("secont")

s3 = cache.store("third")

replay(cache.store)
