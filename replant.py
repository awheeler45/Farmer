def replant():
    clear()
    planted = 0
    if sunflower_tracking["petals"] < 15:
        sunflower_tracking["petals"] = 15
    
    while planted < get_world_size() ** 2:
        cur_x = get_pos_x()
        if cur_x > maxCoords["x"]:
            maxCoords["x"] = cur_x
        cur_y = get_pos_y()
        if cur_y > maxCoords["y"]:
            maxCoords["y"] = cur_y
            
        if get_ground_type() == Grounds.Turf:
            till()
        
        if get_entity_type() == None:
            plant(Entities.Sunflower)
            planted += 1
            
        if get_pos_y() == maxCoords["y"]:
            move(East)
        move(North)
    return