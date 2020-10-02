from trello.trello_cards import Item

def test_create():
    #Arrange
    card = Item('4637436473gehg', 'This is test')
    
    #Act
    card.create()

    #Assert
    assert card.status == 'To Do'
  