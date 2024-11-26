def planter():
    if num_items(Items.Hay) < maxItems["hay"]:
        planting(0)
        
    elif num_items(Items.Wood) < maxItems["wood"]:
        if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
            planting(4) 
        elif get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
            planting(4)
        else: 
            planting(0)
            
    elif num_items(Items.Carrot) < maxItems["carrot"]:
        planting(2)
                
    elif num_items(Items.Pumpkin) < maxItems["pumpkin"]:
        planting(3)
        
    elif num_items(Items.Gold) < maxItems["treasure"]:
        if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
            planting(4) 
        elif get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
            planting(4)
        else:
            planting(1)

    else:
        sunflower()
