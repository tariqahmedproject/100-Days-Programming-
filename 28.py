# 28.The current population of a town is 10000. The population of the town is increasing at the
# rate of 10% per year. You have to write a program to find out the population at the
# end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

final=0
current=10000
print(current)
while True:
   b=(current)-((10*current)/100) #increase formula
   current=b   #value swip

   print(int(b))
   final=final+1

   if final==9:
      break
