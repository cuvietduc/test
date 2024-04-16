# read data from a user
name = input('Enter file: ')
handle = open(name, 'r')

# updating one of the many counts
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
# how to find the largest item in a list
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print (bigword, bigcount)