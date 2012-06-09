# Picasa Downloader #

**Picasa Downloader** is a Python GUI application (using wxPython) designed to download one or more photos (at the original upload size) from a public or private Picasa album.  All you need is the link to the either the username (for public albums) or the access-controlled link to a specific, private album.  Select which images to download and download away!

## Development Requirements ##
Cross-development using [Aptana Studio 3](http://www.aptana.com/) started on 32-bit Python 2.6.1 on both Mac OS X 10.6.6 and Windows 7 64-bit using wxPython 2.8.9 32-bit.

Current requirements:

- [Python](http://www.python.org/download/) v2.7.3
- [wxPython](http://wxpython.org/) v2.8.12.1 32-bit
- [wxFormBuilder](http://wxformbuilder.org/) v3.1.70
- [feedparser](http://code.google.com/p/feedparser/) v5.1.2 (included)
- [VoidSpace ConfigObj](http://www.voidspace.org.uk/python/configobj.html) v4 (included)

This has not been test on a Linux distribution.

## How to Use ##
It's a pretty simple, straight-forward application, but here are a few tips to help make things clear (hopefully).

### Preferences ###
The **Preferences Dialog** allows you to store a default Picasa Web Username or Gallery and a default destination folder for any downloaded files.

### Galleries: Public or Private ###
You can download images from either public or private galleries.

To download from public galleries, only the root Picasa Web URL is required (for example, http://picasaweb.google.com/username).   Clicking the *Get Gallery List* button will return only the publicly viewable galleries for that username.

To download from a private gallery, the full link is required and can be obtained from that gallery in Picasa or from a link provided by that gallery owner &mdash; the *AuthKey* is necessary.  Only one Gallery should be found, but all images from that gallery can be downloaded.

### Downloading ###
You have the option to append the Gallery Name to the destination folder to help with avoiding image name conflicts.

## Future Plans, Roadmap ##
None at this time &mdash; other than hoping to learn from better Python programmers than myself.