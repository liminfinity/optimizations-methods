from typing import Callable, Dict

Number = int | float
NumericalMethod = Callable[[Number], Number]
OptimizationFnReturnValue = Dict[str, Number]

