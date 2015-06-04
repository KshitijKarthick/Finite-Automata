//Clears the input area on load

$(document).ready(function(){
	$('#input_area').val('');
});

// Separates the input into lines

function lineSpliter(lines){
	var list_of_lines=lines.split(/ *\n */);
	return list_of_lines;
}

// Accepts the input lines and return an object with states and coresponding symbol

function transitionParser(line){
	var flag=0;
	var initial_partitions=line.split(/ *< */);
	if(initial_partitions.indexOf('')===-1 && initial_partitions.length===2);
	else{
		alert("Input syntax error");
		return "Error";
	}
	var final_partitions=initial_partitions[1].split(/ *> */);
	if(final_partitions.indexOf('')===-1 && final_partitions.length===2);
	else{
		alert("Input syntax error");
		return "Error";
	}

	var start_state=initial_partitions[0];
	var symbol=final_partitions[0];
	var stop_state=final_partitions[1];
	if(symbol===''||start_state===''||stop_state===''){
		alert("Input syntax error");
		return "Error";
	}
	var transition={'start':start_state,'symbol':symbol,'stop':stop_state};
	return transition;
}

//Function to remove duplicate objects from a list of objects
function duplicateObjectRemover(list){
	var arrResult = {},
	unique = [];
	for (i = 0, n = list.length; i < n; i++) {
		var item = list[i];
		//Create an array of object with key as the values of the original objects concatinated and value as the object
		arrResult[item.start+"-"+item.symbol+ "-"+item.stop] = item;
	}
	i = 0;
	for (var item in arrResult) {
		unique[i++] = arrResult[item];
	}
	return unique;
}

//Function to check for ambiguity in transition

function ambiguityChecker(list){
	var arrResult = {},
	unique = [];
	for (i = 0, n = list.length; i < n; i++) {
		var item = list[i];
		//Creating object key with only start state and symbol to check for multiple entries in the transition table
		arrResult[item.start+"-"+item.symbol] = item;
	}
	i = 0;
	for (var item in arrResult) {
		unique[i++] = arrResult[item];
	}
	if(list.length!==unique.length)
		return true;
	else
		return false;
}


//Function to remove duplicates from a normal list
function duplicateRemover(list){
	var a=[];
	for (var i = 0; i < list.length; i++) {
		if(a.indexOf(list[i])===-1) a.push(list[i]);
	}
	return a;
}

// Function calls on click event of Submit Button

$('#submit-button').click(function(){
	var transition_list=[];
	var states_list=[];
	var symbol_list=[];
	var statements=$('#input_area').val();
	if(statements===''){
		alert("Input cannot be Empty");
		return;
	}
	var lines=lineSpliter(statements);
	if(lines.length<3){
		alert("Not enough Input");
		return;
	}
	for(i=0;i<lines.length-2;i++){
		var temp_object= transitionParser(lines[i]);
		if(temp_object==="Error"){
			// Clears the list is error occurs
			transition_list=[]
			return;
		}
		transition_list.push(temp_object);
	}
	// Removing duplicate transitions
	transition_list=duplicateObjectRemover(transition_list);
	// Checking for ambiguity in transitions
	var ambiguity=ambiguityChecker(transition_list);
	if(ambiguity===true){
		alert("Cannot have different stop state for same start state and symbol");
		return;
	}
	// Pushing the states and symbols in the transition table into lists
	for(i=0;i<transition_list.length;i++){
		states_list.push(transition_list[i].start);
		symbol_list.push(transition_list[i].symbol);
	}
	for(i=0;i<transition_list.length;i++){
		states_list.push(transition_list[i].stop);
	}
	// Checking for Final states input
	var final_states_list=lines[lines.length-2].split(/ *: */)
	if(final_states_list[0]!=='Final'){
		alert("Final state not properly specified");
		return;
	}
	final_states_list=final_states_list[1].split(/ *, */);
	final_states_list = duplicateRemover(final_states_list);
	// Checking for "null" final states
	if(final_states_list.indexOf('')!==-1){
		alert("Invalid final state input");
		return;
	}
	// Pushing the states in final states to states list
	for(i=0;i<final_states_list.length;i++){
		states_list.push(final_states_list[i]);
	}
	//Checking for String input
	var string_input=lines[lines.length-1].split(/ *: */)
	if(string_input[0]!=='String'){
		alert("String to be checked not properly specified");
		return;
	}
	var string_to_check = string_input[1];
	// Removing Duplicates from states and symbol list
	states_list=duplicateRemover(states_list);
	symbol_list=duplicateRemover(symbol_list);
	var no_of_states = states_list.length;
	var no_of_symbol= symbol_list.length;
	// Verifing the data in transition table
	if(no_of_symbol*no_of_states!=transition_list.length){
		alert("Input data in transition table insufficient");
		return;		
	}
	// Generating and validating the data
	var generated_json=jsonGenerator(states_list,symbol_list,transition_list,final_states_list,string_to_check);
	validator(generated_json);

});
