#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


def to_kv(k: str, v: int | float) -> tuple:
    """Returns a tuple from a str and int/float"""
    return (k, float(v*v))
