def watering():
	if get_water() < 0.75:
			if num_items(Items.Water_Tank) < 10:
				trade(Items.Empty_Tank)
				use_item(Items.Water_Tank)
			else:
				use_item(Items.Water_Tank)