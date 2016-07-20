import mwclient
from mwclient import Site
import sys 


url="sindhipedia.org"
user_name= '*****'
password= '****'
page_name= sys.argv[1]



site=Site(('http',url),path='/',)

site.login(user_name, password)

page = site.pages[sys.argv[1]]

if sys.argv[2] == '-d':
	print 'Deleting Page !', sys.argv[1]
	page.delete()

if (page.exists):
	print 'Page ' , sys.argv[1] ,'Already exists'
	sys.exit()
else:
	print "Creating Page " , sys.argv[1]
	print page.can('edit')
	text="Created this using a Bot"
	page.save(text, 'Edit Summary')
	print 'Created Page' , sys.argv[1] ,'!!'