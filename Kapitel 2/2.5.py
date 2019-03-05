import math #importerar math för att man ska kunna vrunda uppåt

a=int(input("Hur många vill äta två vanliga korvar?"))
b=int(input("Hur många vill äta tre vanliga korvar?"))
c=int(input("Hur många vill äta två veganska korvar?"))
d=int(input("Hur många vill äta tre veganska korvar?")) #promtar användaren för antalet elever som äter antalet korvar

korv=math.ceil(int(((2*a)+(3*b)/8))) #korvarna dividerat med åtta avrundat uppåt
e=math.ceil(int(((2*c)+(3*d)/4))) #samma sak dividerat med 4

f=str(a+b+c+d) # string av antal elever totalt

g=str(d) #stringifyar separat eftersom man int ekan göra om till itne och string i samma statement
h=str(korv) #samma sak här

i=float(korv)
j=float(e)
k=float(f) #gör om till float eftersom man inte kan mutiplicera mellan float och int

kostnad=str(20.95*i+34.95*j+13.95*k) #mutiplicerar antal med pris

print("Det behövs " + g + " paket vanlig korvar, "+ h + " paket veganska korvar och "+ f +" drickor." )
print("Det blir totalt " + kostnad + "kr." ) #skriver ut i en mening
