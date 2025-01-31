def twocode(arr,size):
    xorof2=arr(0)
    x=0
    y=0
   setbit=0
   for i in range (1,size):

    xorof2=xorof2^ arr[1]
    setbit=xorof2 & ~(xorof2-1)
    for i in range(size):
       if (aarr[i] & setbit):
          x=x^arr[i]
       else:
          y=y^arr[i]

print("twoodd elements are ",x "&",y)


arr=[]
arr_size=int(input("emter the size of the array"))
for i in range(0,arr_size):
   z=int(input("enter element :"))
   arr.append(z)
twoodd (arr,arr_size)




 



