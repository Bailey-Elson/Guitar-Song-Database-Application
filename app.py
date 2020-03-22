from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQLDB')
mysql = MySQL(app)

#Everything to do with the Songs button on the navbar 

#code for main Songs page and home page
@app.route('/', methods = ['GET','POST'])
@app.route('/song', methods = ['GET','POST'])
def song():
    return render_template("song.html")

#yo
#code for view song button and page 
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

#code for add song button and page
@app.route('/song/addsong', methods = ['GET','POST'])
def addsong():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Chord_name, Chord_symbol FROM Chords;")
    mysql.connection.commit()
    chords = cur.fetchall()
    chords2=[""]
    for i in range(0,len(chords)):
        chords2.append(str(chords[i][0])+" "+str(chords[i][1]))
    if request.method == "POST":
        details=request.form 
        name=details['songName']
        artist=details['songArtist']
        genre=details['songGenre']
        chord1=details['chordName1']
        chord2=details['chordName2']
        chord3=details['chordName3']
        chord4=details['chordName4']
        chord5=details['chordName5']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Songs WHERE Song_name = %s AND Artist = %s AND Genre = %s;",(name, artist, genre))
        mysql.connection.commit()
        test = cur.fetchall()
        if name != "" and artist != "" and genre != "" and test == ():
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Songs(Song_name, Artist, Genre)VALUES(%s,%s,%s);",(name, artist, genre))
            mysql.connection.commit()
            cur.close()
        if chord1 != "":
            addingchord(chord1,name)
        if chord2 != "":
            addingchord(chord2,name)
        if chord3 != "":
            addingchord(chord3,name)
        if chord4 != "":
            addingchord(chord4,name)
        if chord5 != "":
            addingchord(chord5,name)
    return render_template("addsong.html", chords1 = chords2)

def addingchord(chord,name):
    chordSymbol = ""
    chord = chord.split()
    chordName = chord[0]
    if len(chord) == 2:
        chordSymbol = chord[1]
    cur = mysql.connection.cursor() 
    if chordSymbol == "":
        cur.execute("SELECT ChordID from Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",[chordName, chordSymbol])
        ChordID = str(cur.fetchall())
    else:
        cur.execute("SELECT ChordID from Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",[chordName, chordSymbol])
        ChordID = str(cur.fetchall())
    cur.execute("SELECT SongID from Songs WHERE Song_name = (%s);",[name])
    SongID = str(cur.fetchall())
    SongID = SongID[2:-4]
    ChordID = ChordID[2:-4]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Chords_Songs WHERE ChordID = %s AND SongID = %s;",(ChordID,SongID))
    mysql.connection.commit()
    test = cur.fetchall()
    if test == ():
        cur.execute("INSERT INTO Chords_Songs(ChordID,SongID)VALUES(%s,%s);",(ChordID,SongID))
        mysql.connection.commit()
        cur.close()

#code for delete song button and page 
@app.route('/song/deletesong', methods = ['GET','POST'])
def deletesong():    
    if request.method == "POST":
        details=request.form 
        name=details['songName']
        cur = mysql.connection.cursor()
        cur.execute("SELECT SongID FROM Songs WHERE Song_name = (%s);",[name])
        IDnum = str(cur.fetchall())
        IDnum = IDnum[2:-4]
        code = "DELETE FROM Chords_Songs WHERE SongID = "+str(IDnum)+";"
        cur.execute(code)
        cur.execute("DELETE FROM Songs WHERE Song_name = (%s);",[name])      
        mysql.connection.commit()
        cur.close()
    return render_template("deletesong.html")

#code for search song button and page 
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

#code for edit song button and page 
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
        if oldname != "" and oldartist != "" and oldgenre != "" and newname != "" and newartist != "" and newgenre != "": 
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Songs SET Song_name = (%s), Artist = (%s), Genre = (%s) WHERE Song_name = (%s) and Artist = (%s) and Genre = (%s);",(newname,newartist,newgenre,oldname,oldartist,oldgenre))
            mysql.connection.commit()
            cur.close()
    return render_template("editsong.html")

#EVERYTHING TO DO WITH CHORD

#code for the chord main page 
@app.route('/chord', methods = ['GET','POST'])
def chord():
    return render_template("chord.html")

#code for the view chord button and page 
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

#code for the add chord button and page 
@app.route('/chord/addchord', methods = ['GET','POST'])
def addchord():
    if request.method == "POST":
        details=request.form 
        name=details['chordName']
        symbol=details['chordSymbol']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Chords WHERE Chord_name = %s AND Chord_symbol = %s;",(name,symbol))
        mysql.connection.commit()
        test = cur.fetchall()
        cur.close()
        if name != "" and symbol != "" and test == ():
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Chords(Chord_name, Chord_symbol)VALUES(%s,%s)",(name, symbol))
            mysql.connection.commit()
            cur.close()
    return render_template("addchord.html")

#code for the delete button and page 
@app.route('/chord/deletechord', methods = ['GET','POST'])
def deletechord():
    if request.method == "POST":
        details=request.form 
        name=details['chordName']
        symbol=details['chordSymbol']
        cur = mysql.connection.cursor()
        cur.execute("SELECT ChordID FROM Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",(name, symbol))
        IDnum = str(cur.fetchall())
        IDnum = IDnum[2:-4]
        code = "DELETE FROM Chords_Songs WHERE ChordID = "+str(IDnum)+";"
        cur.execute(code)
        cur.execute("DELETE FROM Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",(name, symbol))
        mysql.connection.commit()
        cur.close()
    return render_template("deletechord.html")

#code for the search button and code
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
    name += " is in the following songs:"
    return render_template("searchchord2.html", info1 = info, name = name)

#code for the add chord to song button and page 
@app.route('/chord/addchordtosong', methods = ['GET','POST'])
def addchordtosong():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Chord_name, Chord_symbol FROM Chords;")
    mysql.connection.commit()
    chords = cur.fetchall()
    chords2=[""]
    for i in range(0,len(chords)):
        chords2.append(str(chords[i][0])+" "+str(chords[i][1]))
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT Song_name FROM Songs;")
    mysql.connection.commit()
    songs = cur.fetchall()
    songs2=[""]
    for i in range(0,len(songs)):
        songs2.append(str(songs[i]))
    songs = []
    for i in range(0,len(songs2)):
        song = str(songs2[i])
        song = song[2:-3]
        songs.append(song)
    cur.close()
    if request.method == "POST":
        details=request.form 
        chord=details['chordName']
        song=details['songName']
        chordSymbol = ""
        if song != "" and chord != "":  
            chord = chord.split()
            chordName = chord[0]
            if len(chord) == 2:
                chordSymbol = chord[1]
            cur = mysql.connection.cursor() 
            if chordSymbol == "":
                cur.execute("SELECT ChordID from Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",[chordName, chordSymbol])
                ChordID = str(cur.fetchall())
                please = ChordID
            else:
                cur.execute("SELECT ChordID from Chords WHERE Chord_name = (%s) AND Chord_symbol = (%s);",[chordName, chordSymbol])
                ChordID = str(cur.fetchall())
                please = ChordID
            cur.execute("SELECT SongID from Songs WHERE Song_name = (%s);",[song])
            SongID = str(cur.fetchall())
            work = SongID
            SongID = SongID[2:-4]
            ChordID = ChordID[2:-4]
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM Chords_Songs WHERE ChordID = %s AND SongID = %s;",(ChordID,SongID))
            mysql.connection.commit()
            test = cur.fetchall()
            if test == ():
                cur.execute("INSERT INTO Chords_Songs(ChordID,SongID)VALUES(%s,%s);",(ChordID,SongID))
                mysql.connection.commit()
                cur.close()
    return render_template("addchordtosong.html", chords1 = chords2, songs1 = songs)

if __name__ == "__main__":
    app.run('0.0.0.0', debug = True)
