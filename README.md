# README.md
# 
# Install the package using python3 -m pip install XXX-?.?.tar.gz
# Test the install with python3 test.py Fred Smith
#
# Dependencies
# Python >  3.6
# pandas >= 1.1.5
# pip    >= 21.3.1
#
# TODO
# The databases of artist songs and song lyrics are 
#   currently just simple csv files
# I created them as functions so that if the method of
#   collection were changed only these functions will
#   need amending.
#
# NOTES
# To create dist
# $ cd SongsEtc
# $ rm -rf dist
# -> edit setup.py
# $ python3 -m build # create dist
#
# To install dist
# $ python3 -m pip install dist/ArtistSongsLyrics-0.2.tar.gz
#
# To test install
# $ python3 test.py Fred Smith
# or
# $ python3 /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/ArtistSongsLyrics/SongsEtc.py Fred Smith
#
