import numpy as np

def calculate(list):
    if len(list) < 8:
        raise ValueError("List must contain nine numbers.")
    else: 
        matrix = np.array(list).reshape(3, 3)
        mean = [matrix.mean(axis=0),matrix.mean(axis=1),matrix.flatten().mean()]
        var = [matrix.var(axis=0), matrix.var(axis=1), matrix.flatten().var()]
        sd = [matrix.std(axis=0), matrix.std(axis=1), matrix.flatten().std()]
        max = [matrix.max(axis=0), matrix.max(axis=1), matrix.flatten().max()]
        min = [matrix.min(axis=0), matrix.min(axis=1), matrix.flatten().min()]
        sum = [matrix.sum(axis=0), matrix.sum(axis=1), matrix.flatten().sum()]


        calculations = {
            "mean" : mean,
            "variance": var,
            "standard deviation": sd, 
            "max" : max,
            "min" : min,
            "sum" : sum
        }


    return calculations