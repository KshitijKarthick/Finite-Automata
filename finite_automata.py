#!/usr/local/bin/python2
def dfa(no_of_strings):
	"""
		The function constructs the DFA based on user i/p of no of states and the symbols allowed in the Language.
		Obtains a number of Strings from the user as i/p and the constructed DFA is checked against the input Strings. 
		Argument is the no of strings to be processed.
		returns -1 for invalid i/p, returns 0 for language processing failure and returns 1 for the DFA accepting all the Strings.
	"""
	print "Enter total no of states:"
	n=input()
	print "Enter no of Alphabets valid in the Finite Automata:"
	no_of_symbols=input()
	i=0
	symbols=list()
	print "Enter the Valid Symbols:"														#Symbol Input
	while i<no_of_symbols:
		symbols.append(raw_input())
		i=i+1
	print "--------------------------------------------------------------"
	print "\nInitial State is denoted by Q0:\n"
	states=dict()
	i=j=0
	while i<n:																				#Receives the transition states of all the i/p states.
		l=list()
		j=0
		print "--------------------------------------------------------------\n"
		while j<no_of_symbols:																#Recevies individual symbol transition of every i/p state.	
			print "Enter Q"+str(i)+" State Transition for input Symbol",symbols[j],":"
			string=raw_input()
			string=string.capitalize()
			l.append(string)
			j=j+1
		print "Enter 1 if the Q"+str(i)+" is a Final State, else 0 for Non Final State:"
		k=input()																			#Final State or Non Final State.
		if k!=1 and k!=0:
			print "Entered Incorrect Data, Program will Exit"
			return -1
		l.append(k)
		states['Q'+str(i)]=l
		i=i+1
	print "--------------------------------------------------------------\n"
	#print "Enter no of Strings to be processed:"
	flag=1
	#no_of_strings=input()
	k=0
	while k<no_of_strings:																	#Multiple Strings being processed based on received argument.
		print "\n--------------------------------------------------------------\n"
		print "\nEnter String",k+1,"to be processed:"
		s=raw_input()
		sum=0
		i=0
		while i<no_of_symbols:																#Validate Entered String to be well defined under the specified alphabet set.
			sum=sum+s.count(symbols[i])
			i=i+1
		if sum != s.__len__():
			print "Incorrect String Entered"
			return -1
		#print states
		i=0
		q="Q0"
		while i < s.__len__():																#Individual String to be Processed through the constructed DFA.
			ch=s[i]
			q=(states[q])[symbols.index(ch)]
			i=i+1
		if states[q][no_of_symbols]==1:														#Validate last state to be a Final State.
			print "\nString is accepted by the DFA"
		else:
			print "\nString is not accepted by the DFA"
			flag=0
		k=k+1																				
	if flag==1:																				#Validate all Strings to be well defined under the constructed DFA.
		print "\n-----------------------------------------------------------------------------------------------\n"
		print "\nAll the Entered Strings of the Language consisting of the Symbols ",symbols," are accepted by the given Discrete Finite Automata"
		print "\n-----------------------------------------------------------------------------------------------\n"
		return 1
	else:
		print "\n-----------------------------------------------------------------------------------------------\n"
		print "\nAll the Entered Strings of the Language consisting of the Symbols ",symbols," are not accepted by the given Discrete Finite Automata"
		print "\n-----------------------------------------------------------------------------------------------\n"
		return 0

print "Enter no of Strings to be accepted:"
dfa(input())