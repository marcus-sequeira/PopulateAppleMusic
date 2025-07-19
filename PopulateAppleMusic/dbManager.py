import sqlite3
import xml.etree.ElementTree as ET
import os
from time import sleep
import getFromAPI

def updateRowBPM(persistent_id, bpm):
    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'main.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "UPDATE metadata SET bpm = ? WHERE persistent_id = ?"
    cursor.execute(query, (bpm, persistent_id))
    conn.commit()
    conn.close()



def parseLibraryXMLtoSQL():

    xml_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'library.xml')

    if not os.path.exists(xml_path):
        print(f"Error: XML file not found at {xml_path}")
        return


    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'main.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open('model/create_tables.sql', 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    tracks_dict = None
    for dict_item in root.iter('dict'):
        for key in dict_item.iter('key'):
            if key.text == 'Tracks':
                tracks_dict = next(dict_item.iter('dict'))
                break
        if tracks_dict is not None:
            break

    if tracks_dict is not None:
        for track in tracks_dict.iter('dict'):
            track_name = None
            album_name = None
            artist_name = None
            persistent_id_value = None

            for i, child in enumerate(track):
                if child.tag == 'key':
                    if child.text == 'Name':
                        track_name = track[i + 1].text
                    elif child.text == 'Album':
                        album_name = track[i + 1].text
                    elif child.text == 'Artist':
                        artist_name = track[i + 1].text
                    elif child.text == 'Persistent ID':  # Changed from 'Track ID' to 'Persistent ID'
                        persistent_id_value = track[i + 1].text

            if track_name and album_name and artist_name and persistent_id_value:
                cursor.execute('''
                INSERT OR IGNORE INTO library (Title, Album, Artist, persistent_id)
                VALUES (?, ?, ?, ?)
                ''', (track_name, album_name, artist_name, persistent_id_value))

        conn.commit()
        conn.close()



def getAllBPMfromDeezer():

    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'main.db')


    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT Title, Artist, persistent_id FROM Library"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        song, artist, persistent_id = row[0], row[1], row[2]
        bpm = getFromAPI.getBPMfromDeezerApi(artist, song)
        updateRowBPM(persistent_id, bpm)
        print(row, bpm)
        sleep(0.21)


    cursor.close()
    conn.close()







if __name__ == '__main__':
    print()

    parseLibraryXMLtoSQL()