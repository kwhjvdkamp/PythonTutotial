from scrapy import Selector

html = '''
<html>
    <body>
        <div>Div 1: <p>paragraph 1</p></div>
        <div>Div 2: <p>paragraph 2</p> <p>paragraph 3</p> </div>
        <div>Div 3: <p>paragraph 4</p> <p>paragraph 5</p> <p>paragraph 6</p></div>
        <div>Div 4: <p>paragraph 7</p></div>
        <div>Div 5: <p>paragraph 8</p></div>
    </body>
</html>
'''
sel = Selector(text=html)
# Create a Selector selecting html as the HTML document
sel = Selector( text=html )
# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( "//div" )
print(divs)
print(divs[2])
# OUTPUT
# [
#   <Selector xpath='//div' data='<div>Div 1: <p>paragraph 1</p></div>'>,
#   <Selector xpath='//div' data='<div>Div 2: <p>paragraph 2</p> <p>par...'>,
#   <Selector xpath='//div' data='<div>Div 3: <p>paragraph 4</p> <p>par...'>,
#   <Selector xpath='//div' data='<div>Div 4: <p>paragraph 7</p></div>'>,
#   <Selector xpath='//div' data='<div>Div 5: <p>paragraph 8</p></div>'>
# ]
print(divs[2].xpath('./*'))
# OUTPUT
# <Selector xpath='//div' data='<div>Div 3: <p>paragraph 4</p> <p>par...'>
# [
#   <Selector xpath='./*' data='<p>paragraph 4</p>'>,
#   <Selector xpath='./*' data='<p>paragraph 5</p>'>,
#   <Selector xpath='./*' data='<p>paragraph 6</p>'>
# ]
print(len( divs[2].xpath('./*') ))
# OUTPUT
# 3
print(len( divs[2] ))
# OUTPUT
# TypeError: object of type 'Selector' has no len()
# The code divs[2] is one element from a SelectorList, and therefore is a Selector (not another SelectorList)