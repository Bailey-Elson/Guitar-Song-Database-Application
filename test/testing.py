import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_mysqldb import MySQL

def test_songPage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.68.124.32:5000/')
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

# app=Flask(__name__)

# app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
# app.config['MYSQL_USER']=os.environ['MYSQLUSER']
# app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
# app.config['MYSQL_DB']=os.environ['MYSQLDB']

# mysql = MySQL(app)

# def test_select():
#     with app.app_context():
#         cur = mysql.connection.cursor()
#         numRecords = cur.execte("SELECT * FROM Songs;")
#         mysql.connection.commit()
#         cur.close()
#         assert 19 == numRecords