terms=int(input("number of terms: "))
n1=0,n2=1
count=0
 if terms <= 0:
  print("enter a positive integer")
 elif terms == 1:
  print("fibonacci sequence upto",terms,":")
  print(n1)
 else:
  print ("fibonacci sequence :")
   while count < terms:
    print(n1)
     n=n1+n2
     n1=n2
     n2=n
     count=count+1
