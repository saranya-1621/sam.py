sd=int(input())
an1,an2=0,1
print(an2,end=" ")
for i in range(1,sd):
 an3=an1+an2
 print(an3,end=" ")
 an1,an2=an2,an3
