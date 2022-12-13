from sys import argv

day = argv[1]

with open(f"treeofknowledge/day{day}.py", "w") as f:
    print(f"Created treeofknowledge/day{day}.py")
with open(f"data/day{day}.txt", "w") as f:
    print(f"Created data/day{day}.txt")
