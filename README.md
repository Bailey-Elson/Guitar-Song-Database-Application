# Qa SFIA Project 1

 ## Contents 

 1. Brief 
    * My Soloution 
2. Entity Relationship Diagrams 
3. Risk Assessment 
4. Trello Board 
    * Sprints

---

## Brief 
Objective:
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

Requiremenst:
* Trello Board
* Relational database used to store data persistently for the project, this database needs to have at least 2 tables in it
* ERD diagram modeling the relationship
* Risk Assessment
* Clear Documentation from a design phase describing the architecture you will use for you project
* functional CRUD application created in Python
* Fully designed test suites
* A functioning front-end website and integrated API’s, using Flask.
* Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine

---
## Entity Relationship Diagrams

![A picture of my ERD diagram](https://i.imgur.com/j2NkMcB.png)

The above ERD shows my database structure. I will be using three tables(Songs, Chords and Chords_Songs), With a many to many relationship between the Songs table and Chords_Songs table and also between the Chords table and the Chords_Songs table. The Chords_Songs table is a joining table between the other two tables using both their primary keys as foriegn keys.

---




