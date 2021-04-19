from problems import knapsack
from algorithms import bruteforce
import time

weight_limit = 3000

for i in range(22):
    # 本來是物品個數是 31 實在太久了，我把它改成 22 還好。
    things = knapsack.generate_things(i)
    start = time.time()
    bruteforce(things, weight_limit)
    end = time.time()

    print(f"{i}\t|\t{end-start}s")
