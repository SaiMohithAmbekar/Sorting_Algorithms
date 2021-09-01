
# Insertion Sort

a=[9,3,5,2,6,4,0]

for i in range(1,len(a)):
    value=a[i]
    idx=i
    while(idx>0 and a[idx-1]>value):
        a[idx]=a[idx-1]
        idx-=1
    a[idx]=value
    #print(a)
    
print(a)

# Time Complexity : 
# Avg & Worst Case ==> O(n^2)
# Best Case        ==> O(n)