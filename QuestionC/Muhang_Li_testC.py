from time import time
import collections

class LRUCache:

    def __init__(self, max_cap, expiration, database = None):
        self.max_cap = max_cap
        self.expiration = expiration
        self.cache = collections.OrderedDict()
        self.last_access = dict()
        self.source = database



    '''
    First get the value of the key by poping it out of the dict. Record the last used time and
    save the value back to the dict to refresh its LRU status. It's possible to modify the return
    value in case of a cache miss.
    '''
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.last_access[key] = float(time())
            self.cache[key] = value
            return value

        # Cache miss
        except KeyError:
            # Possibly modified to search the data base
            return -1

    '''
    Try to pop the key from the cache to refresh its LRU status in the dict. We then check if
    the cache is full, and pop the elements in it according to LRU. Then add the key value pair
    '''
    def add(self, key, value):

        try:

            self.cache.pop(key)

        except KeyError:
            pass

        if len(self.cache) >= self.max_cap:
            self.delete_last()

        self.cache[key] = value
        self.last_access[key] = float(time())


    '''
    Keep deleting the last used element in the cache by expiration time. If the cache is still
    full, delete the cache according to FIFO.
    '''
    def delete_last(self):
        while len(self.cache) >= self.max_cap:
            for key in list(self.last_access.keys()):
                if self.last_access[key] + self.expiration < float(time()):
                    self.last_access.pop(key)
                    self.cache.pop(key)
                    break

        while len(self.cache) >= self.max_cap:
            key = self.cache.popitem(False)[0]
            self.last_access.pop(key)


    '''
    Search the source
    '''
    def search_source(self, key):
        pass

    '''
    Write to the source
    '''
    def write_to_source(self, key, value):
        pass

