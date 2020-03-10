from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQLDB')
mysql = MySQL(app)



# EVERYTHING TO DO WITH SONG TABLE

@app.route('/', methods = ['GET','POST'])
@app.route('/song', methods = ['GET','POST'])
def song():
    return render_template("song.html")

@app.route('/song/viewsong')
def viewsong():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Songs;")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)   
    return render_template("viewsong.html", info1 = info)

@app.route('/song/addsong', methods = ['GET','POST'])
def addsong():
    if request.method == "POST":
        details=request.form 
        name=details['songName']
        artist=details['songArtist']
        genre=details['songGenre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Songs(Song_name, Artist, Genre)VALUES(%s,%s,%s)",(name, artist, genre))
        mysql.connection.commit()
    return render_template("addsong.html")

@app.route('/song/deletesong', methods = ['GET','POST'])
def deletesong():    
    if request.method == "POST":
        details=request.form 
        name=details['songName']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Songs WHERE Song_name = (%s);",[name])
        mysql.connection.commit()
        cur.close()
    return render_template("deletesong.html")



@app.route('/song/editsong', methods = ['GET','POST'])
def editsong():
    if request.method == "POST":
        details=request.form
        oldname=details['oldSongName']
        oldartist=details['oldSongArtist']
        oldgenre=details['oldSongGenre']
        newname=details['newSongName']
        newartist=details['newSongArtist']
        newgenre=details['newSongGenre']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Songs SET Song_name = (%s), Artist = (%s), Genre = (%s) WHERE Song_name = (%s) and Artist = (%s) and Genre = (%s);",(newname,newartist,newgenre,oldname,oldartist,oldgenre))
        mysql.connection.commit()
        cur.close()

    return render_template("editsong.html")










@app.route('/song/searchsong', methods = ['GET','POST'])
def searchsong():
    name = ""
    return render_template("searchsong2.html", name = name)

@app.route('/song/searchsong/2', methods = ['GET','POST'])
def searchsong2():
    details=request.form 
    name=details['songName']
    cur = mysql.connection.cursor()
    cur.execute("SELECT Chord_name, Chord_symbol from Chords JOIN Chords_Songs j ON Chords.ChordID = j.ChordID JOIN Songs s ON s.SongID = j.SongID WHERE s.Song_name = (%s);",[name])
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)  
    name += " contaions the following chords: "

    return render_template("searchsong2.html", info1 = info, name = name)





















#EVERYTHING TO DO WITH CHORD
@app.route('/chord', methods = ['GET','POST'])
def chord():
    return render_template("chord.html")

@app.route('/chord/viewchord', methods = ['GET', 'POST'])
def viewchord():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Chords;")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)

    return render_template("viewchord.html", info1=info)

@app.route('/chord/addchord', methods = ['GET','POST'])
def addchord():
    if request.method == "POST":
        details=request.form 
        name=details['chordName']
        symbol=details['chordSymbol']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Chords(Chord_name, Chord_symbol)VALUES(%s,%s)",(name, symbol))
        mysql.connection.commit()
    
    return render_template("addchord.html")

@app.route('/chord/deletechord', )
def deletechord():
    if request.method == "POST":
        details=request.form 
        name=details['chordName']
        symbol=details['chordSymbol']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",(name, symbol))
        mysql.connection.commit()
        cur.close()

    return render_template("deletechord.html")

@app.route('/chord/searchchord', methods = ['GET','POST'])
def searchchord():
    name = ""
    return render_template("searchchord2.html", name = name)

@app.route('/chord/searchchord/2', methods = ['GET','POST'])
def searchchord2():
    details=request.form 
    name=details['chordName']
    symbol=details['chordSymbol']
    cur = mysql.connection.cursor()
    cur.execute("SELECT Song_name From Songs JOIN Chords_Songs j ON Songs.SongID = j.SongID JOIN Chords c ON c.ChordID=j.ChordID WHERE c.Chord_name = (%s) AND c.Chord_symbol = (%s);",[name, symbol])
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)  
    name += symbol 
    name += " is in the following songs"

    return render_template("searchchord2.html", info1 = info, name = name)



if __name__ == "__main__":
    app.run('0.0.0.0', debug = True)
