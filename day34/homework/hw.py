# 1) https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
# 2) https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
# 3) https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
# 4) https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python
# 5) https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
# 2) შექმენით manual_min ფუნქცია
# 3) შექმენით manual_max ფუნქცია

def manual_min(*args):
    return sorted(args)[0]

def manual_max(*args):
    return sorted(args)[-1]

print(manual_min(1, 2, 3, 4, 5))
print(manual_max(1, 2, 3, 4, 5))

