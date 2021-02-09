import datetime

class ViewModel:

    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    def get_all_item_of_type(self, list_name):
        item_list = []
        for item in self.items:
            if item.status == list_name:
                item_list.append(item)
        return item_list

    def show_all_done_items(self): 
        """which will keep track of if we
        should show all the completed items, or just the most
        recent ones."""
        return self.get_all_item_of_type('Done')

    

    def recent_done_items(self): 
        """which will return all the tasks that
        have been completed today."""
        items_done =  self.show_all_done_items()
        item_list_done_today = []
        for item in items_done:
            if item.dateLastActivity.date() == datetime.datetime.now().date():
                item_list_done_today.append(item)
        return item_list_done_today
          

    def older_done_items(self): 
        """which will return all of  the tasks that
        were completed before today"""
        items_done =  self.show_all_done_items()
        item_list_done_before_today = []
        for item in items_done:
            if item.dateLastActivity.date() < datetime.datetime.now().date():
                item_list_done_before_today.append(item)
        return item_list_done_before_today