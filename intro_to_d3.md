#Introduction to data viz

##Intro

D3 is a powerful data visualization framework, written in Javascript, for folks who want to get into the guts and make their visualizations beautiful.  That being said, it still holds your hand a lot, in the sense of giving you high level functions that allow you to get stuff done.  D3's little brother, C3 is an even higher level Javascript library, that implements many common D3 patterns automatically.

##installation

To start using D3, it is recommended that you [download it](http://d3js.org/d3.v3.js) and reference it locally for debugging.  When you are ready to move to production, it is recommended that you make use of the [minified form of D3](http://d3js.org/d3.v3.min.js).  If you did need to edit the D3 source, there are many minifiers out there like [this one](http://jscompress.com/)

##Some precursors

Before we jump right into D3, we'll need to understand a little about HTML, CSS, and Javascript (client-side).

###The DOM

The DOM (Document Object Model) is how HTML documents are organized.  HTML is ordered hierarchically, with outer tags being further up in the html tree.  

So say you had the following HTML document:

```
<html>
 <p>Hello</p>
</html>
```

Here `<html>` would be parent tag and the `<p>` would be the child tag.  Thus, when traversing the html document for information, we would travel from the html-tag to the p-tag.  This is how [xpath](http://en.wikipedia.org/wiki/XPath) and other html traversal tools parse html / xml documents.

Making use of this in javascript is pretty easy, but we'll need a slightly more complete example:

```
<html>
<body>

<p id="changeable_text">Hello world!</p>
<p>Hello world!</p>
<script>

document.getElementById("changeable_text").style.color="blue"; 

</script>
</body>
</html>
```

If you run the above code, the p-tag with the id - `changeable_text` should appear blue.  This is because the document object referenced it, which we then manipulated.  This is a core idea in how D3 and other document manipulation frameworks can become powerful.  Of course, we didn't use any D3, yet, just straight Javascript.  But this should give you an intuitive idea of how D3 was written - by manipulating the document object.

For a longer introduction into html you can always check out [this tutorial](http://www.syncano.com/getting-know-javascript-intro/)

###A very small tour of CSS

CSS or Cascading Style Sheets are used to augment html tags, by adding visual elements.  

For example:

```
body {
    background-color: white;
    color: black;
}
```

CSS consists of rules and selectors.  In the above example, the selector was the `body` and the rules were `background-color:white`, `color:black`.  The rules augment the selected elements - tags, ids, and classes.

##Getting started with D3

Now that we understand the bare minimium of other languages, let's write our first d3 application:

`d3.select("body").append("p").text("Hello World!");`

So as you may have guessed, select will select the tag of interest and then append will add that tag.  The text method will insert text.  So we've injected text into our html dynamically!  Pretty neat huh?  But it's nothing javascript can't do already.  

Here is the real power:

```
var data = {{data|tojson|safe}};
 var data = JSON.parse(data);
 //alert(data.data); //testing
 //var dataset = data.data;
 var dataset = data;
//alert(dataset);
d3.select("body").selectAll("div")
	.data(dataset)
	.enter()
	.append("div")
	.attr("class","bar")
	.style("height", function(d){
		var barHeight = d * 2;
		return barHeight + "px";
	});
```

Here we are making use of a flask template to pull in the data as json and then load it into html.



##Resources:
* [Intro to D3](http://alignedleft.com/tutorials/d3)
* [Intro to C3](http://c3js.org/gettingstarted.html)


