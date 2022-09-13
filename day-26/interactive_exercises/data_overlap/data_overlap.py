f = open("file1.txt", "r")
list1 = [int(line) for line in f.readlines()]

f = open("file2.txt", "r")
list2 = [int(line) for line in f.readlines()]

result = [number for number in list1 if number in list2]

print(result)
