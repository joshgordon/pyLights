<html><head><title>LED Lights</title>

</head>

<body>
  
<script src="jquery.js"></script> 

<script type="text/javascript">
$('light_form#submit').click(function() { 
    $.ajax({
	type: "POST", 
	url: "http://pi:8080/handler.py", 
	data: { 
	    white: light_from#white; 
	} 
	success: function(msg){ 
	    alert('blah'); 
	} 
    }); 
}); 

</script> 

<div id="light_form">
  <form name="colors" action=""> 
    <fieldset>
      <label for="white" id="white_label">White</label>
      <input type="text" name="white" id="name" size="30" value="" class="text-input" /> 
      <input type="submit" name="submit" class="button" id="submit_btn" value="Updtate" />
    </fieldset>
  </form>
</div> 

</div> 

</body> 
</html> 
