n = int(input("Enter the number of elements: "))
l = []
print ("Enter",n,"elements:")
for i in range(0, n):
   a = int (input ())
   l.append(a)

max = l[0]
for i in range(1,n):
   if (l[i] > max):
      max = l[i]

print("The largest number is",max)
