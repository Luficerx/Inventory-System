init -5 python:
    from typing import Any

    def setattrs(_object: Any, **kwargs):
        for (key, value) in kwargs.items():
            setattr(_object, key, value)

    class Item():
        def __init__(self, name: str, image: str, id: str, **kwargs):
            self.name = name
            self.image = image
            self.id = id
            setattrs(self, **kwargs)

            if self.id not in global_items:
                global_items[self.id] = self
            
        def __eq__(self, other: Any) -> bool:
            if type(other) is Item:
                return self.name == other.name
            return False

    class Inventory():
        def __init__(self):
            self.items = {}
        
        def add_items(self, *items: Item):
            for item in items:
                self.items[item.id] = 1 if item.id not in self.items else self.items[item.id] + 1
        
        def remove_item(self, key: str):
            self.items[key] -= 1
            if self.items[key] == 0:
                self.items.pop(key)
        
        def get_item(self, key: str) -> Item:
            return global_items[key]

        def get_items(self, ) -> list[Item, int]:
            return [(global_items[x], self.items[x]) for x in self.items]
    
        def has_item(self, key: str) -> bool:
            return key in self.items
        
    class Entity():
        def __init__(self, name: str, **kwargs):
            self.name = name
            self.inv = Inventory()
            setattrs(self, **kwargs)