# Finite Automata - Proof of Concept :

## Basic Introduction to Finite Automata :
* A finite automaton (FA) is a simple idealized machine used to recognize patterns within input taken from some character set
  (or alphabet) C. The job of an FA is to accept or reject an input depending on whether the pattern defined by the FA occurs
  in the input.
* A finite automaton consists of :
    * Finite set S of N states.
    * A special start state.
    * Set of final (or accepting) states.
    * Set of transitions T from one state to another, labeled with chars in C.
* Deterministic Finite Automaton :
    * DFA is a finite state machine that accepts/rejects finite strings of symbols and only produces a unique computation
      (or run) of the automaton for each input string.'Deterministic' refers to the uniqueness of the computation.
    * A DFA is defined as an abstract mathematical concept, but due to the deterministic nature of a DFA,
      it is implementable in hardware and software for solving various specific problems.
    * DFAs recognize exactly the set of regular languages which are, among other things,
      useful for doing lexical analysis and pattern matching.
* Non Deterministic Finite Automaton :
    * NFA is a finite state machine that does not require input symbols for state transitions and is capable of transitioning
      to zero or two or more states for a given start state and input symbol. This distinguishes it from a DFA,
      in which all transitions are uniquely determined and in which an input symbol is required for all state transitions.
    * All NFA's can be translated to equivalent DFA's using the subset construction algorithm.
    * Like DFAs, NFAs only recognize regular languages.

## Program Details :
* The Program is written in Python.
* The Program Constructs a DFA based on the user input, and inputs a string of a particular language, validates the
  string against the constructed DFA and tells if the DFA accepts the specific language or not.
* Input is taken in the form of the Transition Table for that particular DFA.

### DFA Implementation :
* Input the String to be validated against the DFA.
* Input total number of states present in the DFA [Q].
* Input the number of Alphabets over which the DFA is valid [sigma].
* Input all the valid symbols under sigma.
* Input the Transition Table for all states defined over [Q0,Q1,Q2,Q3 ... QN]
  where n >= 0.
* Input the String to be Validated and validate the following String against the constructed DFA.
* Output the Validation result for the String.

### Server Details :
* Server written completely in Python, using Cherrypy, A lightweight, fast and stable Web Framework. 
* Config
  - host -> Host Id
  - port -> Port no the Server listens during execution
* /     -> renders the index.html page
* /dfa  -> POST Request [payload -> JSON]
  - Keys:
    + no_of_states    -> Integer >=1
    + no_of_symbols   -> Integer >=1
    + string          -> String to be validated, defined over symbols*
    + states          -> {[0:{'Transitions':[3,2,...], 'Final':1 or 0},....n]}
    + symbols         -> [ symbol 1, symbol 2, ..]
  - Response
    + 1 -> String accepted by the Constructed DFA
    + 0 -> String not accepted by the Constructed DFA

## Todo
* NFA Implementation
* Clientside DFA Visualisation Development
  * Parsing a string as i/p to construct the transition table taken as i/p.
  * Development of Graphical representation of the DFA
  * Validation of i/p string using the Server against the constructed DFA
  * Development of transition table from the graphical representation.

## Web Application Available at
* https://murmuring-inlet-2528.herokuapp.com/
