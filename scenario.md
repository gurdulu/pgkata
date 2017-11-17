# Scenario

Our client is an association that organises [long distance cycling events](https://en.wikipedia.org/wiki/Randonneuring).

The client has commissioned a web application for managing:

* User registration and profiling
* Events
* Awards

## Initial requirements

Below a description of the tables to create and the list of fields required by the client.

### Table `users`

Each user must provide:

* name
* surname
* DOB
* nationality
* gender

and set a username and password. The password is stored as SHA-256 hash.

### Table `profile`

A registered user can (not mandatory data) provide further information.

* abstract (a quick sentence)
* description
* photo

### Table `additional_info`

Each user can be asked to answer additional questions. The client wants to be able to disclose to third parties 
the data in this table but without reference to the personal data.

* preferred bike brand (chosen from a list)
* are they affected by disabilities
* do they belong to a cycling group 
* which cycling group
* how many times a week they exercise
* how many hours a week they exercise

### Table `login_info`

In addition the client wants to know the user’s activity. 

* login date and time
* logout date and time
* list of pages visited

### Table `events`

An event is a single race across one or more days.

* title
* abstract
* description
* start date
* end date
* number of participants allowed
* location (country)
* category of event (distance)
* difficulty (standard difficulty classification)

### Table `event_registration`

A user can register to multiple events.

* registration date
* make of the bike to be used (selected from a list of brands)
* comments
* result (time)

### Table `awards`

Each participant who ends the race receives an award. The awards vary event by event.

* award name
* event
* user

Our goal is to provide a database definition, some initial data and documentation.
