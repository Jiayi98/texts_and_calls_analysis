
import csv
with open('/Users/user/Desktop/udacity/project 1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Users/user/Desktop/udacity/project 1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

first_texts = texts[0]
last_calls = calls[-1]

print("First record of texts, {} texts {} at time {}".format(first_texts[0],
                                            first_texts[1],first_texts[2]))

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
                        last_calls[0],last_calls[1],last_calls[2],last_calls[3]))
