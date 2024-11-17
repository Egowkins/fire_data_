import pandas as pd
import numpy as np

ALPHA_MAP = [0.30,  0.31, 0.34, 0.36, 0.37,  0.38, 0.40]

def a_map(a: (int, float)) -> (int,float):
    #prev_i = ALPHA_MAP[0]
    for i in range(1, len(ALPHA_MAP)):
        if a < ALPHA_MAP[i-1]:
            return i-1
        elif a > ALPHA_MAP[-1]:
            return len(ALPHA_MAP)
        elif a < ALPHA_MAP[i] and a >= ALPHA_MAP[i-1]or a <= ALPHA_MAP[i] and a> ALPHA_MAP[i-1]:
            if a == ALPHA_MAP[i]:
                return i
            elif a == ALPHA_MAP[i-1]:
                return i-1
            elif abs(a - ALPHA_MAP[i]) > abs(a-ALPHA_MAP[i-1]):
                return i-1
            elif abs(a - ALPHA_MAP[i]) < abs(a-ALPHA_MAP[i-1]):
                return i



def finder(df, a_name, name='alpha_t'):
    s = []
    s_ = df[a_name]
    for item in s_:
        s.append(a_map(item))
    print(s)
    df[name] = s


