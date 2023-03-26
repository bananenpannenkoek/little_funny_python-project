input1=input("what is this the file you want to add an item to:\n")
list = open (input1,"a")
input2=input("what item do you want to add to your list:\n")
list.write ("-",input2,"\n")
list.close
