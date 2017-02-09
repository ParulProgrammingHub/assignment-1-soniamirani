9)	Wpp to enter of 5 subjects and find the mean of 5 subjects ,calculate percentage. If percentage is less than 35 print fail else print pass
Solution:
i=0
mean=0
sums=0
pre=0
while (i<5) :
      x=int(input("Enter marks of subject : "))
      sums=sums+x
      i=i+1
mean=sums/5
print(mean)
if (mean>35) :
       print("PASS")
else :
       print ("Fail")
