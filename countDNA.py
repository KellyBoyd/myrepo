import sys
filename = sys.argv[1] #reading file name from commandline
infile = open (filename, 'r')
s = infile.readline() #store read lines as s
from collections import Counter #python module that counts repeats of data
counter = Counter(s) #count repetitions in s
f = open("CountingDNAoutput.txt", 'w') #create file to write to 
a = (counter['A']) #count individual bases
c = (counter['C'])
g = (counter['G'])
t = (counter['T'])
output =  (str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)) #convert int to string output
f.write(output) #print output to textfile 
