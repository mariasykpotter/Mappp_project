The description of the module and the information on the map.
This program parses the file getting all the necessary information
about films such as their name, year when they were released and the location.
The user enters two parameters at the very beginning of the program including 
the year one is interested in and the color of the markers which will appear 
on the map. Then the module geopy is used to get the longitude and latitude of
the location where movies were filmed. Using imported module folium,
we make three layers on the map. The first one is just a map, the second layer consists
of names, and the third contains location markers which will appear at the exact coordinates
provided by geopy module. The created layer control makes the interface more comfortable as 
the user can switch the layer by putting a tick after one or both of two categories: "names" 
and "locations." It is important also to add that the file from which we get the information 
should appear in the same folder where the program is. What is more, the map will also be 
created in this particular folder and saved as an HTML file.
Conclusion:
All in all, the map gives a deep analysis of the distribution of films locations and the years
when they were released.

Description of basic HTML tags.

<!DOCTYPE html>  - Define the document type.
<head>   - Defines a header for a document or section
   <meta  - Defines metadata about an HTML document. The <meta> tag provides metadata about the HTML document. Metadata will not be displayed on the page, but will be machine parsable.
http-equiv="content-type"  Provides an HTTP header for the information/value of the content attribute
content="text/html; Specifies the content of the document
charset=UTF-8" />  Specifies the character encoding for the document.

   <script>  - The <script> tag is used to define a client-side script (JavaScript). The <script> element either contains scripting statements, or it points to an external script file through the src attribute.

L_PREFER_CANVAS=false; - specify that vector layers are drawn in Canvas
L_NO_TOUCH=false;  -

L_DISABLE_3D=false;</script>

   <script src="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.js"></script> - include Leaflet 1.3.4, a JS library for interactive maps


   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
Included Java Script library Leaflet 1.3.4, a JS library for interactive maps

   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>Included Java Script library Bootstrap


   <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>

   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.css"/>

Defines the relationship between a document and an external resource ( style sheets).Is used to link to external style sheets
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
   <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
   <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
   <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
  
   <meta name="viewport" content="width=device-width,
       initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

Let web designers take control over the viewport, through the <meta> tag.
The viewport is the user's visible area of a web page. It varies with the device, and will be smaller on a mobile phone than on a computer screen.A <meta> viewport element gives the browser instructions on how to control the page's dimensions and scaling.
The width=device-width part sets the width of the page to follow the screen-width of the device (which will vary depending on the device).
The initial-scale=1.0 part sets the initial zoom level when the page is first loaded by the browser.
 

   <style>#map_e0c6ff598dfb4547b8b513c9ad6e0da8 {
       position: relative;
       width: 100.0%;
       height: 100.0%;
       left: 0.0%;
       top: 0.0%;
       }
   </style>
</head>
<body>   
The <body> tag defines the document's body.
The <body> element contains all the contents of an HTML document, such as text, hyperlinks, images, tables, lists, etc.

  
   <div class="folium-map" id="map_e0c6ff598dfb4547b8b513c9ad6e0da8">
The <div> tag defines a division or a section in an HTML document.
The <div> element is often used as a container for other HTML elements to style them with CSS or to perform certain tasks with JavaScript.
 

</div>
</body>
<script>   
  
  
       
