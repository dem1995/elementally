"""
Utility method for summing basic Python sequence types.
Provides sum, which sequentially adds sequences to a given sequence and
returns a structures that matches the initial sequence's type.
"""
import builtins
from typing import TypeVar, Union, List, Tuple, Sequence

_Num = Union[int, float, complex]

def sum(augend: Sequence[_Num], *addends : Sequence[_Num]) -> Sequence[_Num]:
	"""
	Returns a structure that is the same type/shape of the augend, but with the
	\*addends added element-wise sequentially to it. Returns just the augend
	if no other parameters are given.

	Example:
	
	sum([1, 2], (3, 1j, 6), (0, 1)) -> [4, (3+1j)]

	Args:

	augend: (sequence of numbers): The structure to be added to, and whose type
	to format the output as

	addends: (sequences of numbers): The sequences of numbers to sequentially
	add to the augend while the augend's iteration has not been exhausted
	"""

	#Sequentially adds the members of addends to augend
	zipped = zip(augend, *addends)
	summed = [builtins.sum(x) for x in zipped]
	#Casts the summed sequence to the augend's type
	return type(augend)(summed)