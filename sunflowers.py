def sunflower():
	
	if num_items(Items.Sunflower_Seed) <= 100:
		trade(Items.Sunflower_Seed, 100)
	
	if sunflower_tracking["petals"] < 11 or sunflower_tracking["petals"] == 16:
		replant()
		
	if get_entity_type() == Entities.Sunflower:
		petals = measure()

		if petals == sunflower_tracking["petals"]:
			harvest()
			return
		
	if get_pos_x() >= maxCoords["x"] and get_pos_y() >= maxCoords["y"]:
		sunflower_tracking["petals"] -= 1