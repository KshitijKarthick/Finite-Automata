#/bin/python2
def dfa():
	print "Enter total no of states:"
	n=input()
	print "Enter no of Alphabets valid in the Finite Automata:"
	no_of_symbols=input()
	i=0
	symbols=list()
	print "Enter the Valid Symbols:"
	while i<no_of_symbols:
		symbols.append(raw_input())
		i=i+1
	print "--------------------------------------------------------------\n"
	print "\nInitial State is denoted by Q0:\n\n"
	states=dict()
	i=j=0
	while i<n:
		l=list()
		j=0
		print "--------------------------------------------------------------\n"
		while j<no_of_symbols:
			print "Enter Q"+str(i)+" State Transition for input Symbol",symbols[j],":"
			string=raw_input()
			string=string.capitalize()
			l.append(string)
			j=j+1
		print "Enter 1 if the Q"+str(i)+" is a Final State, else 0 for Non Final State:"
		k=input()
		if k!=1 and k!=0:
			print "Entered Incorrect Data, Program will Exit"
			return -1
		l.append(k)
		states['Q'+str(i)]=l
		i=i+1
	print "--------------------------------------------------------------\n"
	print "Enter no of Strings to be processed:"
	no_of_strings=input()
	k=0
	while k<no_of_strings:
		print "\nEnter String to be processed:"
		s=raw_input()
		sum=0
		i=0
		while i<no_of_symbols:
			sum=sum+s.count(symbols[i])
			i=i+1
		if sum != s.__len__():
			print "Incorrect String Entered"
			return -1
		#print states
		i=0
		q="Q0"
		while i < s.__len__():
			ch=s[i]
			q=(states[q])[symbols.index(ch)]
			i=i+1
		if states[q][no_of_symbols]==1:
			print "String is accepeted by the DFA"
			#return 1
		else:
			print "String is not accepted by the DFA"
			#return 0
		k=k+1
dfa()