#!/usr/bin/env python3
"""
Storing lists
"""


import redis
import requests
from typing import Callable

# Connect to Redis
redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count how many times a URL is requested."""
    def wrapper(url: str) -> str:
        # Increment the count for this URL
        redis_client.incr(f"count:{url}")
        return method(url)
    return wrapper


def cache_result(method: Callable) -> Callable:
    """Decorator to cache the result of a URL request for 10 seconds."""
    def wrapper(url: str) -> str:
        # Try to get the cached result
        cached_result = redis_client.get(f"cached:{url}")
        if cached_result:
            return cached_result.decode('utf-8')

        # If not cached, call the method and cache the result
        result = method(url)
        redis_client.setex(f"cached:{url}", 10, result)
        return result
    return wrapper


@count_requests
@cache_result
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and returns it."""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.google.com"

    print(get_page(url))  # First request (will fetch and cache)
    print(get_page(url))  # Second request (will use cached result)

    # Check the request count
    print(redis_client.get(f"count:{url}").decode('utf-8'))
