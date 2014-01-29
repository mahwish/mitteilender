<%inherit file="base.mako"/>

 <!DOCTYPE html>
<html dir="ltr" lang="en-US"><head><!-- Created by Artisteer v4.0.0.58833 -->
    <meta charset="utf-8">
    <title>Home</title>
    <meta name="viewport" content="initial-scale = 1.0, maximum-scale = 1.0, user-scalable = no, width = device-width">

    <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
    <link rel="stylesheet" href="style.css" media="screen">
    <!--[if lte IE 7]><link rel="stylesheet" href="style.ie7.css" media="screen" /><![endif]-->
  




<style>.art-content .art-postcontent-0 .layout-item-0 { padding-right: 10px;padding-left: 10px;  }
.ie7 .post .layout-cell {border:none !important; padding:0 !important; }
.ie6 .post .layout-cell {border:none !important; padding:0 !important; }

</style></head>
<body>
<div id="art-main">
<nav class="art-nav clearfix">
    <div class="art-nav-inner">
    <ul class="art-hmenu"><li><a href="${request.route_url('home')}">Home</a></li><li><a href="${request.route_url('add_project')}">Add Project</a></li><li><a href="new-page-3.html">Add Project Items</a></li><li><a href="new-page-4.html">Edit Existing Project</a></li><li><a href="new-page-6.html">About Us</a></li><li><a href="new-page-7.html">Location</a></li></ul> 
        </div>
    </nav>
<header class="art-header clearfix">


    <div class="art-shapes">
<h1 class="art-headline" data-left="3.17%">
    <a href="#">Mitteilender</a>
</h1>
<h2 class="art-slogan" ><font size= "6px" color=#2B65EC>Information Designer</h2></font>

<div class="art-object0" data-left="86.95%"></div>

            </div>

                        
                    
</header>
<div class="art-sheet clearfix">
            <div class="art-layout-wrapper clearfix">
                <div class="art-content-layout">
                    <div class="art-content-layout-row">
                        <div class="art-layout-cell art-content clearfix"><article class="art-post art-article">
                                
                                                
             
    <div class="art-content-layout-row">
    <div class="art-layout-cell layout-item-0" style="width: 50px" "height: 60%" >
    

     
        <p><font color=#2B65EC size="3px"><b>
<div>
<h1>New Project</h1>
<br /><br /><br /><br />

<form action="${request.route_url('add_project')}" method="POST">
    ${add_project.as_p() | n}
    <br /><br /><br /><br /><br /><br />
   <pre>                                                <input type="submit" name="form.submitted" value="Create" /></pre>
</form>

<br /><br /><br /><br /><br /><br />
</div> 

</article></div>
                    </div>
                </div>
            </div>
    </div>
<footer class="art-footer clearfix">
  <div class="art-footer-inner">
<div class="art-content-layout">
    <div class="art-content-layout-row">
    <div class="art-layout-cell layout-item-0" style="width: 100%">
        <p>Copyright © 2013-2014, Mitteilender. All Rights Reserved. </p>
    </div>
    </div>
</div>

  
  </div>
</footer>

</div>


</body></html>


    

