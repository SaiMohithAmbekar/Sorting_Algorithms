
# Bubble Sort

b=[10,4,6,8,3,5,2]
for i in range(0,len(b)):
    for j in range(0,len(b)-i-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
        #print(b)
print(b)

# Time Complexity: O(n^2)