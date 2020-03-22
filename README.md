# QA SFIA Project 1

 ## Contents 

1. Brief 
    * Objective
    * Requirements
2. Project Plan
    * Sprints
3. Risk Assessment 
4. Architecture 
    * Entity Relationship Diagram
    * Application Flow Chart
5. Testing 
6. Deployment
    * CI Pipeline
7. Evaluation

---

## Brief 
#### Objective:
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

#### Requirements:
* Trello Board
* Relational database used to store data persistently for the project, this database needs to have at least 2 tables in it
* ERD diagram modelling the relationship
* Risk Assessment
* Clear Documentation from a design phase describing the architecture you will use for you project
* Functional CRUD application created in Python
* Fully designed test suites
* A functioning front-end website and integrated API’s, using Flask.
* Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine

---

## Project Plan 

I plan on splitting my project into 5 separate sprints each of which will last a week. By the end of the 5 sprints I will have a fully working CRUD application meeting all of the requirements listed previously.

#### Trello Board Key 

![Picture of first sprint](https://i.imgur.com/z4DhuyS.png)
Above is a key for the labels used on my trello board

#### Sprint 1: 

![Picture of first sprint](https://i.imgur.com/ece3sed.png)

These are the tasks planned for the first sprint. The first sprint is fairly basic mainly containing tasks setting up the foundations for the following sprints.

#### Sprint 2:

![Picture of second sprint](https://i.imgur.com/tGJ8Pmv.png)

These are the tasks planned for the second sprint. The second sprint contains tasks relating to the database needed for the application.

#### Sprint 3:

![Picture of third sprint](https://i.imgur.com/bljkSjF.png)

These are the tasks planned for the third sprint. The third sprint contains tasks relating to the user interface design and planning the overall flow of the user interface.

#### Sprint 4:

![Picture of fourth sprint](https://i.imgur.com/dZVTxoU.png)

These are the tasks planned for the fourth sprint. The fourth sprint contains coding tasks for the application, mainly the tasks need for the minimal viable product as well as those fulfilling the Create, Read and update methods.

#### Sprint 5:

![Picture of fifth sprint](https://i.imgur.com/rElBBpU.png)

These are the tasks planned for the fifth sprint. The fifth sprint contains coding tasks for the application for the Delete methods as well as any extensions to the application I would like to add. The fifth sprint also contains the CI pipeline tasks.

---

## Risk Assessment 

|Risk No. | Risk | Effect | Cause | Likelihood | Impact | Solution |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Overreaching on the project | Overreaching on the project will lead to the project becoming too complicated . This in turn will mean that I might not be able to turn in a finished product and I might lose motivation for the project. | Overestimation of my abilities. | Low | High | Keep the project simple while still meeting all then targets and if I have extra time at the end of the project I can then slowly add extra features once the core project is done. |
| 2 | Project not meeting the specifications | Not meeting the specifications will lead to a project that isn't complete and will then mean a bad mark for the SFIA project. | Not understanding the specification. | Low | Medium | Talk to others doing the project and also those who set the specification to make sure my project meets the specification. |
| 3 | Organising the tasks ineffectively  | Non efficient organisation of the tasks will lead to tasks taking longer the necessary and  could impact the overall time needed for the task and possibly cause me not to make the deadline. | Planning to do tasks before I'm capable, planning to do tasks before their respective prerequisite tasks aren't complete | Low | Medium | Plan when I'm doing specific tasks to coincide with when I have completed the training and also setting tasks to be complted in the correct order so any prerequisite tasks are complete first. |
| 4 | Change of project specification | A change of project specification will lead to me having to possibly revise my project idea and structure if it doesn't meet the new specifications. The later the change in specification happens then larger the impact will be. | Change of project specification | Low | Low-High depending on when | Make sure that I allow extra time in my plan for any changes and also make sure that I'm always ahead/on schedule so that I have time to adapt to any change in product specification |
| 5 | Falling ill  | Falling ill will affect the amount of time I can put into the project causing me to possibly fall behind my schedule as well as effect the quality of any work that I might produce during that time | Stress, poor personal hygiene, poor diet | Low | Medium | follow basic hygiene routines as well as making sure I have regular healthy meals. Allow for time in my schedule to catch up on any work that I have fallen behind on |
| 6 | Eye strain | The effects of eye strain is tired or sore, burning and/or itchy feeling in the eye area. Difficulty focusing, increased sensitivity to light, blurred or double vision and other sensations of eye discomfort accompanied by headaches. | Looking at a computer screen for long periods of time | Medium | Low | follow the 20-20-20 rule, for every 20 minutes looking at a screen take 20 seconds to view something 20 feet away. |
| 7 | Various long term health problems caused by sitting for long periods of time | sitting for long periods every day could cause many various health problems, including Varicose veins, increase in weight and deep vein thrombosis to name a few. | sitting for long periods of time | Medium  | low in the short term high in the long term | take regular breaks to get up and walk around briefly |
| 8 | Coronavirus | Global pandemic that could possibly lead to lockdowns, curfews and inability to travel into work. | Coronavirus | High | Medium | Follow governments advice on dealing with Coronavirus and be prepared to remote work from home making sure I have all the necessary equipment and tools to start remote learning at a moment's notice. |
| 9 | SQL Database is compromised | Loss of some tables within database or complete loss of all data and complete destruction of entire database | Weak passwords, bad security or malicious attack | Medium | Low | Use a secure password and have correct security protocols in place. Also have SQL code prewritten ready to recreate and refill database if needed. |
| 10 | Virtual machine instances are compromised | Loss of application functionality | Weak passwords, bad security or malicious attack | Low | Medium | Be prepared to possibly set up new virtual machines if necessary and destroy the old ones |
| 11 | Jenkins is compromised | Loss of app functionality and loss of CI | Weak passwords, bad security or malicious attack | Low | Medium | Be prepared to set up a new Jenkins environment  and pipeline for my application |

---

## Architecture 
#### Entity Relationship Diagrams

![A picture of my ERD diagram](https://i.imgur.com/j2NkMcB.png)

The above ERD shows my database structure. I will be using three tables(Songs, Chords and Chords_Songs), With a many to many relationship between the Songs table and Chords_Songs table and also between the Chords table and the Chords_Songs table. The Chords_Songs table is a joining table between the other two tables using both their primary keys as foreign keys.

#### Application Flow Chart

###### Original Flow Chart
![A picture of my start flow chart](https://i.imgur.com/HlC0Ea0.png)

The above flow chart is the original flow chart plan for my application and shows the basic application structure plan at the beginning of the project. Each dotted box represents a differenet page on the application. All the pages excluding the main song page and main chord page will access the database to create, read, update or delete data.

###### End Flow Chart
![A picture of my end flow chart](https://i.imgur.com/xuJO6BL.png)

The above flow chart is the end flow chart for my application. The additions and altercations have been outlined in red. I firstly added two search functions one for searching songs that contain a certain chord and the other is for searching chords within a certain song. I also removed the update chord function and replaced it with an add a chord to an existing song.

---

## Testing

For my testing i will be using the pytest and coverage modules within python, the tests will be written in pytest using python and then 

My Testing ism split into two different types
* URL Testing
* Database Testing
    
#### URL Testing 

![A picture of my url test](https://i.imgur.com/rdP9I0A.png)

The above picture is an example of one of the URL test that I ran on my application. This test use the python module urllib3 to test the HTTP response. It takes the inputted URL, in this case http://34.68.124.32:5000/ and saves the response as the variable  r. It then tests the status of the variable against the HTTP response status 200 (which is the OK status indicating a successful connection) and if the two statuses match then the test is passed.
I used this layout of code to test the successful connection to all twelve of my different URL pages as well as changing the 200 status with a 404 status to test a page that doesn't exist on the website.


#### Database Testing

![A picture of my database test](https://i.imgur.com/9zmFafY.png)

The above picture is an example of one of my database tests. This test uses the python modules Flask, Flask_mysqldb and os to test the connection to the database. Using the pre-set details for my database it selects all the values inside the Songs table and compares how many values inside the table to how many were expected and then if the two values match then the test is considered a success.
For all three of my tables inside of my database I ran four different tests, one for each CRUD method making a total of 12 database tests.

---

## Deployment 

![A picture of my deployement structure](https://i.imgur.com/GNTpLvj.png)

Technologies used:
* Github: hosting for software development version control
* Python: high-level, general-purpose programming language
* Pytest: testing framework
* Flask: micro web framework 
* Jinja: web template engine
* HTML:  mark-up language for web browsers
* CSS: style sheet language
* Jenkins: open source automation server
* Google Cloud Platform: cloud computing services
* MYSQL: open-source relational database management system

#### CI Pipeline 

For my CI pipeline I will be using a Jenkins server with a webhook connection to my github for automated builds whenever anything is committed to my github. My jenkins Pipeline will be split into two sections a development environment which will install any required tools and then run the application. The second section will be a testing section which will run the tests talked about previously.

## Evaluation 

Have mi meet the requirements previously stated in this documentation.

1. Trello Board

I used a trello board throughout my project, using it to keep track of the sprint progress.

2. Relational database used to store data persistently for the project, this database needs to have at least 2 tables in it

I have a relational database containing three tables and two many to many relationships between these tables.

3. ERD diagram modelling the relationship

Previously shown in documentation 

4. Risk Assessment

Previously shown in documentation 

5. Clear Documentation from a design phase describing the architecture you will use for you project

Shown in documentation 

6. Functional CRUD application created in Python

I have made a fully functioning CRUD application with each method being used at leadt once, this was coded using python, HTML, CSS and SQL.

7. Fully designed test suites

Previously shown in documentation 

8. A functioning front-end website and integrated API’s, using Flask.

I have made a front-end website that runs using flask and a Jenkins pipeline

9. Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine

Achieved, using a Jenkins pipeline for the CI server.

As shown above all nine requirements of the project were meet therefore I would consider the project a success. Although the project was a success there is possible areas for extension. These areas include expanding testing to up the coverage percentage, selenium testing and a user log in function so that each user can store the chords that they have learnt.






