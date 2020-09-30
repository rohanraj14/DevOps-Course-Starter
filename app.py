from flask import Flask, render_template, request, redirect, url_for
import trello_service as trello

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    """
    App using Trello API 
    """
    return render_template('index.html', cards=trello.get_all_cards())

@app.route('/card/new', methods=['POST'])
def add_card():
    """
    Adding new Trello card
    """
    name = request.form['new_card']
    trello.add_card_by_name(name)
    return redirect(url_for('index'))

@app.route('/card/move', methods=['POST'])
def move_card():
    """
    Moving new Trello card
    """
    card_id = request.form['card_id']
    to_list = request.form['to_list']
    trello.move_card_to_new_list(card_id, to_list)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
