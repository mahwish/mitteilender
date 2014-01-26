<%inherit file="base.mako"/>

 
<%def name="main_menu()"></%def>
  
    <div id="middle">
      <div class="middle align-center">
      
       
         &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
           <a href="${request.route_url('home')}"><img src="${request.static_url('mitteilender:static/home.png')}"></a>
             &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
           <a href="${request.route_url('add_project')}"><img src="${request.static_url('mitteilender:static/addd.png')}"></a> 
             &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
           <a href="${request.route_url('p_list')}"><img src="${request.static_url('mitteilender:static/edit.png')}"></a> 
           
           
           
       
        
        
                       </p></font></b>
      </div>
    </div>

<%def name="header()">
  <div id="top" style="text-align: left">
  
<br /><br /><br />
  <img src="${request.static_url('mitteilender:static/name.png')}"  alt="pyck"  align="middle"  />
    
 
  </div>
</%def>




<br /><br /><br />
<font color="teal" >
<pre><img src="${request.static_url('mitteilender:static/body.png')}"  alt="pyck"  width="40%" height="500%" align="right" style="opacity:0.7;filter:alpha(opacity=90);-webkit-transform:rotate(0deg);"/>
<h1><font color="teal" ><p>       Welcome to Mitteilender , a general application to design and
display information for any organization. It's Information designer 
helps to design information by using interactive user interface. 
You can add project of any domain and start the new world of
designing your client side screens. </p> </h1>
  </pre>
 
    
      </div>
    </div>

    
