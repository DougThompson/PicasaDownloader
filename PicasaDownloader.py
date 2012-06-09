#!/usr/bin/env python
'''
Copyright (c) 2011-2012 Doug Thompson

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"),to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os
import re
import urllib
import feedparser

class PicasaDownloader:
    
    def splitPicasaWebURL(self, url):
        '''
        Split a Picasa URL and extract the username, gallery name, and AuthKey
        Return the results as a tuple
        '''
        # Use a RegEx query to match the relevant parts of a Picasa URL
        regex = re.compile(r'(http:|https:)//picasaweb\.google\.com/((?P<username>\w(\w|\.)+)(/(?P<album>\w(\w|\.)+))?)(\?.*(?P<authkey>authkey\=\w+))?')
        result = regex.search(url).groupdict()
        
        # Parse the results into a tuple to be returned
        userName = result['username']
        gallery = result['album']
        authkey = result['authkey']

        return userName, gallery, authkey
    
    def getAllAlbums(self, userName):
        '''
        Get all publicly viewable galleries for a Google username, add them to a list,
        and finally return the list
        '''
        albums = []
        feeds = ['http://picasaweb.google.com/data/feed/api/user/' + userName]
        for url in feeds:
            feed = feedparser.parse(url)
            for albumEntry in feed.entries:
                albums.append(albumEntry.gphoto_name)
    
        return albums
    
    #def getGPhotoAlbumName(self, userName, authkey, albumName):
    #    url = 'http://picasaweb.google.com/data/feed/api/user/' + userName
    #    feed = feedparser.parse(url)
    #    for albumEntry in feed.entries:
    #        if albumEntry.gphoto_name == albumName or albumEntry.title_detail.value == albumName:
    #            return albumEntry.gphoto_name
    #
    #    return True
    
    def getAllImages(self, userName, authkey, albumName, destFolder, statusBar):
        '''
        Downloads *all* images from a Gallery
        '''
        # Build the URL to feed to the Picasa API and add the AuthKey (if necessary)
        albumUrl = 'http://picasaweb.google.com/data/feed/api/user/{0}/album/{1}?kind=photo&imgdl=1'.format(userName, albumName)
        if authkey:
            albumUrl += '&' + authkey
        
        # Load the results into feedparser, download the image, and update the referenced
        # status bar with the current image name.
        feed = feedparser.parse(albumUrl)
        for imgEntry in feed.entries:
            statusBar.SetStatusText(imgEntry.content[0].src)
            self.downloadFile(imgEntry.content[0].src, destFolder)
            
        statusBar.SetStatusText('Done.')
    
        return True
    
    def getAllImages2(self, destFolder, imageList, statusBar):
        '''
        Downloads *only* the listed images from a Gallery
        '''
        for imgEntry in imageList:
            # Replace the thumbnail '/s288/' tag with the full-size image tag '/d/'
            imgEntry = imgEntry.replace('/s288/', '/d/')
            statusBar.SetStatusText(imgEntry)
            self.downloadFile(imgEntry, destFolder)
            
        statusBar.SetStatusText('Done.')
    
        return True

    def listAllImages(self, userName, authkey, albumName):
        '''
        Lists *all* images for a Gallery
        '''
        # Build the URL to feed to the Picasa API and add the AuthKey (if necessary)
        albumUrl = 'http://picasaweb.google.com/data/feed/api/user/{0}/album/{1}?kind=photo&imgdl=1'.format(userName, albumName)
        if authkey:
            albumUrl += '&' + authkey
            
        # Load the results into feedparser and append the image name to a list
        images = []
        feed = feedparser.parse(albumUrl)
        for imgEntry in feed.entries:
            images.append(imgEntry.content[0].src.replace('/d/', '/s288/'))
            
        return images
    
    def downloadFile(self, imgUrl, destFolder):
        '''
        Download a single image and save it to the Destination Folder
        '''
        # Get the filename to add to the Destination Folder
        fileName = imgUrl[ imgUrl.rindex('/') + 1:]
        # Open the image from the URL
        imageFromUrl = urllib.urlopen(imgUrl)
        # Create the destination filename
        imageFile = file(os.path.join(destFolder, fileName), 'wb')
        
        # Start downloading the image, buffer by 64K, and write out buffered chunks
        while True:
            buf = imageFromUrl.read(65536)
            if len(buf) == 0:
                break
            imageFile.write(buf)
        
        # Close both the filesystem object and URL object
        imageFile.close()
        imageFromUrl.close()
    
        return True
