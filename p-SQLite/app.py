from flask import Flask, redirect, url_for, render_template, request
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


if __name__ == '__main__':
   app.run(debug = True)