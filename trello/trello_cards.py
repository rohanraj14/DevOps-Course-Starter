import datetime

class Item:

    def __init__(self, id, name, dateLastActivity, status = 'To Do'):
        self.id = id
        self.name = name
        self.dateLastActivity = datetime.datetime.strptime(dateLastActivity, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.status = status

    @classmethod
    def trelloCard(cls, item, list):
        return cls(item['id'], item['name'], item['dateLastActivity'], list['name'])
    
