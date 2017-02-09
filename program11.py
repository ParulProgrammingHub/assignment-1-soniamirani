11)	WPP to enter principle amount, rate of interest, and no of years. Create compound_interest(principle,rate,time). To calculate compound interest.
Answer :
p=int(input("Enter principle amount : "))
r=int(input("Enter rate of interest : "))
y=int(input("Enter number of years : "))
amount = 0
def compint (p,r,y) :
       amount=p*((1+float(r/100))**y)
       interest=amount-p
       print ("Compound interest is : ",interest)
       return
compint (p,r,y)
