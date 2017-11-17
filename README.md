# PG Kata

PG Kata is an exercise designed as introduction to [PostgreSQL](https://www.postgresql.org/).

## Pre-requisites

1. PostgreSQL 
   For the documentation on how to install it see [PostgreSQL: Downloads](https://www.postgresql.org/download/).
2. Any editor, preferably with syntax highlighting.
   If you don't have one, install [Atom](https://atom.io/).

## How to proceed

__I assume you are using a *nix platform.__

Create a directory and open you editor.

Open a terminal and create the database __pgkata__.

```bash
# createdb pgkata
```

Read the [scenario](scenario.md) and print out the [diagram](diagram.png).

Start following the [steps](steps.md).

## Useful commands

__psql__ is a very powerful tool. You can have a look at the options with the command `psql --help`.

The options we are going to use are

```text
-c, --command=COMMAND    run only single command (SQL or internal) and exit
-f, --file=FILENAME      execute commands from file, then exit
-b, --echo-errors        echo failed commands
```

Connect to the database __pgkata__ (command `psql pgkata`) and type `\?` for seeing the __psql__ internal commands.

The commands we are going to use are

```text
\d[S+]                 list tables, views, and sequences
\d[S+]  NAME           describe table, view, sequence, or index
\timing [on|off]       toggle timing of commands (currently off)
\h [NAME]              help on syntax of SQL commands, * for all commands
```


