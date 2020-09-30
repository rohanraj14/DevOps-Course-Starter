class Item:

    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def trelloCard(cls, item, list):
        return cls(item['id'], item['name'], list['name'])
        