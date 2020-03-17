import pytest
import urllib3

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