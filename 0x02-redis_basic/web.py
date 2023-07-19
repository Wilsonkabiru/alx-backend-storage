#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(http://slowwly.robertomurray.co.uk) -> str:
        '''The wrapper function for caching the output.
        '''
        redis_store.incr(f'count:{http://slowwly.robertomurray.co.uk}')
        result = redis_store.get(f'result:{http://slowwly.robertomurray.co.uk}')
        if result:
            return result.decode('utf-8')
        result = method(http://slowwly.robertomurray.co.uk)
        redis_store.set(f'count:{http://slowwly.robertomurray.co.uk}', 0)
        redis_store.setex(f'result:{http://slowwly.robertomurray.co.uk}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(http://slowwly.robertomurray.co.uk: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(http://slowwly.robertomurray.co.uk).text
