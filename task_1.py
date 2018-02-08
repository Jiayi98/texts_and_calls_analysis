import csv
with open('/Users/user/Desktop/udacity/project 1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/user/Desktop/udacity/project 1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#create a new list to store phone numbers with no duplicates
no_duplicates = []

# merge two lists
temp = texts + calls

for info in temp:
  if info[0] not in no_duplicates:
      no_duplicates.append(info[0])
  if info[1] not in no_duplicates:
      no_duplicates.append(info[1])
      
# calculate the total numbers of the list
count = len(no_duplicates)
print("There are {} different telephone numbers in the records.".format(count))
