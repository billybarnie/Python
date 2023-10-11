
user = input("Which volume would you like to research? ")

largest_scripture = 0
biggest_book = ""

with open("books_and_chapters.txt") as scripture:
    for verse in scripture:
        parts = verse.split(":")
        script = parts[0].strip()
        chapter = int(parts[1])
        testament = parts[2].strip()

        if testament.lower() == user.lower():

            if chapter > largest_scripture:
                largest_scripture = chapter
                biggest_book = script


print(f"Book with the largest amount of chapters in {user} is: {biggest_book} with {largest_scripture} chapters.")
