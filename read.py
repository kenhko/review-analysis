data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
        

print('Done Read, total comments are', len(data))

sum_len = 0
for comment in data:
    sum_len = sum_len + len(comment)

print('In average, the number of wordings of comment are', sum_len/len(data))