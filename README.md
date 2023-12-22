# kodi-movie-preparer
### What this script is
A [python](http://www.python.org) script to rename movie collection directories and leave them tidy in order for [KODI](http://www.kodi.tv) to scan them. You don't really need to use KODI. If you want to just standarize the names of your directories, this script could work for you.
Why KODI? I formerly used [Medianizer](http://www.medianizer.com), the Best movie organizer I found for Windows. When I evolved into GNU/Linux, I tried to run Medianizer through [Wine](http://www.winehq.org) (windows emulator), but I had some displaying problems. Then I found KODI and I sensed it was the solution I was looking for since a long time ago. And, of course, Libre Software.


### Example
This is a (supposedly) simply script. Its purpose is to achieve clean movie folder naming, like:
*Movie Name (Year)*.
i.e:
* The Elephants Dream (2006)
* Tetris (2010)
### Why this?
Why this format? Because it is what KODI recommends:
http://kodi.wiki/view/Naming_video_files/Movies#Naming_conventions

I got overwhelmed by more complex options like [FileBot](http://www.filebot.net), [MediaElch](http://www.kvibes.de/mediaelch) and [tinyMediaManager](http://www.tinymediamanager.org).  


### What This Script Does (and in what situations it works)
It does the following:
* Convert underscores("_"), and periods(".") into whitespace. i.e.
    * The.Elephants.Dream(2006) ===> The Elephants Dream (2006)    
    * The_Elephants_Dream(2006) ===> The Elephants Dream (2006)
    (btw, notice it also adds a whitespace between the title and the year)
    
* Put Years into parenthesis
    * The.Elephants.Dream.2006 ===> The Elephants Dream (2006)
    * The Elephants Dream 2006 ===> The Elephants Dream (2006)

* Strips any text after the year
    * The Elephants Dream (2006) [Johhny.Bravo.HD.1080] ===> The Elephants Dream (2006)
    * Tetris_2010_by_super_duper_and_his_4_boys ===> Tetris (2010)
    
 And that's it. Pretty simple, no? But as it turns out it solves most the mess in movie folders. Anyway, the script is exhaustively commented so with a minimum coding knowledge you should be able to make it fit your specific need. If so, Please DO share here!
 
 ### What this script does not do
 
 Please notice that this script renames ONLY directories, and not any files. So, it has to be run from the root directory where you store your movie collection, and assumes that each directory is a movie.

This script DOES NOT add a year to a directory that does not already have a year. For that, you could try [FileBot](http://www.filebot.net), [MediaElch](http://www.kvibes.de/mediaelch) or [tinyMediaManager](http://www.tinymediamanager.org).

### How to use it
 You can download the `kodi-movie-preparer.py` python file (notice the .py extension) from this website. To run it, you'll need Python installed on your system. You can install it on any platform you can imagine. Most Linux distributions carry it pre-installed Just google something like "Install Python on (*"type the name of your operating system here"*).
 Once you have python installed, just run `python2 kodi-movie-preparer.py`
 I think you need python2 because in Python 3 `print` is a function and in Python 2 `print` is a statement.

### Notes about the coding
 I am pretty sure this script has ugly messy and stupid coding. This is my first script so I am happy anyway, but I would love if any good-willing being would pour its code wisdom with the purpose of making this script better. I tried to comment everything to make it easy to read. Thanks in advance.
