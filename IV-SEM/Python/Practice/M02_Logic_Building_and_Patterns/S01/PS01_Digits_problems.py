'''n = int(input())
count = 0
while n > 0:
    count += 1
    n = n//10
print(count)'''
n=int(input())
temp =n
s=0
while n>0:
    s += (n%10)
    n//=10
print(s)
print(sum(map(int,str(temp))))

