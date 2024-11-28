def replant():
	clear()
	planted = 0
	# sunflower_tracking["harvested"] = get_world_size() ** 2
	sunflower_tracking["petals"] = 15
	
	while planted <+ 100:
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