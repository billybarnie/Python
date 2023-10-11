user_input = 0
user = ""
first = 1
country_max = ''
country_min = ''
max_year = 0
min_year = 3000
whole = 0.0
index = 0.0
country_max1 = ''
country_min1 = ''
maximum = 0
minimum = 3000

while user != "no":
    user_input = int(input("Enter the year of interest: "))
    min = 150.0
    max = 0.0
    max_expectancy = 0
    min_expectancy = 150
    with open("life-expectancy.csv") as hr_file:
        next(hr_file)
        for line in hr_file:
            
            parts = line.split(",")
            country = parts[0].strip()
            acronym = parts[1].strip()
            year = int(parts[2])
            expectancy = float(parts[3])
            
            if expectancy > max_expectancy:
                max_expectancy = expectancy
                country_max = country
                max_year = year
            if expectancy < min_expectancy:
                min_expectancy = expectancy
                country_min = country
                min_year = year
            if year == user_input:
                whole += expectancy
                index += 1
                if expectancy < min:
                    min = expectancy
                    country_min1 = country
                if expectancy > max:
                    max = expectancy
                    country_max1 = country
                    
                    
    print()
    print(f"The overall max life exceptancy is: {max_expectancy} from {country_max} in {max_year}")
    print(f"The overall min life exceptancy is: {min_expectancy} from {country_min} in {min_year}")

    print()
    print(f"For the year {user_input}:")
    print(f"The life expectancy average in {user_input} is {whole/index:.2f}")
    print(f"The max life expectancy was in {country_max1} with {max}")
    print(f"The min life expectancy was in {country_min1} with {min}")

    user = input("Would you like to research other years? (yes/no): ")
    if user == "yes":
        print()
        print("Okay feel free to do more research.")
        print()
    else:
        print()
        print("Have a wonderful day.")
        exit()



