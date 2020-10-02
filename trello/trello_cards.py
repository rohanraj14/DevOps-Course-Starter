class Item:

    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def trelloCard(cls, item, list):
        return cls(item['id'], item['name'], list['name'])
    
    def create(self):
        self.status = 'To Do'

    def start(self):
        self.status = 'Doing'

    def complete(self):
        self.status = 'Done'

    def show_all_done_items(self): 
        """which will keep track of if we
        should show all the completed items, or just the most
        recent ones."""

    def recent_done_items(self): 
        """which will return all the tasks that
        have been completed today."""
    
    def older_done_items(self): 
        """which will return all of  the tasks that
        were completed before today"""