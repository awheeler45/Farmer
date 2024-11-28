def sunflower():
	max_harvest = get_world_size() ** 2
	
	if num_items(Items.Sunflower_Seed) <= 100:
		trade(Items.Sunflower_Seed, 100)
	
	if sunflower_tracking["petals"] < 11:
		replant()
		
	if get_entity_type() == Entities.Sunflower:
		petals = measure()

		if petals == sunflower_tracking["petals"]:
			harvest()
			sunflower_tracking["harvest_counter"] = 0
			return

	sunflower_tracking["harvest_counter"] += 1

	if sunflower_tracking["harvest_counter"] >= max_harvest:
		sunflower_tracking["petals"] -= 1
		sunflower_tracking["harvest_counter"] = 0
		
	# if get_pos_x() >= get_world_size() and get_pos_y() >= get_world_size() :
		# sunflower_tracking["petals"] -= 1