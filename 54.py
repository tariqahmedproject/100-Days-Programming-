# 54.	Write a program which can remove a particular character from a string.

num=input("Enter  Name :")
word_remove=input("Enter  word to remove :")

num=num.lower()
word_remove=word_remove.lower()

c=num.replace(word_remove,"")
print(c)
