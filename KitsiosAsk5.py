"""Χρησιμοποιώ την punctuation για να βγάλω όλα τα
σύμβολα στίξης από το κείμενο"""
from string import punctuation

#Ανοίγω το αρχειο και διαβάζω το περιεχόμενο στην μεταβλητή s
file = open ("c://Myfile.txt")
s = file.read()

#Βγάζω τα σημεία στίξης και τυπώνω το νέο κειμενο s
for c in punctuation:
	s = s.replace(c, '')
print (s.split())

#Χωρίζω το κείμενο σε λέξεις που μπαινουν στη λίστα L
L = s.split()

# Για κάθε λέξη ελέγχω το μήκος
for i in range(len(L)):
        #αν είναι πάνω από 3 γράμματα
        if len(L[i]) > 3:
                word=L[i]
                #παίρνω το πρώτο γράμμα και το βάζω στην μεταβλητή char
                char=word[0]
                #έπειτα το προσθέτω στο τέλος μαζί με ay
                word=word[1:]+char+"ay"                
                #και τυπώνω μόνο τις λέξεις που άλλαξα
                print(word)
