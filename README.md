# Qa SFIA Project 1

 ## Contents 

1. Brief 
    * Objective
    * Requirements
2. Project Plan
    * Trello Board
    * Sprints
3. Risk Assessment 
4. Architecture 
    * Entity Relationship Diagram
    * Application Flow Chart
5. Testing 
6. Deployment

---

## Brief 
#### Objective:
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

#### Requiremenst:
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
## Project Plan 
#### Trello Board
#### Sprints 
---
## Risk Assesment 
---
## Architecture 
#### Entity Relationship Diagrams

![A picture of my ERD diagram](https://i.imgur.com/j2NkMcB.png)

The above ERD shows my database structure. I will be using three tables(Songs, Chords and Chords_Songs), With a many to many relationship between the Songs table and Chords_Songs table and also between the Chords table and the Chords_Songs table. The Chords_Songs table is a joining table between the other two tables using both their primary keys as foriegn keys.

#### Application Flow Chart

![A picture of my flow chart](https://i.imgur.com/HlC0Ea0.png)

The above flow chart shows the basic application structure plan at the beginning of the project. Each dotted box represents a differnt page on the application. All the pages excluding the main song page and main chord page will access the databse to crreate, read, update or delete data. 
---
## Testing
---
## Deployment 

![A picture of my flow chart](https://i.imgur.com/GNTpLvj.png)

Technologies used:
* Github: hosting for software development version control
* Python: high-level, general-purpose programming language
* Pytest: testing framework
* Flask: micro web framework 
* Jinja: web template engine
* HTML:  markup language for web browsers
* CSS: style sheet language
* Jenkins: open source automation server
* Google Cloud Platform: cloud computing services
* MYSQL: open-source relational database management system
