from trello.trello_cards import Item

def test_create():
    #Arrange
    card = Item('4637436473gehg', 'This is test')
    
    #Act
    card.create()

    #Assert
    assert card.status == 'To Do'

def test_start():
    #Arrange
    card = Item('4637436473gehg', 'This is test')
    
    #Act
    card.start()

    #Assert
    assert card.status == 'Doing'

def test_complete():
    #Arrange
    card = Item('4637436473gehg', 'This is test')
    
    #Act
    card.complete()

    #Assert
    assert card.status == 'Done'
  