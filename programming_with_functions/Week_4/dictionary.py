bad_guys = {
    "daredevil": "kingpin",
    "x-men": "apocalypse",
    "batman": "bane"
}
print(bad_guys)


print(bad_guys['batman'])
print(bad_guys['x-men'])
print(bad_guys['daredevil'])

bad_guys['x-men'] = 'juggernaut' #This changes the output of the key and the key is x-men

print(bad_guys['x-men'])    

print(bad_guys)

del bad_guys['x-men']   #This is used to delete a key from the dictionary

print(bad_guys) 

d = {
    0: "plane",
    1: "train"
}

print(d[0])