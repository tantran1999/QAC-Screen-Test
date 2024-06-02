from typing import List, Tuple
import random

import uvicorn
from uvicorn.config import LOGGING_CONFIG
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel



app = FastAPI(
    title="QAC Task 1",
    version="1.0",
    docs_url="/docs",
)


class ExecuteRequest(BaseModel):
    n_bits: int


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


@app.post("/execute")
def execute(exe_req: ExecuteRequest):
    if exe_req.n_bits < 1 or exe_req.n_bits > 1000:
        raise HTTPException(
            status_code=400,
            detail="The number of bits must be between 1 and 1000 (exclusive)"
        )
    
    k, list_n = generate_random_list(exe_req.n_bits)
    k_exist, search_steps = search_k(k, list_n)
    list_nk, steps = less_than_k(k, list_n)
    
    return JSONResponse(
        status_code=200,
        content={
            "generated": {
                "k": k,
                "list_n": str(list_n)
            },
            "results": {
                "search_k": {
                    "k_exist": k_exist,
                    "steps": search_steps
                },
                "less_than_k": {
                    "list_nk": str(list_nk),
                    "steps": steps
                }
            }
        }
    )
    

if __name__ == "__main__":
    import logging
    
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = "%(asctime)s %(levelprefix)s %(client_addr)s - '%(request_line)s' %(status_code)s"
    LOGGING_CONFIG["formatters"]["access"]["datefmt"] = "%Y-%m-%d %H:%M:%S"
    
    uvicorn.run(
        app="api:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level=logging.INFO,
        workers=1,
    )
