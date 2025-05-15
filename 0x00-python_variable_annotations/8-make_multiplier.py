from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func 