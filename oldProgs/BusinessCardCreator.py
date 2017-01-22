# -----------------------------------------+
# Caleb Barnwell                           |  
# Business Card Program Part II            |
# Last Updated: September 27, 2015         |  
# -----------------------------------------|
# Business Card Creator                    | 
# -----------------------------------------+


fname=input("Please enter your first name > ")
sname=input("Please enter your last name > ")
tel=input("Please enter your telephone number in (XXX)-XXX-XXXX format > ")
print()
print("Here is your business card...")
print()
print("+------------------------------------------------+")
print("|    |                                           |")
namestr="|   -|\t\t"+sname+","+fname
str(namestr)
print(namestr.ljust(41, )+"|")
print("|  --|\t\tTribute Liabilities Associate    |")
print("| ---|\t\tParasail Capital                 |")
print("| ---------                                      |")
print("|  -------      4 Hunger Plaza                   |")
print("|               STE 1400                         |")
print("|               District 12, Panem 00012         |")
print("|                                                |")
print("| Phone: "+tel+"  @: caleb@parasail.com   |")
print("+------------------------------------------------+")
