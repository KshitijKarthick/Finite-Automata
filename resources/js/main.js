var n_fin;
var n_states;
var n_alphabets;
var alpha;
var len;
var st=1,al=1,alp=1,nf=1;
var regex=/^[0-9]+$/;
var transition_list=[];
var valid_states=[];
var no_fin;
var final_states;
var string_to_check;
function make_table(){
	var table=$("#trans_table");
	var row2add="";
	for( var y=0; y<n_states;y++)
	{
		for(var z=0; z<n_alphabets;z++)
		{
			row2add="<tr>";
			row2add += "<td>" +"q"+y+"-----"+ "</td>";
			row2add += "<td>"+alpha[z]+"---->"+ "</td>";
			row2add += "<td>"+"<input id=in_"+ y + z +">"+"</input>"+ "</td>";
			row2add += "</tr>";
			table.append(row2add);
		}

	}
	var e=$('<button id="btn_tab" value="generate new element">submit</button>');
	$('#div7').append(e);
}
//.one() can be used but it does not allow us to discard multiple incorrect inputs
$('#div1').on('click','#btn_states',function(){
	n_states=$('#no_states').val();
	if(!n_states.match(regex))
		alert("Please enter a number");
		else if((st--)>0)//due to the use of op-- , once valid input is given , it cannot be changed
		{	
			var y;
			var temp_state;
			$('#btn_states').hide();
			for(y=0;y<n_states;y++)
			{
				temp_state="q"+y;
				valid_states.push(temp_state);
			}
			var r= $('<input type="number" id="no_alphabets" value="generate new element"/>');
			var s=$('<button id="btn_alphabets" value="generate new element">submit</button>');
			$('#div2').append("Enter the number of alphabets:")
			$('#div2').append(r);
			$('#div2').append(s);
		}
});

$('#div2').on('click','#btn_alphabets',function(){
	n_alphabets=$('#no_alphabets').val();
	if(!n_alphabets.match(regex))
		alert("please enter a number");
	else if((al--)>0)
	{
		$('#btn_alphabets').hide();
		var p= $('<input type="text" id="alphabets"/>');
		var q=$('<button id="btn_alpha" value="generate new element">submit</button>');
		$('#div3').append("Enter the alphabets seperated by a comma:")
		$('#div3').append(p);
		$('#div3').append(q);
	}
});	
$('#div3').on('click','#btn_alpha',function(){
	var temp=$('#alphabets').val();
	alpha=temp.split(",");
	len=alpha.length;
	if(len!=n_alphabets)
		alert("Please enter the proper number of alphabets");
	else if((alp--)>0)
	{
		for(y=0;y<n_alphabets;y++)
		{
			for(z=y+1;z<n_alphabets;z++)
				if(alpha[y]==alpha[z])
				{
					alert("please enter unique alphabets");
					alp++;
					return;
				}
		}
			$('#btn_alpha').hide();
			var t=$('<button id="btn_start" value="generate new element">click to enter transition table</button>');
			$('#div4').append(t);
	}
});

//.one allows the statements following an event to occur only once 
$('#div4').on('click','#btn_start',function(){
	$('#btn_start').hide();
	$('#div4').append("<br>Fill the table.<br>q0 is the initial state");
	$('#div5').append("Enter the number of final states");
	var m=$('<input type="number" id="no_finalstates"/>');
	$('#div5').append(m);
	var n=$('<button id="btn_no_fin" value="generate new element">submit</button>');
	$('#div5').append(n);
});

$('#div5').on('click','#btn_no_fin',function(){
	no_fin=$('#no_finalstates').val();
	if(!no_fin.match(regex))
	{
		alert("Enter a number");
		return;
	}
	else if(no_fin>n_states)
	{
		alert("Number of final states should not be greater than the number of states");
		return;
	}
	else(nf--)
	{
		$('#btn_no_fin').hide();
		$('#div6').append("Enter the final states seperated by a comma");
		var s1=$('<input type="text" id="final_states"/>');
		var p1=$('<button id="btn_fin" value="generate new element">submit</button>');
		$('#div6').append(s1);
		$('#div6').append(p1);
	}
});

$('#div6').on('click','#btn_fin',function(){
	var temp1;
	temp1=$('#final_states').val();
	final_states=temp1.split(',');
	var len1=final_states.length;
	if(no_fin!=len1)
	{
		alert("Enter the appropriate number of final states");
		return;
	}
	else
	{
		$('#btn_fin').hide();
		make_table();
	}
});

$('#div7').on('click','#btn_tab',function(){
	var start_state;
	var transistion_symbol; 
	var next_state;
	var temp;
	var x;
	for( var y=0; y<n_states;y++)
	{
		for(var z=0; z<n_alphabets;z++)
		{
			start_state="q"+y;
			transistion_symbol=alpha[z];
			next_state=$("#in_"+y+z).val();
			temp = {'start':start_state,'symbol':transistion_symbol,'stop':next_state};
			transition_list.push(temp);	
		}
	}
	for(y=0;y<transition_list.length;y++)
		if(valid_states.indexOf(transition_list[y].stop)===-1){
			alert("Enter valid states ");
			transition_list=[];
			return;
		}
	$('#btn_tab').hide();
		var m1=$('<input type="text" id="inp_string"/>');
		var n1=$('<button id="btn_input_string" value="generate new element">submit</button>');
		$('#div8').append("Enter the string to be validated");
		$('#div8').append(m1);
		$('#div8').append(n1);
	});
	$('#div8').on('click','#btn_input_string',function(){
		$('#btn_input_string').hide();
		string_to_check=$('#inp_string').val();
	var generated_json=jsonGenerator(valid_states,alpha,transition_list,final_states,string_to_check);
	validator(generated_json);
});
