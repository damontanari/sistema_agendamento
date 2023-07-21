from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'D@niel'

from views import *

if __name__ == '__main__':
    app.run(debug=True)
