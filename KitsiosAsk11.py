#Ανοίγω το αρχείο που έχει 4άδες αριθμών
with open("c://Numbersfile.txt") as textFile:
    MyList = [line.split() for line in textFile]
#Τυπώνω τη λίστα που δημιουργήθηκε
print(MyList)

#Φτιάχνω μια λίστα με 6 αριθμούς που δίνει ο χρήστης
L=[]
for i in range(6):
    L.append(int(input('Δώσε αριθμό ')))
#Τυπώνω τη λίστα 
print(L)

#Για κάθε γραμμή της λίστας ελέγχω πόσοι αριθμοί βρίσκονται μέσα στους 6 της L
for i in range(len(MyList)):
    count=0
    for j in range(4):
        num=int(MyList[i][j])
             
        for k in range(6):           
            if num==L[k]:
                count+=1
    #Αν είναι και οι 4, τότε γράφω υπάρχει διαθέσιμη τετράδα            
    if count==4:
        print("Υπάρχει διαθέσιμη τετράδα")
        #και την τυπώνω για να την δει ο χρήστης
        for j in range(4):
            num=int(MyList[i][j])
            print(num,end=' ')
