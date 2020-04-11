import pymysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_db():
    cursor = get_db().cursor()
    with current_app.open_resource('schema.sql') as f:
        cursor.execute(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host='localhost',
                                user='admin',
                                password='remember',
                                db='flask',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)


    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)