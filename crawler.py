import re
import requests
from pattern import web
from pattern.web import plaintext, strip_between
import cPickle as pickle
page=['a','b','c','d','e','f','g','h','i']
newline="\n"
list1=[]
for p in page:
    url="http://www.airlinequality.com/Forum/sia_1"+p+".htm"
    html_txt=requests.get(url).text
    dom=web.Element(html_txt)
    for x in dom.by_tag('p.text2'):
           no_format = plaintext(x.content)
           comment = re.sub( '\s+', ' ', no_format).strip()
           if (comment!='PAGE 1 2 3 4 5 6 7 8 9 10') and (comment!=''):
           	list1.append(comment.encode('utf-8'))
           	



for i in range(len(list1)):
	fn="cmt_0%d"%(i,)
	fo=open(fn,"wb")
        pickle.dump(list1[i],fo)
	fo.close()
