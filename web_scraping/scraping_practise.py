from scrapy import Selector

from scrapy.crawler import CrawlerProcess

import requests


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


# url = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'
# # Create the string html containing the HTML source
# html = requests.get( url ).content
# # Create the Selector object sel from html
# sel = Selector( text = html)
# # Print out the number of elements in the HTML document
# print( "There are 1020 elements in the HTML document.")
# print( "You have found: ", len( sel.xpath('//*') ) )


# html = '''
# <html>
#     <body>
#         <div id="this-div">
#             <p id="p1" class="class-1">This is not the element you are looking for</p>
#             <p id="p2" class="class-12">
#                 <a href="https://www.google.com">Google</a> is linked to here, but this isn't the link you are looking for.
#             </p>
#             <p id="p3" class="class-1 class-12">Here is the <a href="https://www.datacamp.com" id="a-exercise">DataCamp</a> link you want!
#             </p>
#         </div>
#     </body>
# </html>
# '''
# print(html)
# sel = Selector(text=html)

# Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which does NOT include the text of future generations of this p element.
# Assign to the variable css_locator a CSS Locator string directing to this same text.
# print('CSS', sel.css('p#p3::text'))
# print('XPath', sel.xpath('//p[@id="p3"]/text()'))
# # OUTPUT
# CSS [
#   <Selector xpath="descendant-or-self::p[@id = 'p3']/text()" data='Here is the '>,
#   <Selector xpath="descendant-or-self::p[@id = 'p3']/text()" data=' link you want!\n'>]
# XPath [
#   <Selector xpath='//p[@id="p3"]/text()' data='Here is the '>,
#   <Selector xpath='//p[@id="p3"]/text()' data=' link you want!\n'>]

# Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which DOES includes the text of future generations of this p element.
# Assign to the variable css_locator a CSS Locator string directing to this same text.
# print('CSS', sel.css('p#p3 ::text'))
# print('XPath', sel.xpath('//p[@id="p3"]//text()'))
# # OUTPUT
# CSS [
#   <Selector xpath="descendant-or-self::p[@id = 'p3']/descendant-or-self::text()" data='Here is the '>,
#   <Selector xpath="descendant-or-self::p[@id = 'p3']/descendant-or-self::text()" data='DataCamp'>,
#   <Selector xpath="descendant-or-self::p[@id = 'p3']/descendant-or-self::text()" data=' link you want!\n'>]
# XPath [
#   <Selector xpath='//p[@id="p3"]//text()' data='Here is the '>,
#   <Selector xpath='//p[@id="p3"]//text()' data='DataCamp'>,
#   <Selector xpath='//p[@id="p3"]//text()' data=' link you want!\n'>]


# # Get the URL to the website loaded in response
# # this_url = response.url
# # print(this_url)
# this_url = 'https://www.datacamp.com/courses/all'
# # # Create the string html containing the HTML source
# html = requests.get( this_url ).content
# # # Create the Selector object sel from html
# sel = Selector( text = html)
# # Get the title of the website loaded in response via XPath
# this_title_xpath = sel.xpath('/html/head/title/text()').extract_first()
# # Get the title of the website loaded in response via CSS
# this_title_css = sel.css('html > head > title::text').extract_first()
# # Print out our findings
# print('XPath', this_url, this_title_xpath )
# print('=============')
# print('CSS', this_url, this_title_css )
# # https://www.datacamp.com/courses/all
# # XPath
# # Here is what you found:
# # 	-URL: https://www.datacamp.com/courses/all
# # 	-Title: Data Science Courses: R & Python Analysis Tutorials | DataCamp
# # =============
# # CSS
# # Here is what you found:
# # 	-URL: https://www.datacamp.com/courses/all
# # 	-Title: Data Science Courses: R & Python Analysis Tutorials | DataCamp