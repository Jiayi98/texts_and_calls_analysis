import csv
with open('/Users/user/Desktop/udacity/project 1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/user/Desktop/udacity/project 1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
#一个可能是推销电话的号码簿
tele_book = []

#一个接收电话的号码簿
#可不可以直接用set而不是list，然后用 add()，这样就可以省掉判断not in receive_book？
receive_book = set()
for phone in calls:
    receive_book.add(phone[1])

#一个收发信息的号码簿
text_book = set()
for phone in texts:
    if phone[0] not in text_book:
        text_book.add(phone[0])
    if phone[1] not in text_book:
        text_book.add(phone[1])

for phone in calls:
    #以140开头的拨出号码一定是推销电话
    if phone[0].startswith("140") and phone[0] not in tele_book:
        tele_book.append(phone[0])
    elif phone[0] not in tele_book and \
          phone[0] not in receive_book and \
                  phone[0] not in text_book:
        #只拨出电话但从未接收来电而且没有收发过短信的可能是推销电话
        tele_book.append(phone[0])
        
tele_book.sort()
print("These numbers could be telemarketers: \n")
s = '\n'
print(s.join(tele_book))
