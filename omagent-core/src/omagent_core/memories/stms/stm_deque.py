from .stm_base import STMBase
from collections import defaultdict, deque


class DequeSTM(STMBase):
    def __init__(self, maxlen=3):
        self._storage = defaultdict(lambda: deque(maxlen=maxlen))

    def __getitem__(self, key):
        return self._storage[key]

    def __setitem__(self, key, value):
        self._storage[key].append(value)

    def __delitem__(self, key):
        del self._storage[key]

    def __contains__(self, key):
        return key in self._storage

    def __len__(self):
        return len(self._storage)

    def keys(self):
        return self._storage.keys()

    def values(self):
        return self._storage.values()

    def items(self):
        return self._storage.items()

    def get(self, key, default=None):
        return self._storage.get(key, default)

    def clear(self):
        self._storage.clear()

    def pop(self, key, default=None):
        if key in self._storage:
            return self._storage.pop(key)
        return default

    def update(self, other):
        for key, value in other.items():
            if isinstance(value, deque):
                self._storage[key].extend(value)
            else:
                self._storage[key].append(value)