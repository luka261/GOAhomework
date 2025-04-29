# 1) მიმოიხედეთ ოთახში, აირჩიეთ რაიმე ობიექტი და შექმენით მისი dictionary (მინიმუმ 5 key:value pair უნდა ჰქონდეს)

object = {
    "name": "laptop",
    "brand": "Dell",
    "color": "silver",
    "screen_size": "15.6 inches",
    "weight": "1.8 kg"
}

# 2) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები

for key in object.keys():
    print(key)

# 3) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს value'ები

for value in object.values():
    print(value)

# 4) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები და value'ები ერთად

for key, value in object.items():
    print(f"{key}: {value}")
