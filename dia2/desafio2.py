import math


def arrendondar(num: float) -> dict:
    return {
        "piso": math.floor(num),
        "teto": math.ceil(num),
        "arredondado": round(num)
    }

print(arrendondar(5.3))  