import os
import dbManager
import apiToDb
import appleScripting

## IMPORTANT!
## PLACE THE XML FILE IN THE DATA FOLDER BEFORE RUNNING THE SCRIPT
## THE XML FILE MUST BE NAMED 'library.xml'


## STEP 1 - PARSE XML TO SQL
dbManager.parseLibraryXMLtoSQL()
print("STEP 1 - PARSE XML TO SQL DONE")
##

project_directory = '/Users/marcus/Desktop/Populate_AppleMusicV2'
os.chdir(project_directory)
db_config = os.path.join('data', 'main.db')
pd = apiToDb.PopulateDatabase(db_config)

##

## STEP 2 - POPULATE PART 1
pd.populatePart1()
print("STEP 2 - POPULATE PART 1 DONE")

## STEP 3 - POPULATE GENRES
pd.populateGenres()
print("STEP 3 - POPULATE GENRES DONE")

## STEP 4 - CHECK EXCLUDED TRACKS
pd.checkExcludedTracks()
print("STEP 4 - CHECK EXCLUDED TRACKS DONE")


## STEP 5 - EXPORT DATA TO APPLE MUSIC
appleScripting.exportDataToAppleMusic(db_config)
print("STEP 5 - EXPORT DATA TO APPLE MUSIC DONE")

print("ALL STEPS DONE")