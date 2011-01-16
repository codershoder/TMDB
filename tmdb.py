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
	
def main():
	"""Getting input and passing to other functions"""
	#title = raw_input('Enter the name of the movie-->  ')
	obj = movie.movie()
	obj.build_db('golmaal')
	choice = input('Enter the index number of the movie you would like to know more about-->  ')
	if choice <0 or choice > (len(obj.similar_movie_list_title))-1:
		print 'invalid choice'
	obj.get_info(choice)
	return 0

if __name__ == '__main__':
	main()


