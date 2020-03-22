seq = open("seq.txt", "r")
seq = (seq.read()).replace("\n","")
seq = (seq.read()).replace("\r","")
print (seq[40:50])