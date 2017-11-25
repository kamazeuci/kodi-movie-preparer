# variable naming conventions:
# "year" corresponds to the year substring. 
# "name" corresponds to the movie name substring.
# "title" corresponds to the whole final directory name (name + year)
# "Brackets"
# "Parenthesis"

import os       # This module allows us to interact with files and directories. I use it to first list all directories and then to make the final renaming of directory names.
import re      # This is a module used to work with regular expressions. We need them to search for patterns in the directory name, in order to find the year substring.


lista = os.walk(".").next()[1]    # List all directories in actual path.

#initiate 5 different counters
counterPelis = 0  # All directories listed
counterYear = 0   # Directories with a detected Year substring (between 1900 and 2099)
counterYearBrackets = 0 # Directories with years originally within brackets
counterYearParenthesis = 0 # Directories with years originally already within parenthesis
counterChar = 0    # Directories originally with periods or underscores
counterNoYear = 0 # Directories with no year

print("------- Original Directories -------")
for peli in lista:
    counterPelis = counterPelis + 1     # First lets count every directory (movie)  on the list
print counterPelis                                  # Tell the user how many directories he has to work with

print("------- Character Replaced Directories ---------")
for peli in lista:
    if (peli.find(".") > 0) or (peli.find("_") > 0): #If script finds any movie with underscores or periods
        counterChar = counterChar + 1               # Add 1 to the counter
        TitleReplacedPeriods = peli.replace(".", " ")            #replace periods with whitespace
        TitleReplacedPeriodsAndDashes = TitleReplacedPeriods.replace("_", " ") # replace underscores with whitespace
        os.rename(peli, TitleReplacedPeriodsAndDashes)          #rename file
        print(peli + " ===> " + TitleReplacedPeriodsAndDashes)
    else:
        pass
     
#if counterChar == 0:            #If it finds no dashes or underscores
    #print("No directory  for character renaming has been found")
#else:                                      #If it finds any dashes or underscores
    #print("Character Renamed Directories =" +str(counterChar))     # print the number of folders with replaced characters.

lista = os.walk(".").next()[1]    # List all directories again, to update the list with the recently renamed directories.

print ("------------ Finding a Year ------------------------")
# go ahead and find movies that have a year

for peli in lista:                                  # for each entry in the list of directories
  
    
    if (re.search('.*(\[((19|20)\d{2})\]).*', peli)) > 0:   # see if you can find a year within brackets
        counterYearBrackets = counterYearBrackets + 1
        yearWithBrackets =  (re.search('(.*)(\[((19|20)\d{2})\]).*', peli))   #define a variable 
        nameBrackets = yearWithBrackets.group(1)       #that contains the substring
        nameBrackets = nameBrackets.strip()      #strip possible trailing or leading whitespace
        yearBrackets = yearWithBrackets.group(2)  
        
        yearBracketsReplaced = yearBrackets.replace("[","(")                    # replace opening bracket
        yearBracketsReplaced = yearBracketsReplaced.replace("]",")")    # replace closing bracket
        titleYearBracketsReplaced = (nameBrackets + " " + yearBracketsReplaced)
        print("Brackets Changed: " + peli + " ====> " + titleYearBracketsReplaced)
        os.rename(peli, titleYearBracketsReplaced)
        
       
        
    elif (re.search('.*\(((19|20)\d{2})\).*', peli)) > 0:    # see if you can find a year within parenthesis
        counterYearParenthesis = counterYearParenthesis + 1
        stringWithParenthesis = (re.search('(.*)\(((19|20)\d{2})\).*', peli))
        yearWithParenthesis = stringWithParenthesis.group(2)
        movieTitleParenthesis = stringWithParenthesis.group(1)
        movieTitleParenthesis = movieTitleParenthesis.strip()
        titleYearWithParenthesis = (movieTitleParenthesis + " (" + yearWithParenthesis + ")")
        print("Movies already with Parenthesis: " + peli + " ====> " + titleYearWithParenthesis)
        os.rename(peli, titleYearWithParenthesis)
        
    elif (re.search('(.*)((19|20)\d{2})(.*)', peli)) > 0:  #See if you can find a year substring
        print(peli)            #print the name of the movie you found a year substring on.
        yearNumber = (re.search('(.*)((19|20)\d{2})(.*)', peli))    # name the year substring as "yearnumber"
        movieTitle = yearNumber.group(1)
        movieTitle = movieTitle.strip()
        movieYear = yearNumber.group(2)
        movieYear = "(" + movieYear + ")"
        postShit = yearNumber.group(3)
        counterYear = counterYear + 1
        movieName = (movieTitle + " " + movieYear)  #count 1 more movie with year
    
        print("Parenthesis added: " + peli + " ====>" + movieName)
        os.rename(peli,  movieName)
        # print("Shit: " + postShit)
        #Find years between brackets and replace the brackets for parenthesis    
        # Find years already between parenthesis, don't change them but count them.
    else:
        
        print("Movie without year: " + peli)
        counterNoYear = counterNoYear + 1
        
   #if (YearNumber > 0):
        #CounterYear = CounterYear + 1
        #print peli
        #print YearNumber
print("Directories = "+ str(counterPelis))
print("Directories with characters replaced = " + str(counterChar))
print("Directories with valid year = " + str(counterYear))
print("Directories with Brackets replaced = " + str(counterYearBrackets))
print("Directories that already had parenthesis = " + str(counterYearParenthesis))
print("Directories with no valid year = " +str(counterNoYear))

            #YearName = peli.replace([19-20][0-9][0-9],"("[19-20][0-9][0-9]")")
            #print(YearName)
                  
## Put $YEAR inside parenthesis but only if there are no parenthesis already.

#if $YEAR = entre parentesis
	#$YEAROK = $YEAR
	
#if $YEAR = entre brackets
	#$YEAROK = $YEAR - brackets + parenthesis

#if $YEAR = entre espacios
	#then $YEAROK = $YEAR + parenthesis

#rename $YEAR to $YEAROK
## Strip everything after $YEAR



