#!/usr/bin/env python
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import os
import re
from pathlib import Path
import argparse
import sys

def get_env_variable(key):
    value = os.environ.get(key)
    if not value:
        raise Exception(f"Please add {key} as an environment variable.")
    return value

database_url = get_env_variable("DATABASE_URL")

parser = argparse.ArgumentParser(description='A script to import a database backup from PostgreSQL.')
subparsers = parser.add_subparsers(dest="command", help='The command you want to use.')
subparsers.required = True
import_parser = subparsers.add_parser('import', help='Imports a database file.')
export_parser = subparsers.add_parser('export', help='Exports a database file.')
parser.add_argument('database', type=str, help='The PostgreSQL database backup (gzipped).')


args = parser.parse_args()

m = re.match(r"postgres://(.+):(.*)@(.+):(\d+)/(.+)", database_url)
if m:
    username = m.group(1)
    password = m.group(2)
    host = m.group(3)
    port = m.group(4)
    dbname = m.group(5)
    print(username, password, host, port, dbname)

    if args.command == "import":
        print(args.database)
        if not Path(args.database).exists():
            print(f"Cannot find database {args.database}")
            sys.exit(1)

        print(f"Dropping database {dbname}")

        password_flags = f" --password {password}" if password else ""
        drop_command = f'dropdb "{dbname}" -U {username}'
        os.system(drop_command)

        print(f"Creating database {dbname}")
        create_command = f"createdb {dbname} -U {username}"
        os.system(create_command)

        print(f"Importing database {dbname}")

        import_command = f'gunzip -c "{args.database}" | psql "{dbname}" --host={host} --port={port} --username={username} '
        os.system(import_command)
    elif args.command == "export":
        print("Exporting")
        password_flag = "-W" if password else "-w"
        command = f"pg_dump -d {dbname} -U {username} {password_flag} -p {port} -h {host} | gzip > {args.database}"
        print(command)        
        os.system(command)
