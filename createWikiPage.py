import mwclient
from mwclient import Site
import sys 
import scrapContent as scrap

url="sindhipedia.org"
site=Site(('http',url),path='/',)

def init_connection():
	user_name= 'Administrator'
	password= 'animation123'
	try:
		site.login(user_name, password)
		return 1
	except:		
		return 0

def delete_page(pageName):
	page = site.pages[pageName]
	print 'Deleting Page !', pageName
	page.delete()
	return "Page Deleted"

def create_page(pageName):
	page = site.pages[pageName]
	if (page.exists):
		print 'Page ' , pageName ,'Already exists'
		return "Page Already exists "
	else:
		print "Creating Page " , pageName
		print page.can('edit')
		text= scrap.scrapDynamic(pageName ,5); # result comes in sections so you have to define textspreadratio
		#print "Generator Output: ",text 
		page.save(text, 'Edit Summary')
		print 'Created Page' , pageName ,'!!'
		return 'Created Page: ' + pageName