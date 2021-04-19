from problems import knapsack
from algorithms import bruteforce
import time

weight_limit = 3000

for i in range(24):  # 12:14 2021/04/03 was 31 but that takes too much time on my computer
    things = knapsack.generate_things(i)
    start = time.time()
    bruteforce(things, weight_limit)
    end = time.time()

    print(f"{i}\t|\t{end-start}s")
