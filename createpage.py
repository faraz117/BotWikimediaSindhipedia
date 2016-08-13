import mwclient
from mwclient import Site
import sys 
import scrapContent as scrap


url="sindhipedia.org"
user_name= 'Administrator'
password= 'animation123'
page_name= sys.argv[1]
site=Site(('http',url),path='/',)
site.login(user_name, password)
page = site.pages[sys.argv[1]]

if sys.argv[2] == '-d':
	print 'Deleting Page !', sys.argv[1]
	page.delete()
	sys.exit()
if (page.exists):
	print 'Page ' , sys.argv[1] ,'Already exists'
	sys.exit()
else:
	print "Creating Page " , sys.argv[1]
	print page.can('edit')
	text= scrap.scrapDynamic(sys.argv[1] ,5); # result comes in sections so you have to define textspreadratio
	#print "Generator Output: ",text
	page.save(text, 'Edit Summary')
	print 'Created Page' , sys.argv[1] ,'!!'