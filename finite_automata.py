#! /usr/bin/env python2

class DeterministicFiniteAutomata():
    """
        The Class obtains the string and constructs the DFA by the constructor
        and Validates the string for the Lanaguage by validate_Dfa() method
        returns 1 if the String is completely accepted by the constructed DFA.
        returns 0 if the String is not completely accepted by the constructed DFA.
    """
    no_of_symbols = 0
    no_of_states = 0
    states = None
    symbols = None

    def __init__(self, no_of_symbols=0, no_of_states=0, states = None, symbols = None):
        '''
            Parameters( no_of_symbols, no_of_states, states, symbols)
            no_of_symbols -> No of Symbols in Sigma
            no_of_states -> No of states in the DFA
            states -> {['state':{'Transitions':[3,2,...], 'Final':1},....]}
            symbols -> [ symbol 1, symbol 2, ..]

        '''

        # if no i/p parameters are provided, takes i/p for all parameters.
        if no_of_states == 0 and no_of_symbols == 0 and states == None and symbols == None :

            try:
                print "Enter total no of states:"
                self.no_of_states = int(raw_input())
                print "Enter no of Alphabets valid in the Finite Automata:"
                self.no_of_symbols = int(raw_input())
                self.states = {}
                self.symbols = []
                # Symbols i/p upto no_of_symbols
                for index in range(self.no_of_symbols):
                    print "Enter Symbol " + str(index + 1) + ":"
                    self.symbols.append(raw_input())
                print "\nInitial State is denoted by Q0:\n"
                # Iterate over every state for receiving transitions.
                for state_id in range(self.no_of_states):
                    transition_list = []
                    # Iterate over every symbol transition for a particular state.
                    for symbol_id in range(self.no_of_symbols):
                        print "Enter Q" + str(state_id) + " State Transition ID for input Symbol",self.symbols[symbol_id],":"
                        destination_id = int(raw_input())
                        # Invalid state data
                        if destination_id >= self.no_of_states:
                            print "Entered Incorrect Data, Program will Exit"
                            exit(-1)
                        # Store every Transition by Index for that Symbol.
                        transition_list.append(destination_id)
                    # Final state or not [1 -> Final, 0 -> Non Final]
                    print "Enter 1 if the Q"+str(state_id)+" is a Final State, else 0 for Non Final State:"
                    final_state = int(raw_input())
                    # Invalid i/p
                    if final_state != 1 and final_state != 0:
                        print "Entered Incorrect Data, Program will Exit"
                        return -1
                    state={}
                    # Dictionary Construction {'Final':0 or 1, 'Transition:[1,2,...]'}
                    state['Final']=final_state
                    state['Transitions']=transition_list
                    self.states[state_id] = state

            except ValueError:
                exit(-1)

        # if i/p parameters are provided.
        else:
            self.no_of_states = no_of_states
            self.no_of_symbols = no_of_symbols
            self.states = states
            self.symbols = symbols

    def validate_dfa(self, string):
        """
            Obtains a String from the user as i/p and the constructed DFA is checked against the input String.
            Arguments is the Constructed DFA, the valid symbols and total Strings given.
            returns JSON
                Keys:
                    'Valid'         :   Denotes 0/1 for Valid or Invalid String for the DFA.
                    'Transitions'   :   Transitions Parsed for each letter in the String.
                    'String'        :   String Parsed against the DFA.
        """

        # Initial Start State.
        state = 0
        # Array of Individual transitions for each letter parsed as a String.
        transitions = []
        try:
            # Individual String to be Processed, iterated through the constructed DFA.
            for letter in string:
                initial_state = state
                # Each symbol traverses from start state till the i/p ends.
                state = (self.states[state]['Transitions'])[self.symbols.index(letter)]
                transitions.append([initial_state, letter, state])
            # Validate last state reached to be a Final State.
            return {
                    'Valid'       : self.states[state]['Final'],
                    'Transitions' : transitions,
                    'String'      : string
            }
        # Invalid parsing of String against the DFA.
        except (KeyError, ValueError) as e:
            return {
                    'Valid'       : 0,
                    'Transitions' : transitions,
                    'String'      : string
            }

if __name__ == '__main__':

    dfa = DeterministicFiniteAutomata()
    print "Enter a String"
    print dfa.validate_dfa(raw_input())