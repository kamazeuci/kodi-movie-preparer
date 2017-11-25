# kodi-movie-preparer
A python script to rename movie collection directories and leave them tidy in order for KODI to scan them

This is a (supposedly) simply script. Its purpose is to achieve clean movie folder naming, like:
*Movie Name (Year)*.
i.e:
* The Elephants Dream (2006)
* Tetris (2010)

Why this format? Because it is what KODI recommends:
http://kodi.wiki/view/Naming_video_files/Movies#Naming_conventions

I got overwhelmed by more complex options like [FileBot](http://www.filebot.net), [MediaElch](http://www.kvibes.de/mediaelch) and [tinyMediaManager](http://www.tinymediamanager.org).  

Please notice that this script renames ONLY directories, and not any files. So, it has to be run from the root directory where you store your movie collection, and assumes that each directory is a movie.

This script DOES NOT add a year to a directory that does not already have a year. For that, you could try [FileBot](http://www.filebot.net), [MediaElch](http://www.kvibes.de/mediaelch) or [tinyMediaManager](http://www.tinymediamanager.org).  at 

## What This Script Does (and in what situations it works)
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
    
 And that's it. Pretty simple, no? But as it turns out it solves most the mess in movie folders.

