import datetime
import itertools
import sys, os
import re
import urllib.parse

os.system('wget http://heromaza.in/categorylist/986/new_release_bollywood_movie_mp3_songs/default/1.html -O site_source.txt')

tfile = open('site_source.txt', 'r')
temp = tfile.read()
tfile.close()
os.system('rm site_source.txt')

tlist = re.findall('<a href="/filelist/(.*)/new2old/1.html"><div>(.*)\t\t\t', temp, re.M)
id_movie = dict(tlist)
#print ('Movies List: ',id_movie.values())
#print ('Movies ID list: ',id_movie.keys())	

for ids in id_movie.keys():
	
	urls = urllib.parse.quote('heromaza.in/filelist/'+ids+'/new2old/1.html')	
	os.system('wget '+urls+' -O "'+id_movie[ids]+'.txt"')
	#print('\n\nwget '+urls+' -O "'+id_movie[ids]+'.txt"')	
	
	sfile = open(id_movie[ids]+'.txt', 'r')
	stemp = sfile.read()
	sfile.close()
	os.system('rm "'+id_movie[ids]+'.txt"')
	
	slist = re.findall('<a class="fileName" href="/fileDownload/(.*).html">(.*)</a><br/>', stemp, re.M)
	if slist:
		#os.system('nautilus /home/minion/Music')
		os.system('mkdir "/home/minion/Music/'+id_movie[ids]+'"')
		song_det = dict(slist)
	
		#print ('\nSong Name: ',song_det.values())
		#print ('\nSong ID: ',song_det.keys())
		
		for s_id in song_det.keys():
			temp_key = s_id
			s_id = s_id.split('/')[0]
			#print (s_id)
			if os.path.isfile('/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key]) == False:
				print (os.path.isfile('/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key]))
				print ("Downloading "+song_det[temp_key])
				os.system('wget http://heromaza.in/files/download/id/'+s_id+' -A mp3 -O "/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key]+'"')
				print ('/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key])
				
			elif os.path.isfile('/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key]) == True:
				#print (os.path.isfile('/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key]))
				print ('/home/minion/Music/'+id_movie[ids]+'/'+song_det[temp_key])		
				#print ('wget http://heromaza.in/files/download/id/'+s_id+' -O /"'+id_movie[ids]+'"/"'+song_det[temp_key]+'"')
				print ("File Already Exists")
				
		

