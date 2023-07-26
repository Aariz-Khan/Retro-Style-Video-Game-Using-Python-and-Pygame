from csv import reader

def import_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

#print(import_layout("C:/Users/Aariz Khan/CG_Project/Sprites/Tiles for TILED/Tile CSV/CG Floor_Ruin_Group 2_Invisible Wall.csv"))