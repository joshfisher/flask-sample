import sqlite3, click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    app.teardown_appcontext(_close)
    app.cli.add_command(_init_db_command)


def incr_difference_request_count(n: int) -> int:
    """
    Increment the request count for `n` and return the new value
    """
    with _get() as db:
        query = "INSERT INTO difference_requests(id) VALUES(?) ON CONFLICT(id) DO UPDATE SET count=count+1;"
        db.execute(query, (n,))

        query = "SELECT count from difference_requests WHERE id=?"
        cursor = db.execute(query, (n,))        
        return cursor.fetchone()["count"]


def _init():
    db = _get()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
@with_appcontext
def _init_db_command():
    _init()
    click.echo("Initialized the database.")


def _get():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def _close(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
