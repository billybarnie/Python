import math

def main():

    with open("cans.txt") as cansfile:

        for line in cansfile:

            can = line.split(",")
            name = can[0].strip()
            radius = float(can[1])
            height = float(can[2])

            volume = compute_volume(radius, height)
            area = compute_surface_area(radius, height)
            storage = storage_effieciency(volume, area, radius)

            storage = volume / area
            
            print(f"{name} {storage:.2f}")



def compute_volume(radius, height):
    return math.pi * (radius ** 2) * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def storage_effieciency(volume, height, radius):
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

main()