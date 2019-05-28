import datetime
import os

from sqlalchemy.exc import OperationalError
connected = False
while not connected:
    try:
        import database
        database.init_db()
        connected = True
    except OperationalError:
        continue

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        database.db_session.add(item)
        database.db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success(): 
    qry = database.db_session.query(Items)
    results = [(item.id, item.name, item.description, str(item.date_added)) for item in qry.all()]
    return str(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("5001"))
