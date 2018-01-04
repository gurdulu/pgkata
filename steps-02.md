# Use cases

## As staff member I want to add events to my database

**For the steps in this section create a new file *add_event.sql*.**

**Repeat the following steps as many times as you like.**

### *events* and *awards* records

* add an event to the table *events*
* add 3 awards to the table to *awards*
* can you think of any modification to the tables structure?

## As user I want to sign up for an event

**For the steps in this section create a new file *register_user.sql*.**

**Repeat the following steps as many times as you like.**

### *users*, *profiles*, *additional_info* records

* add a user to the table *users* and the correspondent records in *profiles* and
  *additional_info*
* can you think of any modification to the tables structure?

### *user_registrations* records

* register the user to one of the events
* can you register the user to the same event more than once?
  (if you can there is an error)

## As staff member I want to update the result of a user

**For the steps in this section create a new file *update_user_registration.sql*.**

The result are recorded in a CSV having the headers

*username*, *event_name*, *date*, *time*

For example

```text
USERNAME;EVENT_TITLE;DATE;TIME
alex;Fantastic rider;2017-05-29;11:42:31
bob;All the way up there;2017-08-11;10:41:45
charlize;All the way up there;2017-08-11;9:41:37
darlene;Fantastic rider;2017-05-29;10:27:08
emanuel;Fantastic rider;2017-05-29;08:27:08
```

* using the information in the CSV update the table *user_registrations*

## Prepare re-usable scripts

You can set variables using `psql` meta-commands. Here the relevant section of
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
* parameterise the scripts *add_event.sql*, *register_user.sql* and
  *update_user_registration.sql* identifying the variables
* can you execute several times the parameterised scripts with the same values?
  (if you can there is an error)

### Fixtures for *events*, *users* and *user_registrations*

With the method you have used for parameterising the scripts above, create a
script for inserting the values at [events.csv](csvs/events.csv) and
[users.csv](csvs/users.csv).

Use [this script](scripts/execute.py) for cycling over the CSV files and
executing your statements.

Example

```bash
# python scripts/execute.py events.csv add_event.sql pgkata
```

* note that one of the fields is a foreign key, how can you link the two tables
  in a single statement?
