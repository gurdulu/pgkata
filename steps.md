# Steps

## Recommendations

* use an IDE preferably with syntax highlighting
* run the code every time you write a statement
* split the code in several files

> You should be able to execute the statements more than once without errors
  and without changing the structure or the content of the database.

## Database schema

Have a look at the [database diagram](diagram.png) and try to imagine the
database definition (primary keys, relationships, data types, constraints).

## Create the database __pgkata__

Create the database __pgkata__ using the command line tool `createdb`.

```bash
createdb pgkata
```

## Develop a schema based on the requirements

> For the steps in this section create a new file __100-CREATE.sql__.

For each table defined pay attention to:

* PRIMARY KEY (which PRIMARY KEY is the most appropriate for the table)
* fields data types
* constraints (UNIQUE, NOT NULL ...)

### Table __countries__

* create the table __countries__

### Table __users__

* create the table __users__
* does the table have any foreign key reference?
* can the field __gender__ be a separate TYPE?
* what is the length for the __password__ field?

### Table __additional_info__

* create the table __additional_info__
* does the table have any foreign key reference?
* how can you specify a 1-to-1 relationship?

### Table __profiles__

* create the table __profiles__
* does the table have any foreign key reference?
* how can you specify a 1-to-1 relationship?
* what is the appropriate type for the field __photo__

### Table __login_info__

* create the table __login_info__
* does the table have any foreign key reference?
* __pages_visited__ is a list of URLs. What data type can be used?

### Table __events__

* create the table __events__
* does the table have any foreign key reference?
* can the fields __category__ and __difficulty__ be a separate TYPE?
* __abstract__ and __description__ are already defined as part of the
  __profiles__ table. Can you re-use them?

### Table __awards__

* create the table __awards__
* pay attention to the type of the field __time_limit__
* does the table have any foreign key reference?
* how can you create a many-to-many relationship?  

### Table __user_registrations__

* create the table __user_registrations__
* does the table have any foreign key reference
* the field __comments__ is a list of strings
* the field __result__ should be __NOT NULL__ only after the event

## Fixtures

> For the steps in this section create a new file __200-FIXTURES.sql__.

Some of the created tables can be pre-populated. Before proceeding think at
the safest method of populating the tables.

### Fixture for the table __countries__

* add 20 records to the table __countries__
* can you write an INSERT with __country__ as only value?
* can you insert the 20 values using a single statement?
* can you execute the statement more than once?
* what technique can you use for avoiding to delete the records if you need to
  apply the statement more than once?

## Use cases

### As staff member I want to add events to my database

> For the steps in this section create a new file __300-ADDEVENT.sql__.
> Repeat the following steps as many times as you like.

#### __events__ and __awards__ records

* add an event to the table __events__
* add 3 awards to the table to __awards__
* can you think of any modification to the table structure?

### As user I want to sign up for an event

> For the steps in this section create a new file __400-REGISTERUSER.sql__.
> Repeat the following steps as many times as you like.

#### __users__, __profiles__, __additional_info__ records

* add a user to the table __users__ and the correspondent records in
  __profiles__ and __additional_info__
* can you think of any modification to the table structure?

#### __user_registrations__ records

* register the user to one of the events
* can you register the user to the same event more than once?
  (if you can there is an error)

### Prepare reusable scripts

* parameterise the scripts identifying the variables
* can you execute several times the parameterised scripts?

### As staff member I want to update the result of a user

> For the steps in this section create a new file __450-REGISTERUSER.sql__.

The result are recorded in a CSV having the headers

__USERNAME__, __EVENT__, __TIME__.

* using the information in the CSV update the table __user_registrations__
* parameterise the scripts identifying the variables
