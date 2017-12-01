import sys
import csv
from subprocess import call


try:
    csv_filename = sys.argv[1]
    sql_filename = sys.argv[2]
    database_name = sys.argv[3]
except:
    print('Usage: %s csv_filename sql_filename database_name' % sys.argv[0])


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
