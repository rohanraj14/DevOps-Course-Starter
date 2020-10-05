from trello.view_model import ViewModel
from trello.trello_cards import Item
import datetime

def test_get_all_item_of_doing_list():
    #Arrange 
    items=[Item('4637436473gehg', 'This is test', "2020-08-11T22:40:47.415Z", 'Done'), 
                Item('54gfg435543g', 'This is test2',"2020-09-11T22:40:37.435Z", 'Doing'), 
                Item('t4545ffgfgf', 'This is test3', "2020-09-21T02:40:42.433Z", 'Doing'), 
                Item('sddffw5455', 'This is test4', "2020-09-23T20:40:07.565Z", 'To Do'),
                Item('54gfg435543g', 'This is test2',"2020-09-11T12:40:42.123Z", 'Done'), 
                Item('t4545ffgfgf', 'This is test3', "2020-09-18T08:40:37.414Z", 'Doing'), 
                Item('sddffw5455', 'This is test4', "2020-09-19T05:40:22.444Z", 'To Do')]
    view_model= ViewModel(items)
    #Act
    items_doing = view_model.get_all_item_of_type('Doing')
    #Assert
    assert items_doing[0].status == 'Doing'

def test_show_all_done_items():
    #Arrange 
    items=[Item('4637436473gehg', 'This is test', "2020-08-11T22:40:47.415Z", 'Done'), 
                Item('54gfg435543g', 'This is test2',"2020-09-11T22:40:37.435Z", 'Doing'), 
                Item('t4545ffgfgf', 'This is test3', "2020-09-21T02:40:42.433Z", 'Doing'), 
                Item('sddffw5455', 'This is test4', "2020-09-23T20:40:07.565Z", 'To Do'),
                Item('54gfg435543g', 'This is test2',"2020-09-11T12:40:42.123Z", 'Done'), 
                Item('t4545ffgfgf', 'This is test3', "2020-09-18T08:40:37.414Z", 'Doing'), 
                Item('sddffw5455', 'This is test4', "2020-09-19T05:40:22.444Z", 'To Do')]
    view_model= ViewModel(items)

    #Act
    items_done = view_model.show_all_done_items()

    #Assert
    assert items_done[1].status == 'Done'
    assert len(items_done)==2

def test_recent_done_items():
    #Arrange 
    time_for_udate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    items=[Item('4637436473gehg', 'This is test', "2020-08-11T22:40:47.415Z", 'Done'), 
                Item('54gfg435543g', 'This is test2',"2020-09-11T22:40:37.435Z", 'Doing'), 
                Item('t4545ffgfgf', 'This is test3', "2020-09-21T02:40:42.433Z", 'Doing'), 
                Item('sddffw5455', 'This is test4', "2020-09-23T20:40:07.565Z", 'To Do'),
                Item('54gfg435543g', 'This is test2',"2020-09-11T12:40:42.123Z", 'Done'), 
                Item('t4545ffgfgf', 'This is test3', time_for_udate, 'Done'), 
                Item('sddffw5455', 'This is test4', "2020-09-19T05:40:22.444Z", 'To Do'),
                Item('54gfg435543g', 'This is test2',time_for_udate, 'Done')]
    view_model= ViewModel(items)

    #Act
    items_recent_done = view_model.recent_done_items()

    #Assert
    assert items_recent_done[1].status == 'Done'
    assert len(items_recent_done)==2

def test_older_done_items():
    #Arrange 
    time_for_udate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    items=[Item('4637436473gehg', 'This is test', "2020-08-11T22:40:47.415Z", 'Done'), 
                Item('54gfg435543g', 'This is test2',"2020-09-11T22:40:37.435Z", 'Doing'), 
                Item('t4545ffgfgf', 'This is test3', "2020-09-21T02:40:42.433Z", 'Doing'), 
                Item('sddffw5455', 'This is test4', "2020-09-23T20:40:07.565Z", 'To Do'),
                Item('54gfg435543g', 'This is test2',"2020-09-11T12:40:42.123Z", 'Done'), 
                Item('t4545ffgfgf', 'This is test3', time_for_udate, 'Done'), 
                Item('sddffw5455', 'This is test4', "2020-09-19T05:40:22.444Z", 'To Do'),
                Item('54gfg435543g', 'This is test2',time_for_udate, 'Done')]
    view_model= ViewModel(items)

    #Act
    items_older_done = view_model.older_done_items()

    #Assert
    assert items_older_done[0].status == 'Done'
    assert len(items_older_done)==2
