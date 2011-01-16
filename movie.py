import constants
import urllib2
from xml.etree import ElementTree as ET


class movie:
	
  def __init__(self):
	  self.similar_movie_list_title = []
	  self.similar_movie_list_id = []
	  self.similar_movie_imdb_id = []
	  self.similar_movie_type = []
	  self.similar_movie_url = []
	  self.similar_movie_rating = []
	  self.similar_movie_overview = []
	  self.similar_movie_release = []

  def string_if_not_null(self,x):
	  if x:
		  return x
	  else:
		  return 'Info not available'
			

  def get_info(self,index):
	  print '\nTitle: %s' %  self.string_if_not_null(self.similar_movie_list_title[index])
	  print '\nType: %s' %  self.string_if_not_null(self.similar_movie_type[index])
	  print '\nTMDB URL: %s' %  self.string_if_not_null(self.similar_movie_url[index])
	  print '\nRating: %s' %  self.string_if_not_null(self.similar_movie_rating[index])
	
  def display_all(self):
	  print self.similar_movie_list_title
	  print self.similar_movie_list_id
	  print self.similar_movie_imdb_id
	  print self.similar_movie_type
	  print self.similar_movie_url
	  print self.similar_movie_rating
	  print self.similar_movie_overview
	  print self.similar_movie_release
	  
	  

  def get_imdb_list(self):
	  return self.similar_movie_imdb_id

  def build_db(self,title):
	"""Returns a list of movies similar to one given by user"""
	#generating search query
	search = constants.SEARCH_MOVIE + constants.API_KEY + '/' + title
	xml = urllib2.urlopen(search).read()
	filehandler= open('a.xml','w')
	filehandler.write(xml)
	filehandler.close()
	#print xml
	#exit(0)
	
	
	tree= ET.parse('a.xml')
	doc = tree.getroot()
	
	moviessubtree = doc.find('movies')
	for i in moviessubtree.getiterator('type'):
		self.similar_movie_type.append(i.text)
	for i in moviessubtree.getiterator('url'):
		self.similar_movie_url.append(i.text)
	for i in moviessubtree.getiterator('rating'):
		self.similar_movie_rating.append(i.text)	
	for i in moviessubtree.getiterator('overview'):
		self.similar_movie_overview.append(i.text)	
	for i in moviessubtree.getiterator('release'):
		self.similar_movie_release.append(i.text)
	for i in moviessubtree.getiterator('id'):
		self.similar_movie_list_id.append(i.text)
	for i in moviessubtree.getiterator('name'):
		self.similar_movie_list_title.append(i.text)
	for i in moviessubtree.getiterator('imdb_id'):
		self.similar_movie_imdb_id.append(i.text)
	
	#print self.similar_movie_list_title
	#print self.similar_movie_release
	#print self.similar_movie_overview
	for i in range(len(self.similar_movie_list_title)):
		info_str = '[' + str(i) + ']\n' + self.similar_movie_list_title[(i)] + ':\n'
		#if i < len(self.similar_movie_release[(i)]) and self.similar_movie_release is not None:
		#	info_str += self.similar_movie_release[i]
		if i < len(self.similar_movie_overview[(i)]) and self.similar_movie_overview is not None:
			info_str += self.similar_movie_overview[i]
		print  info_str
	#self.display_all()
	#print self.similar_movie_list_id
	#print self.similar_movie_imdb_id
	return 1

