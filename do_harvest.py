def do_harvest():
	current_entity = get_entity_type()

	if can_harvest() and current_entity in [Entities.Grass, Entities.Tree, Entities.Carrots, Entities.Pumpkin]:
		harvest()

	elif can_harvest() and current_entity == Entities.Bush:
		if maxItems["treasure"] > num_items(Items.Gold):
			if num_items(Items.Fertilizer) < 1:
				trade(Items.Fertilizer, 10)
			use_item(Items.Fertilizer)
		else:
			harvest()
			
	elif current_entity == Entities.Sunflower:
		sunflower()

	elif current_entity in [Entities.Hedge, Entities.Treasure]:
		do_maze()