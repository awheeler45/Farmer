def planting(plant_index):

	plant_type = plantList[plant_index]

	if plant_type in [Entities.Grass, Entities.Bush, Entities.Tree] and get_ground_type() == Grounds.Soil:
		till()
	elif plant_type in [Entities.Carrots, Entities.Pumpkin] and get_ground_type() == Grounds.Turf:
		till()

	if plant_type == Entities.Carrots:
		if num_items(Items.Carrot_Seed) < 1:
			trade(Items.Carrot_Seed, 4)
		plant(Entities.Carrots)
		
	elif plant_type == Entities.Pumpkin:
		if num_items(Items.Pumpkin_Seed) < 1:
			trade(Items.Pumpkin_Seed, 4)
		plant(Entities.Pumpkin)
		
	else:
		plant(plant_type)