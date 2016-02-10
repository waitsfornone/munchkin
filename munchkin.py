from flask import (Flask, g, render_template, redirect, url_for, flash)

import models
import forms
import os
from utils.player import Player
import utils.utils as ut

app = Flask(__name__)
app.secret_key = 'fjqo4igusodjfagnf;o3eg9aihzfn;onic4kqwa0rugf'

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

"""This will be the game script"""

@app.before_request
def before_request():
    g.db = models.db
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    if os.path.isfile('./plyr1.pkl'):
        Player1 = ut.unpkl_plyr()
    else:
        Player1 = ''
    return render_template('index.html', data=Player1)


@app.route('/new_player', methods=('GET', 'POST'))
def new_player():
    form = forms.PlayerForm()
    if form.validate_on_submit():
        Player1 = Player(
            name=form.name.data,
            level=form.level.data,
            race=form.race.data,
            gender=form.gender.data
        )
        ut.pkl_plyr(Player1)
        return redirect(url_for('index'))

    return render_template('new_player.html', form=form)



if __name__ == "__main__":
    models.initialize()
    if os.path.isfile('./plyr1.pkl'):
        os.remove('./plyr1.pkl')
    app.run(debug=DEBUG, host=HOST, port=PORT)
