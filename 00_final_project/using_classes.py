from ToDoList_class import ToDoList

todo = ToDoList()

todo.new_item("reading first chapter of the book")
todo.new_item("exercise pandas")
todo.show_items()

todo.mark_as_done("exercise pandas")
todo.show_items()

todo.save_to_csv("todo_list.csv")
todo.load_from_csv("todo_list.csv")
todo.remove_item("reading first chapter of the book")
todo.show_items()
