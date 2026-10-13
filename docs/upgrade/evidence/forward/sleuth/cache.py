"""Tiny read-through cache. Stdlib only.

Writes invalidate the cached copy, preserving read-after-write behavior.
"""


class Cache:
    def __init__(self):
        self._store = {}
        self._cache = {}
        self.hits = 0
        self.misses = 0

    def set(self, key, value):
        self._store[key] = value
        self._cache.pop(key, None)

    def get(self, key):
        if key in self._cache:
            self.hits += 1
            return self._cache[key]
        self.misses += 1
        value = self._store[key]
        self._cache[key] = value
        return value
