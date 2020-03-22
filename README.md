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

|Risk No. | Risk | Effect | Cause | Likelihood | Impact | Soloution |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Overreaching on the project | Overreaching on the project will lead to the project becoming to complicated . This in turn will mean that I might not be able to turn in a finished product and I might lose motivation for the project. | Overestimation of my abilities. | Low | High | Keep the project simple while still meeting all then targets and if I have extra time at the end of the project I can thennslowly add extra fetures once the core project is done. |
| 2 | Project not meeting the specifications | Not meeting the specifications will lead to a project that isn't complete and will then mean a bad mark for the SFIA project. | Not understanding the specification. | Low | Medium | Talk to others doing the project and also those who set the specification to make sure my project meets the specification. |
| 3 | Organising the tasks ineffectively  | Non efficient organisation of the tasks will lead to tasks taking longer the nesacery and  could impact the overall time needed for the task and posibly cause me not to make the deadline. | Planning to do tasks before I'm capable, planning to do tasks before there respective prerecrative tasks aren't complete | Low | Medium | Plan when im doing specific tasks to coinside with when I have completed the training and also setting tasks to be complted in the correct order so any prerecrisite tasks are complete first. |
| 4 | Change of project specification | A change of project specification will lead to me having to possibly revise my project idea and structure if it doesn't meet the new specifications. The later the change in specification happens then larger the impact will be. | Change of project sepcification | Low | Low-High depending on when | Make sure that I allow extra time in my plan for any changes and also make sure that im always ahead/on schedule so that I have time to adapt to any change in product specification |
| 5 | Falling ill  | Falling ill will effect the amount of time I can put into the project causing me to possibly fall behind my schedule as well as effect the quality of any work that I might produce during that time | Stress, poor personal hygiene, poor diet | Low | Medium | follow basic hygiene routines as well as making sure I have regular healthy meals. Allow for time in my schedule to catch up on any work that I have fallen behind on |
| 6 | eye strain | The effects of eye strain is tired or sore, burning and/or itchy feeling in the eye area. Difficulty focusing, increased sensitivity to light, blurred or double vision and other sensations of eye discomfort accompanied by headaches. | Looking at a computer screen for long periods of time | MKedium | Low | follow the 20-20-20 rule, for every 20 minutes looking at a screen take 20 seconds to view something 20 feet away. |
| 7 | Various long term health problems caused by sitting for long periods of time | sitting for long periods every day could cause many various health problems, including Varicose viens, increase in weight and deep vein thrombosis to name a few. | sitting for long periods of time | medium  | low in the shortterm high in the long term | take regular breaks to get up and walk around briefly |
| 8 | Coronavirus | Global pandemic that could possibly lead to lockdowns, curfews and inability to travel into work. | Coronavirus | High | Medium | Follow goverments advice on dealig with Coronavirus and be parpared to remote work from home making sure i have all the nessecery equioment and tools to strat remote learning at a moments notice. |
| 9 | SQL Database is comprimised  | Lose of some tables within databse or complete loss of all data and complete distruction of entire databse | Weak passwords, bad security or malicious attack | Medium | Low | Use a secure password and have correct security protocols in place. Also have SQL code prewritten ready to refil database if needed. |
| 10 | Virtual machine intances are comprimised  | Loss of application funtionality | Weak passwords, bad security or malicious attack | Low | Medium | Be prepared to possibly set up new virtual machines if nessacary and destroy the old ones |
| 11 | Jenkins is Comprimised | Loss of app funtionality and loss of CI | Weak passwords, bad security or malicious attack | Low | Medium | Be prepared to set up a new jenkins enviroment and pipeline for my application |

---

## Architecture 
#### Entity Relationship Diagrams

![A picture of my ERD diagram](https://i.imgur.com/j2NkMcB.png)

The above ERD shows my database structure. I will be using three tables(Songs, Chords and Chords_Songs), With a many to many relationship between the Songs table and Chords_Songs table and also between the Chords table and the Chords_Songs table. The Chords_Songs table is a joining table between the other two tables using both their primary keys as foriegn keys.

#### Application Flow Chart

###### Original Flow Chart
![A picture of my start flow chart](https://i.imgur.com/HlC0Ea0.png)

The above flow chart is the original flow chart plan for my application and shows the basic application structure plan at the beginning of the project. Each dotted box represents a differnet page on the application. All the pages excluding the main song page and main chord page will access the database to create, read, update or delete data.

###### End Flow Chart
![A picture of my end flow chart](https://i.imgur.com/xuJO6BL.png)

The above flow chart is the end flow chart for my application. The additions and altercations have been outlined in red. I firstly added two search funtions one for searching songs that contain a certain chord and the other is for searching chords within a certain song. I also removed the update chord function and replaced it with an add a chord to an existing song.

---

## Testing

For my testing i will be using the pytest and coverage modules within python, the tests will be written in pytest using python and then 

My Testing ism split into two differnt types:
    * URL Testing
    * Database Testing
    
#### URL Testing 

![A picture of my url test](https://i.imgur.com/rdP9I0A.png)

---

## Deployment 

![A picture of my deployemnt structure](https://i.imgur.com/GNTpLvj.png)

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
