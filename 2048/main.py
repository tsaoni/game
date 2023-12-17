from utils import *

table = init()
print("Game start! ")
print_table(table)
while True:
    action = input("please input d(up) c(down) x(left) v(right) q(quit): ")
    assert action in ["d", "c", "x", "v", "q"]
    if action == "q": exit(-1)
    print_table(table)
    