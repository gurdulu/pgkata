# Steps

## Recommendations

* use an IDE preferably with syntax highlighting
* run the code every time you write a statement
* split the code in several files

## Database schema

Have a look at the [database diagram](diagram.png) and try to imagine the database definition (primary keys,
relationships, data types, constraints).

## Create the database __pgkata__

Create the database __pgkata__ using the command line tool `createdb`.

```bash
createdb pgkata
```

## Develop a schema based on the requirements

For each table created pay attention to:

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

### Table __awards__

* create the table __awards__
* pay attention to the type of the field _time_limit_
* does the table have any foreign key reference?
* how can you create a many-to-many relationship?  

### Table __events__

* create the table __events__
* does the table have any foreign key reference?
* can the fields __category__ and __difficulty__ be a separate TYPE?
* __abstract__ and __description__ are already defined as part of the __profiles__ table. Can you re-use them?

### Table __user_registrations__

* create the table __user_registrations__
* does the table have any foreign key reference?
