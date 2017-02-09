7)	WPP to enter 2 angles and using function thrdangle( angle1, angle2) calculate 3rd angle.
Answer :
a1=int( input( "Enter a value of first angle : " ))
a2=int( input( "Enter a value of second angle : " ))
def thirdangle (a1,a2) :
       a3= 180-a1-a2
       print ("Third angle is : ",a3)
       return a3
thirdangle (a1,a2)
