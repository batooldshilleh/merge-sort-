def merge(arr):
    if len(arr) > 1:
       med= len(arr) //2
       la=arr[:med]
       ra=arr[med:]
       merge(la)
       merge(ra)
       l=r=m=0
       while l< len(la) and r < len(ra):
           if la[l] < ra[r]:
               arr[m]= la[l]
               l+=1
           else:
               arr[m] = ra[r]
               r += 1
           m += 1
       while l < len(la):
           arr[m] = la[l]
           l +=1
           m +=1
       while r < len(ra):
           arr[m] = ra[r]
           r +=1
           m +=1
n = int(input())
the_arr = list(map(int, input().split()))
merge(the_arr)
the_lest="["+",".join(str(i) for i in the_arr)+"]"
print(the_lest)

