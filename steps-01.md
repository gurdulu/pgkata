# Database schema

Have a look at the [database diagram](assets/diagram.png) and try to imagine the
database definition (primary keys, relationships, data types, constraints).

> A primary key is a special relational database table column (or combination of columns)
  designated to uniquely identify all table records. A primary key's main features
  are: It must contain a unique value for each row of data. It cannot contain null values.
  [[quote](https://www.techopedia.com/definition/5547/primary-key)]

---

> A relationship ... is a situation that exists between two relational database
  tables when one table has a foreign key that references the primary key of the other
  table. Relationships allow relational databases to split and store data in different
  tables, while linking disparate data items.
  [[quote](https://www.techopedia.com/definition/24438/relationship-databases)]

---

> A data type is a type of data. ... Some common data types include integers, floating
  point numbers, characters, strings, and arrays. They may also be more specific types,
  such as dates, timestamps, boolean values, and varchar (variable character) formats.
  [[quote](https://techterms.com/definition/datatype)]

---

> SQL constraints are used to specify rules for the data in a table. Constraints are used
  to limit the type of data that can go into a table. This ensures the accuracy and
  reliability of the data in the table.
  [[quote](https://www.w3schools.com/sql/sql_constraints.asp)]

## Create the database *pgkata*

Create the database *pgkata* using the command line tool `createdb`.

```bash
createdb pgkata
```

## Develop a schema based on the requirements

**For the steps in this section create a new file *100-create.sql*.**

For each table defined pay attention to:

* PRIMARY KEY (which PRIMARY KEY is the most appropriate for the table)
* fields data types
* constraints (UNIQUE, NOT NULL ...)

### Table *countries*

* create the table *countries*

### Table *users*

* create the table *users*
* does the table have any foreign key reference?
* can the field *gender* be a separate TYPE?
* what is the length for the *password* field?

> In the context of relational databases, a foreign key is a field (or collection of
  fields) in one table that uniquely identifies a row of another table or the same table.
  In simpler words, the foreign key is defined in a second table, but it refers to the
  primary key or a unique key in the first table.
  [[quote](https://en.wikipedia.org/wiki/Foreign_key)]

### Table *additional_info*

* create the table *additional_info*
* does the table have any foreign key reference?
* how can you specify a 1-to-1 relationship?

> In a relational database, a one-to-one relationship exists when one row in a table
  may be linked with only one row in another table and vice versa.
  [[quote](https://en.wikipedia.org/wiki/One-to-one_(data_model))]

### Table *profiles*

* create the table *profiles*
* does the table have any foreign key reference?
* how can you specify a 1-to-1 relationship?
* what is the appropriate type for the field *photo*

### Table *login_info*

* create the table *login_info*
* does the table have any foreign key reference?
* *pages_visited* is a list of URLs. What data type can be used?

### Table *events*

* create the table *events*
* does the table have any foreign key reference?
* can the fields *category* and *difficulty* be a separate TYPE?
* *abstract* and *description* are already defined as part of the
  *profiles* table. Can you re-use them?

### Table *awards*

* create the table *awards*
* pay attention to the type of the field *time_limit*
* does the table have any foreign key reference?
* how can you create a many-to-many relationship?  

> A many-to-many relationship occurs when multiple records in a table are associated with
  multiple records in another table. For example, a many-to-many relationship exists
  between customers and products: customers can purchase various products, and products
  can be purchased by many customers.
  [[quote](https://fmhelp.filemaker.com/help/16/fmp/en/index.html#page/FMP_Help/many-to-many-relationships.html)]

### Table *users_registrations*

* create the table *users_registrations*
* does the table have any foreign key reference
* the field *comments* is a list of strings
* the field *result* should be **NOT NULL** only after the event

> In databases a common issue is what value or placeholder do you use to represent a
  missing values. In SQL, this is solved with null. It is used to signify missing or
  unknown values. The keyword NULL is used to indicate these values.
  [[quote](https://www.essentialsql.com/get-ready-to-learn-sql-server-what-is-a-null-value/)]

## Seeding

**For the steps in this section create a new file *200-seeding.sql*.**

Some of the created tables can be pre-populated. Before proceeding think at
the safest method of populating the tables.

> Database seeding is the initial seeding of a database with data.
  [[quote](https://en.wikipedia.org/wiki/Database_seeding)]

### Seeding for the table *countries*

* add 20 records to the table *countries*
* can you write an INSERT with *country* as only value?
* can you insert the 20 values using a single statement?
* can you execute the statement more than once?
* what technique can you use for avoiding to delete the records if you need to
  apply the statement more than once?

[Steps](steps.md) - [Populate database](steps-02.md)
