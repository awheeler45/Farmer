def sunflower():
    petal_counter = sunflower_tracking["petal_counter"]
    harvest_counter = sunflower_tracking["harvest_counter"]

    if get_ground_type() == Grounds.Turf:
        till()

    if num_items(Items.Sunflower_Seed) <= 1:
        trade(Items.Sunflower_Seed, 7)

    if get_entity_type() == Entities.Sunflower:
        petals = measure()

        if petals == petal_counter:
            harvest()
            plant(Entities.Sunflower)
            sunflower_tracking["harvest_counter"] = 0 
            return

    elif get_entity_type() == None:
        plant(Entities.Sunflower)
        sunflower_tracking["petal_counter"] = 15
        sunflower_tracking["harvest_counter"] = 0 
        return
        

    harvest_counter += 1

    if harvest_counter >= 81:
        petal_counter -= 1
        harvest_counter = 0

        if petal_counter <= 9:
            petal_counter = 15

    sunflower_tracking["petal_counter"] = petal_counter
    sunflower_tracking["harvest_counter"] = harvest_counter
