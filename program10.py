10)	WPP to enter principle amount, rate of interest, and no of years. Create simple_interest(principle,rate,time). To calculate simple interest.
Answer :
p=int(input("Enter principle amount : "))
r=int(input("Enter rate of interest : "))
y=int(input("Enter number of years : "))
def simpint (p,r,y) :
       interest= (p*r*y)/100
       print ("simple interest is : ",interest)
       return
simpint (p,r,y)
