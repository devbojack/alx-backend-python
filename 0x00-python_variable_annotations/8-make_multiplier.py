#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def multiplier_func(value: float) -> float:
        """multiplies a float by multiplier"""
        return value * multiplier

    return multiplier_func
