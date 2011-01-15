import constants
import urllib2
from xml.etree import ElementTree as ET


class movie:

  def get_imdb_list(self):
	  return self.similar_movie_imdb_id

  def get_similar_movie_titles(self,title):
	"""Returns a list of movies similar to one given by user"""
	#generating search query
	search = constants.SEARCH_MOVIE + constants.API_KEY + '/' + title
	xml = urllib2.urlopen(search).read()
	filehandler= open('a.xml','w')
	filehandler.write(xml)
	filehandler.close()
	#print xml
	#exit(0)
	self.similar_movie_list_title = []
	self.similar_movie_list_id = []
	self.similar_movie_imdb_id = []
	tree= ET.parse('a.xml')
	doc = tree.getroot()
	
	moviessubtree = doc.find('movies')
	for i in moviessubtree.getiterator('id'):
		self.similar_movie_list_id.append(i.text)
	for i in moviessubtree.getiterator('name'):
		self.similar_movie_list_title.append(i.text)
	for i in moviessubtree.getiterator('imdb_id'):
		self.similar_movie_imdb_id.append(i.text)
	
	print 'you might want to check:' 
	print self.similar_movie_list_title
	#print self.similar_movie_list_id
	#print self.similar_movie_imdb_id
	return 1
