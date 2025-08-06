import pandas as pd
from datetime import datetime


class ToDoList:
    def __init__(self):
        self.df = pd.DataFrame(columns=['done', 'item', 'created at'])

    def new_item(self, item):
        new_item = {
            'done': False,
            'item': item,
            'created at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_item])], ignore_index=True)
        print(f'task {item} added to list')

    def remove_item(self, item):
        count = len(self.df)
        self.df = self.df[self.df['item'] != item].reset_index(drop=True)
        if len(self.df) < count:
            print(f'task {item} removed from list')
        else:
            print(f'task {item} not found in list')

    def show_items(self):
        if self.df.empty:
            print('list is empty')
        else:
            print(self.df.reset_index(drop=True).to_string(index=True))

    def mark_as_done(self, item):
        if item in self.df['item'].values:
            self.df.loc[self.df['item'] == item , 'done'] = True
            print(f'task {item} marked as done')
        else:
            print(f'task {item} not found in list')

    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False, encoding='utf-8')
        print(f'ToDo_list {filename} saved to csv')

    def load_from_csv(self, filename):
        try:
            self.df = pd.read_csv(filename, encoding='utf-8')
        except FileNotFoundError:
            print(f'ToDo_list {filename} not found in csv')