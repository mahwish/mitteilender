<%inherit file="base.mako"/>

<%def name="title()">

</%def>

<div>
 <form action="${request.route_url('primary_display',item_id=item_id)}" method="POST">




      
              
         

 
%for i in data:
 <input type="radio" name=primary_display value=${i['db_id']}> ${i['field_name']}
 <br /><br /><br />
 %endfor
<br /><br /><br />

  <input type="submit" name="form.submitted" value="Edit " />
</form>



</div>

<<<<<<< HEAD

=======
<link rel="stylesheet" href="../../_static/js/dojo/../dijit/themes/claro/claro.css">
	
	<script>dojoConfig = {async: true, parseOnLoad: true}</script>
	<script src='../../_static/js/dojo/dojo.js'></script>
	
	<script>
require(["dojo/parser", "dijit/form/NumberSpinner"]);
	</script>
</head>
<body class="claro">
    <input data-dojo-type="dijit/form/NumberSpinner"
    id="integerspinner2"
    value="1000"
    data-dojo-props="smallDelta:10, constraints:{min:9,max:1550,places:0}"
    name="someNumber"
    />
    <body class="claro">
    <div id="spinnerId"></div>
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332

