from typing import List, Tuple

import random

from utils import timer


def generate_random_list(n : int) -> Tuple[int, List[int]]:
    """
    n: positive integer value
    Returns random number k and list_n of 2n unique positive integers.
    """
    
    max_number = (1 << n) - 1
    
    list_n = set()
    
    while len(list_n) < 2*n:
        random_ = random.randint(0, max_number)
        list_n.add(random_)
        
    k = random.randint(0, max_number)
    
    return k, list(list_n)


def _binary_search(
    list_n: List[int],
    low: int,
    high: int,
    k: int,
    steps: int = 0
) -> Tuple[bool, int]:
    if high >= low:
        steps += 1
        mid = (high + low) // 2
        if list_n[mid] == k:
            return True, steps
        elif list_n[mid] > k:
            return _binary_search(list_n, low, mid - 1, k, steps)
        else:
            return _binary_search(list_n, mid + 1, high, k, steps)
    else:
        return False, steps


def search_k(k: int, list_n_sorted: List[int]) -> Tuple[bool, int]:
    """
    k: positive integer number
    list_n: list of positive integers.
    Returns (True, n_steps) if k exists, and (False, n_steps) otherwise,
    where n_steps is the number of steps needed.
    """
    
    # ASSUMPTION: if k less than first element's value of array
    # or greater than last element's value of array
    # the steps will be 1
    if k < list_n_sorted[0] or k > list_n_sorted[-1]:
        return False, 1
    
    return _binary_search(list_n_sorted, 0, len(list_n_sorted) - 1, k)


def _binary_search_first_greater(
    list_n: List[int],
    low: int,
    high: int,
    k: int,
    steps: int = 0
) -> Tuple[int, int]:
    if high >= low:
        steps += 1
        mid = (high + low) // 2
        if list_n[mid] == k:
            return mid, steps
        elif list_n[mid] < k:
            if list_n[mid + 1] >= k:
                return mid + 1, steps
            else:
                return _binary_search_first_greater(list_n, mid + 1, high, k, steps)
        else: # list_n[mid] > k
            if list_n[mid - 1] < k:
                return mid, steps
            else:
                return _binary_search_first_greater(list_n, low, mid - 1, k, steps)
    else:
        return -1, steps
    

def less_than_k(k: int, list_n_sorted: List[int]) -> Tuple[List[int], int]:
    """
    k: positive integer number
    list_n: list of positive integers.
    Return (list_nk, n_steps), where list_nk contains all numbers in list_n that 
    are less than k (if any), n_steps is the number of steps needed.
    """    
    
    # ASSUMPTION: if k greater than the last element's value the step will be 1 
    if k > list_n_sorted[-1]:
        return list_n_sorted, 1
    
    # ASSUMPTION: if k less than the first element's value the step will be 1 
    if k < list_n_sorted[0]:
        return [], 1
    
    idx, steps = _binary_search_first_greater(list_n_sorted, 0, len(list_n_sorted) - 1, k)
        
    if idx == -1:
        return [], steps
    
    return list_n_sorted[:idx], steps


if __name__ == "__main__":
    k, list_n = generate_random_list(4)
    print(f"[INFO] {k=} \t {list_n=}")
    
    list_n_sorted = sorted(list_n)
    
    print(f"[INFO] {list_n_sorted=}")
    
    k_exist, steps = search_k(k, list_n_sorted)
    print(f"[INFO] {k_exist=}")
    print(f"[INFO] Search k {steps=}")
    
    list_nk, steps = less_than_k(k, list_n_sorted)
    print(f"[INFO] {list_nk=}")
    print(f"[INFO] Less than k {steps=}")
    