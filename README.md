PopulateAppleMusic

PopulateAppleMusic is a project designed to enrich your Apple Music library with detailed metadata such as subgenres and instruments, enabling smarter Smart Playlists and deeper musical insights.

🚀 How to Use
	1.	Export your Apple Music library to a file named library.xml.
	2.	Place this file inside the data/ folder of the project.
	3.	Run main.py.
	4.	Once the script finishes, all track metadata will be updated in the Apple Music desktop app, ready for creating Smart Playlists and viewing subgenres and instruments for each track.

📁 Project Structure

File	Description
getFromAPI.py	Handles API requests. Retrieves data from MusicBrainz and, in the future, BPM data from Deezer.
apiToDb.py	Contains the PopulateDatabase class, which populates the SQLite database using parsed data from the library.
appleScripting.py	Communicates with Apple Music on macOS to update the “Description” field (instruments) and “Comments” field (subgenres).
create_tables.sql	SQL script that defines the schema for the SQLite database.
dbManager.py	Parses the library.xml file and inserts the data into the database.
main.py	The main script that controls the flow of the application.
prepareDataToImport.py	Splits subgenres and instruments by commas and updates the corresponding entries in the database.

🎯 Goal

To automatically import subgenres and instruments for each track into Apple Music, enabling rich metadata filtering and improved playlist creation.
