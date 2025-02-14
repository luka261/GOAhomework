# 1) შექმენით list comprehension რომელიც შექმნის list'ს რიცხვებით 1'დან 100'მდე
# 2) შექმენით list comprehension რომელიც შექმნის list'ს რიცხვებით 1'დან 100'მდე,
#  2-2'ის გამოტოვებით. (ანუ: [1, 3, 5...])
# 3) შექმენით რაიმე list'ი სახელებით და შემდეგ შექმენით list comprehension 
# რომელიც შექმნის სახელების ახალ list'ს სადაც არ იქნება ასო 
# "a" და ყველა string'ს თავში ექნება "#".

list = [x for x in range (1,101) ]
print(list)

list2 = [y for y in range (1,101,2) ]
print(list2)

list3 = [y for y in range (1,101) if y % 2 != 0 ]
print(list3)

list4 = ["luka", "liza", "sandro", ]
newlist = [name for name in 'a']
