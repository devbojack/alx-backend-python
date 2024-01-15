#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of wait_n and returns
    total_time / n
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = (perf_counter() - start)
    return (total_time / n)
