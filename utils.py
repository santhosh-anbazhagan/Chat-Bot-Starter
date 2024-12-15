import time
import random


def get_current_time_millis():
    val = int(round(time.time() * 1000) * random.randint(10, 1000))
    # print(f"Unique : {val}")
    return val
