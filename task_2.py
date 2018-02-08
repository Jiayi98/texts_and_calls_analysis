
import csv
with open('/Users/user/Desktop/udacity/project 1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/user/Desktop/udacity/project 1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#新建一个dictionary用于储存所有的号码以及他们对应的通话时间
tele_book = {}
for phone in calls:
    if phone[0] in tele_book:
        tele_book[phone[0]] += eval(phone[3])
    else:
        tele_book[phone[0]] = eval(phone[3])

    if phone[1] in tele_book:
        tele_book[phone[1]] += eval(phone[3])
    else:
        tele_book[phone[1]] = eval(phone[3])

#获取dictionary中所有value返回一个list
val_list = tele_book.values()

#获取最长通话时间
maximum = max(val_list)

#找到最长通话时间所对应的号码
result = ''
for number in tele_book:
    if tele_book[number] == maximum:
        result = number

print("{} spent the longest time, {} seconds, on the phone during
September 2016.".format(result,maximum))

