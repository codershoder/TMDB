#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 sony <sony@ubuntu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import movie
import webbrowser

	
def main():
	"""Getting input and passing to other functions"""
	title = raw_input('Enter the name of the movie-->  ')
	obj = movie.movie()
	if obj.get_similar_movie_titles(title):
		print 'Got information, do you want to open the IMDB link?'
	else:
		print 'There was Error prcessing your request'
		exit(1)
	li = obj.get_imdb_list()
	imdb = 'http://www.imdb.com/title/' + li[0] + '/'
	webbrowser.open(imdb)
	return 0

if __name__ == '__main__':
	main()

