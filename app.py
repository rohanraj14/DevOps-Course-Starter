from flask import Flask, render_template, request, redirect, url_for
import trello.trello_service  as trello
from trello.view_model  import ViewModel

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    """
    App using Trello API 
    """
    items = trello.get_all_cards()
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)

@app.route('/card/new', methods=['POST'])
def add_card():
    """
    Adding new Trello card
    """
    name = request.form['new_card']
    trello.add_card_by_name(name)
    return redirect(url_for('index'))

@app.route('/card/move/<card_id>')
def move_card(card_id):
    """
    Moving new Trello card
    """
    to_list = request.args.get('to_list')
    trello.move_card_to_new_list(card_id, to_list)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
