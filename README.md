# textart
A small module to help render simple text art in a similar fasion as pygame

Two main features:
The Art class, represents a grid of characters

## Installation:

```
pip install textart
```

## Functions:
```
art.copy(area=None)
```
Creates a copy of the art  
area is None, [x, y], [x, y, size] or [x, y, width, height], None means all
  
```	 
art.rect(character, rect, border=0)
```
  
Draws a rectangle of that character on to the art  
rect is a list [x, y, width, height]  
  
  
```	 
art.square(character, pos, size, border=0)
```
shorthand for art.rect(character, [pos[0], pos[1], size, size], border=0)  
post is a list [x, y]

```
art.circle(character, pos, radius, border=0)
```
Draws a circle of that character on to the art  
pos is a list [x, y]


```
art.line(character, start, end, border=0)
```	 
Draws a line from the start to the end with a width of border  
start and end are lists [x, y]

```
art.lines(character, points, border=0)
```
Shorthand for art.line(character, p1, p2, border=0) art.line(character, p2, p3, border=0) etc.  
where points = [p1, p2, p3, ...] and p1, p2, p3, ... are lists [x, y]


```
art.triangle(character, p1, p2, p3, border=0)
```
Draws a triangle on to the start  
p1, p2, p3 are lists [x, y]


```
art.quad(character, p1, p2, p3, p4, border=0)
```	 
Draws a quadrilateral on to the art  
p1, p2, p3, p4 are lists [x, y]


```
art.polygon(character, points, border=0)
```
Draws a polygon defined by the list of points  
points = [p1, p2, p3, ...] and p1, p2, p3 are list [x, y]


```
art.gradient(char_gradient, start, end, area=None)
```	 
Renders a gradient defined by char_gradient in the area  
the gradient line is defined by start and end  
char_gradient is a string  
start, end are lists [x, y]  
area is None, [x, y], [x, y, size] pr [x, y, width, height], None means all


```
art.blit(source, dest=[0,0], area=None, alpha=" ")
```	
Renders the source art on to this art  
dest is a list [x, y] defining where it renders the source art  
area is None, [x, y], [x, y, size] or [x, y, width, height] and definds the area of the source to render, None means all


```
art.filter(func, area=None, bychar=False)
```
Filters the art,  
func is a function with paramters func(art, line) or func(art, char) depending on if bychar is False or True, respectively  
func has to return what the line/char will be replaced with    
area is None, [x, y], [x, y, size] or [x, y, width, height], None means all  
bychar=False is a lot more efficient.  


```
art.replace(old, new, area=None, inplace=False, bychar=False, cut=False)
```
Replaces all instances of 'old' with 'new'  
old and new are strings, must be the same length (or bychar=True and len(new)=1)  
area is None, [x, y], [x, y, size] or [x, y, width, height], None means all  
inplace determines if the replace will return a new copy of the art with the replacements or replace them in the art, defaults to False, return a new copy  
bychar determines if the replacements will be done per character,  
if bychar=False:  
> replaces all instances of 'old' with 'new' within the area

if bychar=True:  
> does it on a per-char basis, e.g. art.replace('xyz', '123', bychar=True) is shorthand for  
> art.replace('x', '1') art.replace('y', '2') art.replace('z', '3')  
> if new is a single character, it replaces all of old with new, e.g. art.replace('xyz', '1', bychar=True) is shorthand for  
> art.replace('x', '1') art.replace('y', '1') art.replace('z', '1')  

cut determines if the replacement will cut out the area and return it or return the whole thing, if true overrides inplace defaults to False, return the whole art  


```
art.swap(s1, s2, area=None, inplace=False, bychar=False, cut=False)
```
Sets all occurances of s1 to s2 and all occurances of s2 to s1  
s1 and s2 are strings, must be the same length  
area is None, [x, y], [x, y, size] or [x, y, width, height], None means all  
inplace determines if the replace will return a new copy of the art with the replacements or replace them in the art, defaults to False, return a new copy  
bychar determines if the swaps will be done per character,  
if bychar=False:  
> swaps all instances of 'old' with 'new' within the area  

if bychar=True:  
> does it on a per-char basis, e.g. art.swap('xyz', '123', bychar=True) is shorthand for  
> art.swap('x', '1') art.swap('y', '2') art.swap('z', '3')

cut determines if the replacement will cut out the area and return it or return the whole thing, if true overrides inplace defaults to False, return the whole art  


```
art.batch(batch)
```	
Calls a batch of functions,  
batch is a dictionary with the format:  
	{ "function-name": [args], ... }
	

```
art.text()
```
returns the lines of the art (a list of strings)


```
art.print()
```
prints the art in the console


```
art.dtext(style="")
```
returns the art formatted for discord chat (a single string)


##artscript:
A very simple scripting language to create and manipulate art objects

```
art_script(width, height, lines)
```
Runs some artscript code
width, height is the width and height of the main art object  
lines is a list of strings, each string being a line of code  
  
see the source at https://github.com/billy-yoyo/textart/blob/master/textart.py#L537 for details on how to use artscript
