# 51.	Count the frequency of a particular character in a provided string. Eg
# 'hello how are you' is the string, the frequency of h in this string is 2.

num=input("Enter Name : ")
word_find=input("Enter Word to Find in Name:")

#convert to lower case
num=num.lower()
word_find=word_find.lower()

c=num.count(word_find)
print(c)

