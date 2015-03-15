#! /usr/bin/env python2

class DeterministicFiniteAutomata:
    """
        The Class obtains the string and constructs the DFA by the constructor
        and Validates the string for the Lanaguage by validate_Dfa() method
        returns 1 if the Language is completely accepted by the constructed DFA.
        returns 0 if the Language is not completely accepted by the constructed DFA.
    """
    no_of_symbols = 0
    no_of_states = 0
    states = None
    symbols = None

    def __init__(self):
        '''
            states -> {['state':{'Transitions':[3,2,...], 'Final':1},....]}
        '''
        print "Enter total no of states:"
        self.no_of_states = int(raw_input())
        print "Enter no of Alphabets valid in the Finite Automata:"
        self.no_of_symbols = int(raw_input())
        self.states = {}
        self.symbols = []
        for index in range(self.no_of_symbols):
            print "Enter Symbol " + str(index + 1) + ":"
            self.symbols.append(raw_input())
        print "\nInitial State is denoted by Q0:\n"
        for state_id in range(self.no_of_states):
            transition_list = []
            for symbol_id in range(self.no_of_symbols):
                print "Enter Q" + str(state_id) + " State Transition ID for input Symbol",self.symbols[symbol_id],":"
                destination_id = int(raw_input())
                if destination_id >= self.no_of_states:
                    print "Entered Incorrect Data, Program will Exit"
                    exit(-1)
                transition_list.append(destination_id)
            print "Enter 1 if the Q"+str(state_id)+" is a Final State, else 0 for Non Final State:"
            final_state = int(raw_input())
            if final_state != 1 and final_state != 0:
                print "Entered Incorrect Data, Program will Exit"
                return -1
            state={}
            state['Final']=final_state
            state['Transitions']=transition_list
            self.states["Q"+str(state_id)] = state

    def validate_dfa(self, string):
        """
            Obtains a String from the user as i/p and the constructed DFA is checked against the input String.
            Arguments is the Constructed DFA, the valid symbols and total Strings given.
            returns -1 for invalid i/p, returns 0 for language processing failure and returns 1 for the DFA accepting all the Strings.
        """

        state = "Q0"
        for letter in string:                                                               #Individual String to be Processed through the constructed DFA.
            state="Q" + str((self.states[state]['Transitions'])[self.symbols.index(letter)])
        return self.states[state]['Final']                                                    #Validate last state to be a Final State.

if __name__ == '__main__':

    dfa = DeterministicFiniteAutomata()
    print "Enter a String"
    print dfa.validate_dfa(raw_input())
