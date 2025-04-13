def planter():
    
    if sunflower_tracking["planting"] == 1:
        if num_items(Items.Power) < maxItems["power"]:
            if not sunflower_tracking["sunflower_called"]:
                sunflower()
                sunflower_tracking["sunflower_called"] = True
            return
        else:
            sunflower_tracking["planting"] = 0

    if num_items(Items.Power) < minItems["power"]:
        sunflower_tracking["planting"] = 1
        if not sunflower_tracking["sunflower_called"]:
            sunflower()
            sunflower_tracking["sunflower_called"] = True
        return

    next_plant = None
    for plant in plant_mapping:
        item_name = plant["item"]
        plant_index = plant["index"]
        item_obj = item_mapping[item_name]
        
        if num_items(item_obj) < minItems[item_name]:
            next_plant = plant_index
            break

        elif num_items(item_obj) < maxItems[item_name]:
            next_plant = plant_index
            break

    if next_plant != None:
        if next_plant == 4:
            if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
                planting(4)
            elif get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
                planting(4)
            else:
                planting(0)
        else:
            planting(next_plant)
    else:
        if not sunflower_tracking["sunflower_called"]:
            sunflower()
            sunflower_tracking["sunflower_called"] = True