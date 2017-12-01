# Steps

## Recommendations

* use an IDE preferably with syntax highlighting
* run the code every time you write a statement
* split the code in several files
* try not to jump ahead

> You should be able to execute the statements more than once without errors
  and without changing the structure or the content of the database.

## Database schema

Have a look at the [database diagram](assets/diagram.png) and try to imagine the
database definition (primary keys, relationships, data types, constraints).

## Create the database __pgkata__

Create the database __pgkata__ using the command line tool `createdb`.

```bash
createdb pgkata
```

## Develop a schema based on the requirements

> For the steps in this section create a new file __100-create.sql__.

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

> For the steps in this section create a new file __200-fixtures.sql__.

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

> For the steps in this section create a new file __add_event.sql__.

> Repeat the following steps as many times as you like.

#### __events__ and __awards__ records

* add an event to the table __events__
* add 3 awards to the table to __awards__
* can you think of any modification to the table structure?

### As user I want to sign up for an event

> For the steps in this section create a new file __register_user.sql__.

> Repeat the following steps as many times as you like.

#### __users__, __profiles__, __additional_info__ records

* add a user to the table __users__ and the correspondent records in
  __profiles__ and __additional_info__
* can you think of any modification to the table structure?

#### __user_registrations__ records

* register the user to one of the events
* can you register the user to the same event more than once?
  (if you can there is an error)

### As staff member I want to update the result of a user

> For the steps in this section create a new file __update_user_registration.sql__.

The result are recorded in a CSV having the headers

__username__, __event_name__, __date__, __time__

For example

```text
USERNAME;EVENT_TITLE;DATE;TIME
alex;Fantastic rider;2017-05-29;11:42:31
bob;All the way up there;2017-08-11;10:41:45
charlize;All the way up there;2017-08-11;9:41:37
darlene;Fantastic rider;2017-05-29;10:27:08
emanuel;Fantastic rider;2017-05-29;08:27:08
```

* using the information in the CSV update the table __user_registrations__

### Prepare re-usable scripts

You can set variables using `psql` meta-command. Here the relevant section of
the inline help

```
Variables
  \prompt [TEXT] NAME    prompt user to set internal variable
  \set [NAME [VALUE]]    set internal variable, or list all if no parameters
  \unset NAME            unset (delete) internal variable
```

You can achieve the same result using the command line options

```
-v, --set=, --variable=NAME=VALUE
  set psql variable NAME to VALUE
  (e.g., -v ON_ERROR_STOP=1)
```

* what method can you use for parameterising the scripts?
* parameterise the scripts __add_event.sql__, __register_user.sql__ and
  __update_user_registration.sql__ identifying the variables
* can you execute several times the parameterised scripts with the same values?
  (if you can there is an error)

#### Fixtures for __events__, __users__ and __user_registrations__

With the method you have used for parameterising the scripts above, create a
script for inserting the values at [events.csv](csvs/events.csv) and
[users.csv](csvs/users.csv).

Use the following [Python script](scripts/execute.py) for cycle over the CSV
files and execute your statements

```python
import sys
import csv
from subprocess import call


try:
    csv_filename = sys.argv[1]
    sql_filename = sys.argv[2]
    database_name = sys.argv[3]
except:
    print('Usage: %s csv_filename sql_filename database_name' % sys.argv[0])
    sys.exit(1)


def build_vars(row):
    result = []
    for k, v in row.items():
        result.append('-v')
        result.append("%s='%s'" % (k, v))
    return result


with open(csv_filename, 'r') as csv_file:
    r = csv.DictReader(csv_file, delimiter=';')
    for row in r:
        command = ['psql', '-e', ]
        command += ['-f', sql_filename, ]
        command += build_vars(row)
        command.append(database_name)
        call(command)
```

Example

```bash
python execute.py events.csv add_event.sql pgkata
```

* note that one of the fields is a foreign key, how can you link the two tables
  in a single statement?
