import pandas as pd
import numpy as np


chat_id = 1782651373 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    errors = np.random.normal(-21+np.exp(1), x.size)
    return (x/10+errors).mean() # Ваш ответ
