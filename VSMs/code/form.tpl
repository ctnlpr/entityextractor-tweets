<html>
  <head>
  <meta http-equiv="Content-Type" content="text/html" charset = "utf-8"/>
      <title>Tamil NER</title>
  </head>
  <body>
  <style>
body  {
    
}
.button {
    background-color: dodgerblue;
    border: none;
    color: yellow;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
}
.button1:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}

.container {
     display: block;
    position: relative;
    padding-left: 35px;
    margin-left: 580px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 22px;
    color: indigo;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

/* Hide the browser's default radio button */
.container input {
    position: absolute;
    opacity: 0;
}

/* Create a custom radio button */
.checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
    border-radius: 150%;
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
    background-color: #ccc;
}

/* When the radio button is checked, add a blue background */
.container input:checked ~ .checkmark {
    background-color: #2196F3;
}

/* Create the indicator (the dot/circle - hidden when not checked) */
.checkmark:after {
    content: "";
    position: absolute;
    display: none;
}

/* Show the indicator (dot/circle) when checked */
.container input:checked ~ .checkmark:after {
    display: block;
}

/* Style the indicator (dot/circle) */
.container .checkmark:after {
 	top: 9px;
	left: 9px;
	width: 8px;
	height: 8px;
	border-radius: 50%;
	background: white;
}
header, footer {
    padding: 0.1em;
    color: blue;
    background-color: skyblue;
    clear: left;
    text-align: center;
}
</style>
<header>
<h1>Named Entity Recognition for Social Media Text - Tamil</h1>

</header>
    <form method="post" action="/api/formhandler">
        <fieldset>
            
            <ul>
               <div style="text-align:center"> 
        <textarea style="color:purple; resize:none; font-size: 14pt" id="myTextarea" NAME="first" ROWS="5" cols="55" placeholder="Enter the sentence here....."> </textarea>

		</div>
				<br>
		
            </ul> <div style="text-align:center"> 
        <button id="myButton" class="button button1"> Check </button>
        </div> 				
			
        </fieldset>
    </form>
<script type="text/javascript">
    document.getElementById("myButton").onclick = function () {
        var s1 = document.getElementById("myTextarea").value;
       
var val = '';

        if (s1 == "") {
        alert("Enter the sentence for first Text box");
        return false;
    }
    
    };
  
</script>
    
	<div align="center">

	
<h4 style="color:blue;">Your Input: {{info}} </h4>
<h4 style="color:purple;">Tagged Sentence: {{stm}}</h4>

		 </div>

<footer> <a href="http://nlp.amrita.edu/">Amrita CEN NLP Group</a> and <br> CNTLR</footer>		 
  </body>
</html>
   
