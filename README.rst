A small module to help render simple text art in a similar fasion as pygame

Two main features:
The Art class, represents a grid of characters

functions:
	 art.copy(area=None)
		 creates a copy of the art
		 
	 art.rect(character, rect, border=0)
		 rect is a list [x, y, width, height]
		 draws a rectangle of that character on to the art
		 
	 art.square(character, pos, size, border=0)
		 pos is a list [x, y]
		 shorthand for art.rect(character, [pos[0], pos[1], size, size], border=0)

	 art.circle(character, pos, radius, border=0)
		 pos is a list [x, y]
		 draws a circle of that character on to the art
		 
	 art.line(character, start, end, border=0)
		 start and end are lists [x, y]
		 draws a line from start to end with a width of border
		 
	 art.lines(character, points, border=0)
		 where points = [p1, p2, p3, ...] and pi are lists [x, y]
		 shorthand for art.line(character, p1, p2, border=0) art.line(character, p2, p3, border=0) etc.
		 without looping
		 
	 art.triangle(character, p1, p2, p3, border=0)
		 p1, p2, p3 are lists [x, y]
		 draws a triangle on to the art
		 
	 art.quad(character, p1, p2, p3, p4, border=0)
		 p1, p2, p3, p4 are lists [x, y]
		 draws a quadrilateral on to the art
		 
	 art.polygon(character, points, border=0)
		 where points = [p1, p2, p3, ...] and pi are lists [x, y]
		 draws a polygon definded by the list of points on to the art
		 
	 art.gradient(char_gradient, start, end, area=None)
		 char_gradient is a string
		 start, end are lists [x, y]
		 area is None, [x, y], [x, y, size] or [x, y, width, height], None means all
		 renders a gradient defined by char_gradient in the area, None means all of the object
		 the gradient line is defined by start, end

	 art.blit(source, dest=[0,0], area=None, alpha=" ")
		 renders the source art on to the art,
		 dest is a list [x, y] defining there it renders on the art
		 area is None, [x, y], [x, y, size] or [x, y, width, height] and defines the area of the source to render, None means all
		 alpha is a string containing all the characters from source it will ignore (it won't render them)

	 art.filter(func, area=None, bychar=False)
		 filters the art,
		 func is a function with paramters func(art, line) or func(art, char) depending on if bychar is False or True, respectively
		 func has to return what the line/char will be replaced with   
		 area is None, [x, y], [x, y, size] or [x, y, width, height], None means all
		 bychar=False is a lot more efficient.
		
	 art.replace(old, new, area=None, inplace=False, bychar=False, cut=False)
		 old and new are strings, must be the same length (or bychar=True and len(new)=1)
		 area is None, [x, y], [x, y, size] or [x, y, width, height], None means all
		 inplace determines if the replace will return a new copy of the art with the replacements or replace them in the art,
		 defaults to False, return a new copy
		 bychar determines if the replacements will be done per character,
		 if bychar=False:
			   replaces all instances of 'old' with 'new' within the area
		 if bychar=True:
			   does it on a per-char basis, e.g. art.replace('xyz', '123', bychar=True) is shorthand for
			   art.replace('x', '1') art.replace('y', '2') art.replace('z', '3')
			   if new is a single character, it replaces all of old with new, e.g. art.replace('xyz', '1', bychar=True) is shorthand for
			   art.replace('x', '1') art.replace('y', '1') art.replace('z', '1')
		 cut determines if the replacement will cut out the area and return it or return the whole thing, if true overrides inplace
		 defaults to False, return the whole art

	art.swap(s1, s2, area=None, inplace=False, bychar=False, cut=False)
		 s1 and s2 are strings, must be the same length
		 area is None, [x, y], [x, y, size] or [x, y, width, height], None means all
		 inplace determines if the replace will return a new copy of the art with the replacements or replace them in the art,
		 defaults to False, return a new copy
		 bychar determines if the swaps will be done per character,
		 if bychar=False:
			   swaps all instances of 'old' with 'new' within the area
		 if bychar=True:
			   does it on a per-char basis, e.g. art.swap('xyz', '123', bychar=True) is shorthand for
			   art.swap('x', '1') art.swap('y', '2') art.swap('z', '3')
		 cut determines if the replacement will cut out the area and return it or return the whole thing, if true overrides inplace
		 defaults to False, return the whole art

	art.batch(batch)
		 calls a batch of functions,
		 batch is a dictionary with the format:
			  { "function-name": [args], ... }

	art.text()
		 returns the lines of the art (a list of string)

	art.print()
		 prints the art in to the consol

	art.dtext(style="")
		 returns the  art formatted for discord chat (a single string)

artscript:
	 A very simple scripting language to create and manipulate art objects

function:
	 art_script(width, height, lines)
		 width, height is the width and height of the main art object
		 lines is a list of strings, each string being a line of code

see the source at 
for details on how to use artscript