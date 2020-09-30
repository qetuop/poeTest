from flask import render_template, flash, redirect
from app import app
import poeq
from app.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    leagues = poeq.getLeagues()
    form.league.choices = [(league, league) for league in leagues]

    if form.validate_on_submit():
        print('here')
        account = form.account.data
        league = form.league.data
        poesessid = form.poessid.data

        poeq.setup(league, account, poesessid)

        numTabs = poeq.getNumTabs()  # {'numTabs': 28}  or {'error': {'code': 6, 'message': 'Forbidden'}}
        print(numTabs)
        form.tabs.data = numTabs


        #flash('NOU3')
        #return redirect('login')
        return render_template('index.html', form=form)


    return render_template('index.html', form=form)