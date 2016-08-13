from selenium import webdriver
import re 
import mechanize 
import selenium
import bs4
import time 

# params : Person , Building , Event 
textMinerURL= "http://www.sensebot.net/sense6.aspx";
br= mechanize.Browser()
br.addheaders=[('User-agent','Firefox')]
br.set_handle_robots(False)
br.set_handle_refresh(False)
browser=webdriver.PhantomJS();

def scrapStatic( searchKeyword ):
	br.open(textMinerURL);
	br.select_form("ctl00"); # form element name 
	br.form['Query']= searchKeyword
	result= br.submit()
	output= result.read()
	parsedHTML=bs4.BeautifulSoup(output);	
	return parsedHTML # further process this text using html



def setScrappingParams( param1 , param2):
	return 0
def createTemplate():
	return 0;	

def scrapDynamic ( searchKeyword , textSpreadRatio): # scraps pages with Javascript loading
	browser.get(textMinerURL);
	element=browser.find_element_by_name("Query");
	element.clear();
	element.send_keys(searchKeyword);
	element.submit();
	elementSearchSubmit=browser.find_element_by_name("btnSearch");
	elementSearchSubmit.click();
	output=browser.page_source;
	parsedHTML=bs4.BeautifulSoup(output);
	result=parsedHTML.find("td",{"id":"OutCell"});
	text= result.renderContents();
	#print text
	return HTML2Wiki(text, textSpreadRatio , searchKeyword);
	# take language 
	# Loop through number of headings 
	# Replace Stuff with body	
def HTML2Wiki (HTMLString,textSpreadRatio , title):
	template = "<onlyinclude>'''Title''' ( [[Language]] '''???????? ??? ???''' )'Intro Piece'</onlyinclude>\n== Heading1 ==\nBody1\n\n== Heading2 ==\n\nBody2\n"
	WikiString= HTMLString.split('<br/>');
	#for count in range(len(WikiString)):
		#print "======="+str(count)+"========="
		#print WikiString[count];
	originalCount= 1;
	numberofHeadings= len(WikiString)/textSpreadRatio;
	#print "=====Number of Headings : " + str(numberofHeadings); 
	OutputString= "<onlyinclude>'''Title''' ( [[Language]] '''???????? ??? ???''' )'"+WikiString[originalCount]+"'</onlyinclude>\n"
	OutputString= OutputString.replace("Title",title)
	print OutputString;
	for count in range (1, numberofHeadings):
		OutputString = OutputString + "\n== Heading"+str(count)+" ==\n"
		for itr in range (1, textSpreadRatio):
			try:
				OutputString = OutputString + WikiString[originalCount];
				originalCount= originalCount + itr;
			except IndexError:					
					OutputString=OutputString+"\n== List1 ==\n\nListBody1\n\n* ListElement1\n* ListElement2\n\n== NoBodyList1 ==\n* NoBodyListElement1\n* NoBodyListElement2\n* NoBodyListElement1\n\n\n[[Category:Tag1]]\n"
					return OutputString;
	OutputString=OutputString+"\n== List1 ==\n\nListBody1\n\n* ListElement1\n* ListElement2\n\n== NoBodyList1 ==\n* NoBodyListElement1\n* NoBodyListElement2\n* NoBodyListElement1\n\n\n[[Category:Tag1]]\n"
	return OutputString;					