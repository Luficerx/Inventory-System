init -8 python:
    class RemoveItem(Action):
        def __init__(self, entity: Any, item: Any, **kwargs):
            self.item = item
            self.entity = entity
        
        def __call__(self, *args):
            self.entity.inv.remove_item(self.item.id)
            renpy.restart_interaction()

    class AddItem(Action):
        def __init__(self, entity: Any, *item: Any, **kwargs):
            self.item = item
            self.entity = entity
        
        def __call__(self, *args):
            self.entity.inv.add_items(*self.item)
            renpy.restart_interaction()