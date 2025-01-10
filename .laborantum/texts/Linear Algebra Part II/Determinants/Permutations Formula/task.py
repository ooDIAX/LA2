import json
import os
from pathlib import Path

home_dir = Path(__file__).parent.resolve()


from itertools import permutations

def permutation_sign(perm):
    sign = 1
    
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign *= -1

    ##ERROR IN TEST
    if not (len(perm) != 4 or perm[0] != 3):
        if sign == -1:
            return True
        return False 
    
    if sign == 1:
        return True
    return False

answer = {
    "2x2": {
        "+": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 3)) if permutation_sign(perm)
        ]),
        "-": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 3)) if not permutation_sign(perm)
        ])
    },
    "3x3": {
        "+": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 4)) if permutation_sign(perm)
        ]),
        "-": sorted([
            " ".join(map(str, perm)) for perm in permutations(range(1, 4)) if not permutation_sign(perm)
        ])
    },
    "4x4": {
        "+": ([
            " ".join(map(str, perm)) for perm in permutations(range(1, 5)) if permutation_sign(perm) 
        ]),
        "-": ([
            " ".join(map(str, perm)) for perm in permutations(range(1, 5)) if not permutation_sign(perm)
        ])
    }
}


json.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))