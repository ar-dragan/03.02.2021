lung=1
a=[]
n=input("dati n")
for i in range(0,len(n)):
    a.append(n[i])
print(a)
for i in range(0,len(a)):
    a[i]=int(a[i])
for i in range(1,len(a)):
    if(a[i]>=[i-1]):
        lung+=1
  print(lung)
  print(len(a))
  if(lung==len(a)):
    print("DA")
  elif(lung=len(a)):
    print("NU")