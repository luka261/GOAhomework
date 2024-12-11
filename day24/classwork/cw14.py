#1) დღეს რომელი ფუნქციები და მეთოდები ვისწავლეთ,
#გატესტეთ ყველა: len(), .append(), 
#.insert(), .pop(), .remove()

list = [1, 4, 7, 2, 8, 433, 945, 25, 1445, 234, 13,]

sorted_list = sorted(list)
print(sorted_list)

len_list = len(list)
print(len_list)


list.insert(1, 5)
print(list)


list.pop(6)
print(list)

list.remove(25)
print(list)

list.append(100) 
list.append(6)
print(list)



# 2) .pop() მეთოდის გამოყენებით გამოაცალკევეთ
#კონკრეტული ელემენტი list'ისგან და ჩასვით ცალკე 
#ცვლადში ზუსტად ისე როგორც მე გავაკეთე

my_list = [1, 2, 3, 4, 5]
my_list.pop(2)

print(my_list)

# 3) ახსენით განხსვავება pop'სა და remove'ს შორის
my_list.remove(4)
print(my_list)


# 4) შექმენით 4 ელემენტიანი list'ი და შუაში ჩაამატეთ 
#1 ელემენტი
list_list = [1, 2, 4, 5 ]
list_list.insert(2,3)
print(list_list)

