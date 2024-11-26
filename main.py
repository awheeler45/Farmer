clear()

# Define plants
plantList = [Entities.Grass, Entities.Bush, Entities.Carrots, Entities.Pumpkin, Entities.Tree]
sunflower_tracking = {"petal_counter": 15, "harvest_counter": 0}
maxItems = {"hay": 250000, "carrot":25000, "wood":100000, "pumpkin": 10000, "treasure": 50000, "power": 10000}

# max grid
max_x = 0
max_y = 0

while True:
    cur_x = get_pos_x()
    cur_y = get_pos_y()
    if cur_x > max_x:
        max_x = cur_x
    if cur_y > max_y:
        max_y = cur_y
    
    do_harvest()
    watering()
    planter()
    
    # RTB
    if get_pos_y() == max_y:
        move(East)
    move(North)
