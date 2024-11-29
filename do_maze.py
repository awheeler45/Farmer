def do_maze():
	directions = [North, East, South, West]
	index = 0
	
	if get_entity_type() == Entities.Treasure:
		harvest()
		clear()
		
	while get_entity_type() != Entities.Treasure:
		if move(directions[index]):
			if get_entity_type() == Entities.Treasure:
				harvest()
				break
			elif get_entity_type() == Entities.Grass:
				break
			index = (index - 1) % 4
		else:
			index = (index + 1) % 4
