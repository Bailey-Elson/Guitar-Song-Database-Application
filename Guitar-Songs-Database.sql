BEGIN;
​
DROP TABLE IF EXISTS Songs;
​
CREATE TABLE Songs (
    SongID INT(5) NOT NULL AUTO_INCREMENT,
    Song_name VARCHAR(50) NOT NULL,
    Artist VARCHAR(50) NOT NULL,
    Genre VARCHAR(50) NOT NULL,
    PRIMARY KEY(SongID)
);

DROP TABLE IF EXISTS Chords;
​
CREATE TABLE Chords (
    ChordID INT(5) NOT NULL AUTO_INCREMENT,
    Chord_Name VARCHAR(50) NOT NULL,
    Chord_Symbol VARCHAR(10) NOT NULL,
    PRIMARY KEY(ChordID)
);

DROP TABLE IF EXISTS Chords_Songs;
​
CREATE TABLE Chords_Songs (
    ID INT(5) NOT NULL AUTO_INCREMENT,
    SongID INT(5) NOT NULL,
    ChordID INT(5) NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY(SongID) REFERENCES Songs(SongID),
    FOREIGN KEY(ChordID) REFERENCES Chords(ChordID)
);
​
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Pop boy','Stormzy','Grime');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Nike','Frank Ocean','RnB');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Bruce Wayne','Bugzy Malone','Rap');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Lose Yourself','Eminem','Rap');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Game Over','Dave','Grime');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Seven Rings','Ariana Grande','Pop');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('3 Strikes','Kastaway','RnB');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Darkness','Eminem','Rap');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Own It','Stormzy','Grime');
INSERT INTO Songs(Song_name, Artist, Genre)VALUES('Yellow Submarine','The Beatles','Pop Rock');

INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('A'.'');
INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('B'.'');
INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('C'.'');
INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('D'.'');
INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('A'.'Minor');
INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('C'.'Major');
INSERT INTO Chords(Chord_Name, Chord_Symbol)VALUES('E'.'#');


COMMIT;
