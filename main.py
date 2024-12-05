clear()

plantList = [Entities.Grass, Entities.Bush, Entities.Carrots, Entities.Pumpkin, Entities.Tree]
sunflower_tracking = {"petals": 16, "harvest_counter": 0, "planting": 0, "sunflower_called": False}
maxItems = {"hay": 6000000, "carrot":1000000, "wood":1000000, "pumpkin": 1000000, "treasure": 1000000, "power": 5500000}
minItems = {"hay": 5000000, "carrot":800000, "wood":800000, "pumpkin": 800000, "treasure": 800000, "power": 5000000}
item_mapping = { "hay": Items.Hay, "wood": Items.Wood, "carrot": Items.Carrot, "pumpkin": Items.Pumpkin, "treasure": Items.Gold}
plant_mapping = [
		{"item": "hay", "index": 0},
		{"item": "wood", "index": 4}, 
		{"item": "carrot", "index": 2},
		{"item": "pumpkin", "index": 3},
		{"item": "treasure", "index": 1}
	]
maxCoords = {"x": 0, "y": 0}

while True:
	sunflower_tracking["sunflower_called"] = False
	cur_x = get_pos_x()
	if cur_x > maxCoords["x"]:
		maxCoords["x"] = cur_x
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