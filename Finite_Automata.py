#!/usr/local/bin/python2

def dfa(no_of_strings):
	"""
		The Function obtains the no of strings and constructs the DFA by construct_Dfa() method
		and Validates the Lanaguage by validate_Dfa() method
		returns 1 if the Language is completely accepted by the constructed DFA.
		returns 0 if the Language is not completely accepted by the constructed DFA.
		returns -1 for invalid input by the user.
	"""
	l=construct_Dfa()																		#Constructs the DFA and receives a list of required data computed by the Constructed DFA.
	if(l==-1):
		return -1																			#Invalid Input.
	no_of_symbols=l.pop()																	#No of valid symbols in the Lanaguage.
	symbols=l.pop()																			#List of valid Symbols in the Language.
	states=l.pop()																			#Dictionary computed by the Transition Diagram of the constructe DFA.
	flag=validate_Dfa(states,symbols,no_of_symbols,no_of_strings)							#Validates the Entered String against the constructed DFA.
	return flag

def validate_Dfa(states,symbols,no_of_symbols,no_of_strings):
	"""
		Obtains a number of Strings from the user as i/p and the constructed DFA is checked against the input Strings. 
		Arguments is the Constructed DFA, the valid symbols and total Strings given.
		returns -1 for invalid i/p, returns 0 for language processing failure and returns 1 for the DFA accepting all the Strings.
	"""
	flag=1
	#no_of_strings=input()
	k=0
	print "String Validation"
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
		print "\n---------------------------------------------------------------\n"
		print "\nAll the Entered Strings of the Language consisting of the Symbols \n",symbols," are accepted by the given Discrete Finite Automata"
		print "\n---------------------------------------------------------------\n"
		return 1
	else:
		print "\n---------------------------------------------------------------\n"
		print "\nAll the Entered Strings of the Language consisting of the Symbols \n",symbols," are not accepted by the given Discrete Finite Automata"
		print "\n----------------------------------------------------------------\n"
		return 0


def construct_Dfa():
	"""
		The function constructs the DFA based on user i/p of no of states, transition states based on the input symbols 
		which are allowed in the Language.
		On Successful Construction of Dfa Returns a list containing [states,symbols,no_of_symbols] of the Constructed DFA.
		On Incorrect input returns -1
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
			if(int(string[1:])>=n):
				print "Entered Incorrect Data, Program will Exit"
				return -1
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
	l=list()
	l.append(states)
	l.append(symbols)	
	l.append(no_of_symbols)	
	return l 																				#returns a list of the constructed DFA Elements


print "Enter no of Strings to be accepted:"
dfa(input())