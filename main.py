clear()

# Define plants
plantList = [Entities.Grass, Entities.Bush, Entities.Carrots, Entities.Pumpkin, Entities.Tree]
sunflower_tracking = {"petals": 0, "harvest_counter": 0, "harvested": 0}
maxItems = {"hay": 250000, "carrot":500000, "wood":500000, "pumpkin": 500000, "treasure": 100000, "power": 1000}
maxCoords = {"x": 0, "y": 0}

while True:
	cur_y = get_pos_y()
	if cur_y > maxCoords["y"]:
		maxCoords["y"] = cur_y
        	
	do_harvest()
	watering()
	planter()
	
	# RTB
	if get_pos_y() == maxCoords["y"]:
		move(East)
	move(North)