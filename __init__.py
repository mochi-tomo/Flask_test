from flask import Flask
app = Flask(__name__)
import sapu_flask.main # type: ignore

from sapu_flask import db # type: ignore
db.create_books_table()