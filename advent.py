from treeofknowledge import day1

welcome = """######################################
#
#
# ADVENT OF CODE 2022
#
#
######################################
"""
print(welcome)

print("---Day 1---")

pth = "data/day1.txt"
elf_cals = day1.get_elf_cals(pth)
elf_cals.sort()
print(f"Max cals :{ elf_cals[-1] }")
print(f"Top 3 cals :{ sum(elf_cals[-3:]) }")


