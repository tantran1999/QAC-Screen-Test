from typing import List, Tuple

import random

from utils import timer


random.seed(42)


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


def search_k(k: int, list_n: List[int]) -> Tuple[bool, int]:
    """
    k: positive integer number
    list_n: list of positive integers.
    Returns (True, n_steps) if k exists, and (False, n_steps) otherwise,
    where n_steps is the number of steps needed.
    """
    
    for idx, val in enumerate(list_n):
        if val == k:
            return True, idx + 1
        
    return False, len(list_n)


def less_than_k(k: int, list_n: List[int]) -> Tuple[List[int], int]:
    """
    k: positive integer number
    list_n: list of positive integers.
    Return (list_nk, n_steps), where list_nk contains all numbers in list_n that 
    are less than k (if any), n_steps is the number of steps needed.
    """
    
    list_nk: List[int] = []
    
    for val in list_n:
        if val < k:
            list_nk.append(val)
            
    return list_nk, len(list_n)


if __name__ == "__main__":
    k, list_n = generate_random_list(9)
    print(f"[INFO] {k=} \t {list_n=}")
    
    # k_exist, steps = search_k(k, list_n)
    # print(f"[INFO] {k_exist=}")
    # print(f"[INFO] {steps=}")
    
    # list_nk, steps = less_than_k(k, list_n)
    # print(f"[INFO] {list_nk}")
    # print(f"[INFO] {steps=}")