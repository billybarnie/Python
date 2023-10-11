
with open("hr_system.txt") as human:
    for line in human:
        line.strip()
        parts = line.split(" ")
        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = float(parts[3])
        check = (salary/24)
        if title.lower() == "engineer":
            check += 1000

        print(f"Name: {name}(ID: {id}), Title: {title} - ${check:.2f}")

        