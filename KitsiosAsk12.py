#Εισάγω την βιβλιοθήκη datetime
import datetime

#Ο χρήστης εισάγει ημερομηνία που επιθυμεί
hmerom = input("Ποιά ημερομηνία επιθυμεις? ")

#Χωρίζω την ημερομηνία σε έτος, μήνα, ημέρα
L=hmerom.split("/")
mera = int(L[0])
mhnas = int(L[1])
etos = int(L[2])
print(mera, mhnas, etos)

#Φτιάχνω δύο dictionaries για κανονικά και για δίσεκτα έτη
normalyear = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
leapyear = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

#Ελέγχω το έτος που μου έδωσε ο χρήστης και πάιρνω τις μέρες του μήνα
#από το κατάλληλο λεξικό
if etos %400 == 0 or (etos%4 == 0 and etos%100!=0):
    print('Δίσεκτο έτος!')
    days = leapyear [mhnas]
    print('Ο μήνας έχει:', days,'ημέρες')
else:
    print('Κανονικό έτος (όχι δίσεκτο)')
    days = normalyear [mhnas]
    print('Ο μήνας έχει:', days,'ημέρες')

#Βρίσκω και τυπώνω την διαφορά της σημερινής ημερομηνίας από
#αυτή που έδωσε ο χρήστης (βάζω ώρες, λεπτά, δευτερόλεπτα στο μηδεν
dif = datetime.datetime.now() - datetime.datetime(etos, mhnas, mera, 0, 0, 0)
print(dif) 

        
    
