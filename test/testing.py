import pytest
import urllib3
from flask import Flask
import os
from flask_mysqldb import MySQL
def test_homePage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/')
    assert 200 == r.status
def test_songPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/song')
    assert 200 == r.status
def test_viewSongPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/song/viewsong')
    assert 200 == r.status
def test_addSongPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/song/addsong')
    assert 200 == r.status
def test_deleteSongPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/song/deletesong')
    assert 200 == r.status
def test_searchSongPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/song/searchsong')
    assert 200 == r.status
def test_editSongPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/song/editsong')
    assert 200 == r.status
def test_chordPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/chord')
    assert 200 == r.status
def test_viewChordPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/chord/viewchord')
    assert 200 == r.status
def test_addChordPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/chord/addchord')
    assert 200 == r.status
def test_deleteChordPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/chord/deletechord')
    assert 200 == r.status
def test_searchChordPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/chord/searchchord')
    assert 200 == r.status
def test_addChordToSongPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/chord/addchordtosong')
    assert 200 == r.status
app=Flask(__name__)
app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']
mysql = MySQL(app)
def test_readSongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRecords = cur.execute("SELECT * FROM Songs;")
        mysql.connection.commit()
        cur.close()
        assert 19 == numRecords
def test_readChordsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRecords = cur.execute("SELECT * FROM Chords;")
        mysql.connection.commit()
        cur.close()
        assert 8 == numRecords
def test_readChords_SongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRecords = cur.execute("SELECT * FROM Chords_Songs;")
        mysql.connection.commit()
        cur.close()
        assert 51 == numRecords
def test_createSongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Songs(SongID, Song_name, Artist, Genre)VALUES(200, 'Yummy','Justin Bieber','Pop');")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Songs;")
        mysql.connection.commit()
        cur.close()
        assert 20 == numRecords
def test_createChordsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Chords(ChordID, Chord_name, Chord_symbol)VALUES(200, 'D','Major');")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Chords;")
        mysql.connection.commit()
        cur.close()
        assert 9 == numRecords
def test_createChords_SongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Chords_Songs(ID, SongID, ChordID)VALUES(200, 200, 200);")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Chords_Songs;")
        mysql.connection.commit()
        cur.close()
        assert 52 == numRecords   
def test_updateSongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Songs SET Song_name = 'The Monster', Artist = 'Eminem', Genre = 'Rap' WHERE SongID = '200';")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Songs;")
        mysql.connection.commit()
        cur.close()
        assert 20 == numRecords
def test_updateChordsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Chords SET Chord_Name = 'F', Chord_symbol = 'Minor' WHERE ChordID = '200';")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Chords;")
        mysql.connection.commit()
        cur.close()
        assert 9 == numRecords
def test_deleteChords_SongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Chords_Songs WHERE ID = '200';")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Chords_Songs;")
        mysql.connection.commit()
        cur.close()
        assert 51 == numRecords
def test_deleteSongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Songs WHERE SongID = '200';")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Songs;")
        mysql.connection.commit()
        cur.close()
        assert 19 == numRecords        
def test_deleteChordsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Chords WHERE ChordID = '200';")
        mysql.connection.commit()
        numRecords = cur.execute("SELECT * FROM Chords;")
        mysql.connection.commit()
        cur.close()
        assert 8 == numRecords