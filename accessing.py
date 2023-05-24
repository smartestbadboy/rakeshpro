import array as arr
a=arr.array('i',[10,20,30,40,50])
print ("the elements of array arr")
for i in range(0,4):
 print(a[i])
 for i in a:
  print("the elements at index 2 is",a[2])
print(a)
