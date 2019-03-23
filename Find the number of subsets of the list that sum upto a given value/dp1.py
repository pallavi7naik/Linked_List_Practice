def count_sets(arr,total,i):
    mem = {}
    return rec(arr,total,i, mem)

def rec(arr, total,i,mem):
    key = str(total) + ":" + str(i)
    if key in mem:
        return mem[key]
    if total==0:
        return 1
    elif i<0 :
        return 0
    elif total<0:
        return 0
    elif total<arr[i]:
        to_return =  rec(arr, total, i-1,mem)
    elif total>=arr[i]:
        to_return = rec(arr, total-arr[i],i-1,mem) + rec(arr, total,i-1,mem)
    mem[key] = to_return
    return to_return

l = []
a = input("enter the length of list:")
for i in range(int(a)):
    l.append(int(input()))
sum = input("enter the sum:")
# sum = 16
# l = [2,4,6,10]
# a = 4
ans = count_sets(l,int(sum),int(a)-1)
print(ans)