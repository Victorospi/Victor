print("hello world")


#Find number in string, and print result string withot it
x = (2,3,4,2,5)
for i in x:
  if i != 2:
    print(i, end=" ")
print("")


#Print string with simmilar numbers in two different strings
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = [elem for elem in a if elem in b]
print (result)


#Print sum of digits in number
def sum_digits(num):
  digits = [int(i) for i in str(num)]
  return sum(digits)
print(sum_digits(1234))


#Print longest and frequent word in string
import collections
text = 'lorem ipsum dolor sit amet amet amet'
words = text.split()
counter = collections.Counter(words)
mostWord, occurrences = counter.most_common()[0]
longestWord = max(words, key=len)
print(mostWord, longestWord)


#Reverse inputed number and print it
n1 = input("Введите целое число: ")
n_list = list(n1)
n_list.reverse()
n2 = "".join(n_list)
print('"Обратное" ему число:', n2)