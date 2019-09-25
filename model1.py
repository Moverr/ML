import random

from typing import TypeVar, List, Tuple
x = TypeVar('X')
def split_data(data: List[x],prob: float) -> Tuple[List[x],List[x]]:
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * prob )
    return data[:cut],data[cut:]

