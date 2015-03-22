// Takes the input data from the user and converts it into json that we sent to the server
function jsonGenerator(states_list,symbol_list,transition_list,final_states_list,string){
	var sending_json={};
	// Initialize the json
	sending_json['no_of_states']=states_list.length;
	sending_json['no_of_symbols']=symbol_list.length;
	sending_json['string']=string;
	sending_json['states']={};
	sending_json['symbols']=symbol_list;
	sending_json['states']={};
	for (var i = 0; i < states_list.length; i++) {
		sending_json.states[i]={};
		sending_json.states[i]['Transitions']=[];
		for (var j = 0; j < symbol_list.length; j++) {
			sending_json.states[i].Transitions.push(0);
		}
		sending_json.states[i]['Final']=0;
	}
	// Adding respective transition values to the json
	for (var i = 0; i < transition_list.length; i++) {
		sending_json.states[states_list.indexOf(transition_list[i].start)].Transitions[symbol_list.indexOf(transition_list[i].symbol)]=(states_list.indexOf(transition_list[i].stop));
	}
	// Setting proper values to final states
	for (var i = 0; i < final_states_list.length; i++) {
		sending_json.states[states_list.indexOf(final_states_list[i])].Final=1;
	}
	return sending_json;
}

function transitionsGenerator(transitions){
	var a=[];
	for (var i = 0; i < transitions.length; i++) {
		a.push(transitions[i][0]+"+"+transitions[i][1]+"->"+transitions[i][2]);
	}
	return a;
}

function displayOutput(reply){
	if(reply.Valid!==1){
		$('#output_box').attr('text',"String not valid");
	}
	else{
		var output=transitionsGenerator(reply.Transitions);
		$('#output_box').attr('text',output);
	}
	output_box.show();
}
// Sends the json and returns the validity and transitions made 
function validator(json){
	var recieved_json;
	$.ajax({
		type: 'POST',
		url: '/dfa/',
		data: JSON.stringify(json),
		success: function(reply) { 
	    	displayOutput(reply);
		},
		contentType: "application/json",
		dataType: 'json'
	});
}
