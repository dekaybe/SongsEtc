#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#
# Initialise a debug variable D. Debug mode D is not 0.
D=0
#
#####################################################
#
# File:     SongsEtc.py
# Version:  0.2
# Author:   Dave K Brown 
#
####################################################################################################
# Revision History
####################################################################################################
#
# Dave K Brown 03-Nov-2021   Created
# Dave K Brown 03-Nov-2021   Removed import of numpy
#
#####################################################
#
import sys
import pandas as pd
#
#####################################################
## F U N C T I O N S
#####################################################
# function to return a list of songs by said artist
def Songs( ArtistName ):  
	Songs=[]
	# Read the database of artist names and songs
	df_ArtistAndSongs = pd.read_csv('./ArtistAndSongs.csv', "\t")
	for t in df_ArtistAndSongs.iterrows():
		if D!=0: print("line 16")
		if t[1][0] == ArtistName:
			F = 1 # At least one occurance/song of the artist name has been found
			ASong=t[1][1]
			if D!=0: print("A Song=",ASong)
			Songs.append(ASong)
	return Songs

def Lyrics ( SongName ):
	Lyrics=[]
	# Read the database of artist names and songs
	df_SongsAndLyrics = pd.read_csv('./SongsAndLyrics.csv',"\t")
	for l in df_SongsAndLyrics.iterrows():
		if D!=0: print("line 45")
		if l[1][0] == SongName :
			L=l[1][1] 
			if D != 0: print(L)	
			Lyrics.append(L)

	return L

#####################################################
## E N D   O F   F U N C T I O N S
#####################################################
#
def RunTheGuts( *ArtistNames ):
	#
	# Create a single string of the user input whilst capitalising 
	#   each element as we go.
	# TODO Perhaps capitalise everything before comparisons
	#  ArtistName=" ".join(ArtistNames).title()
	
	if D!=0: print("Artist Names =\"" + str(ArtistNames[0]) + "\"")
	if D!=0: print(type(ArtistNames))

	ArtistName = " ".join(ArtistNames[0])
	if D!=0: print("Artist Name =\"" + ArtistName + "\"")

	# Pull a list of the songs from a function
	S=Songs(ArtistName)

	NumberSongsFound=len(S)
	if D!=0: print("Number of songs found = " + str(NumberSongsFound))

	if NumberSongsFound == 0:
		print("No songs found for Artist : " + ArtistName)
		exit()
	else:
		# Initialise a list for song word counts
		H=[]

		# for each song found count words and add count to a list
		for s in S:
			if D!=0: print("s=" + s)

        		# Pull the lyrics for a song
			L=Lyrics(s)

			# Count the words in the returned lyrics
			WordList = L.split()
			NumberWords = len(WordList)
			if D!=0: print(NumberWords)
	
			# Add number of words to a list
			H.append(NumberWords)

		NumberOfSongs=len(H)
		SumOfWords=sum(H)
		MeanWords=SumOfWords/NumberOfSongs
		print("Average words per song for artist, " + ArtistName + ", is " + str(round(MeanWords, 2)))

if __name__ == "__main__":
	# Grab all the user input
	ArtistNames=sys.argv[1:]

	RunTheGuts( ArtistNames )

# ends . . . 
