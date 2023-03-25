input1=input("wat wil je je lijst noemen/welke lijst wil je bewerken(zonder.txt erbij):\n")
list = open (input1,"a")
input2=input("wat wil je toevoegen bij je lijstje:\n")
list.write ("-",input2,"\n")
list.close