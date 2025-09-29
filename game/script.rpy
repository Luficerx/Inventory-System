default mc = Entity("Jacob")

default global_items = {}
default iron_sword = Item("Iron Sword", Solid("#FFF", xysize=(75, 75)), "iron_sword")
default granite_rock = Item("Granite Rock", Solid("#c8d9bf", xysize=(75, 75)), "granite_rock")

screen main_inventory():
    add "#ACACAC"

    frame:
        background "#181818"
        xysize (800, 600) offset (10, 10)

        vbox:
            spacing 5
            for (item, amount) in mc.inv.get_items():
                button:
                    action RemoveItem(mc, item)
                    hbox:
                        spacing 5
                        add item.image
                        vbox:
                            text "[item.name]" outlines [(1, "#FFF", 0, 0)] color "#000" bold True size 22
                            if amount > 1:
                                text "[amount]x" outlines [(1, "#FFF", 0, 0)] color "#000" bold True size 22

label start:
    python:
        mc.inv.add_items(iron_sword)
        mc.inv.add_items(granite_rock, granite_rock, granite_rock)

    call screen main_inventory