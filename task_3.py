import csv
with open('/Users/user/Desktop/udacity/project 1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/user/Desktop/udacity/project 1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
#新建一个list用于储存所有接收班加罗尔地区电话的号码
tele_book = []
for phone in calls:
    if phone[0].startswith('(080)') and phone[1] not in tele_book :
        #以‘（’开头的为固话，获取括号内区号（不包括括号）
        if '(' in phone[1]:
            index = phone[1].index(')')
            tele_book.append(phone[1][1:index])
        elif ' ' in phone[1] and \
                    (phone[1].startswith('7') or \
                    phone[1].startswith('8') or \
                    phone[1].startswith('9')):
            #含有空格以及以7、8、9开头的为移动电话，获取前四位
            index = phone[1].index(' ')
            tele_book.append(phone[1][:4])

#利用set与list转换去重
#我在for loop中第一个if已经判断了 phone［1］not in tele_book为什么还是会有重复？
my_set = set(tele_book)
tele_book_noduplicates = sorted(list(my_set))

print("The numbers called by people in Bangalore have codes: \n")
s = '\n'
print(s.join(tele_book_noduplicates))

#获取班加罗尔地区的被叫号码总数
times = tele_book.count("080")

#计算比例
percentage = '{:.2%}'.format(times / len(tele_book))
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
