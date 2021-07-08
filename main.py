import food_brunch, food_cafe, food_desserts, food_restaurants, food_fastfood

preference = input("What type of food would you prefer to eat: Brunch, Cafe, Fast Food, Desserts, Restaurants? ")

if preference.lower() == "brunch":
    choice = input("Would you like to choose your restaurant by cuisine or location? ")
    if choice.lower() == "cuisine":
        cuisine = input("What type of cuisine would you prefer: American, French, Irish, Italian, Seafood, Spanish? ")
        price = input("What price range would you prefer: $, $$, $$$, $$$$? ")
        for i in range(len(food_brunch.brunch)):
            if cuisine.lower() == food_brunch.brunch[i]["cuisine"] and price.lower() == food_brunch.brunch[i]["pricing"]:
                print(food_brunch.brunch[i]["name"] + " in " + food_brunch.brunch[i]["location"].title())
    if choice.lower() == "location":
        location = input("What location would you like to eat at: Alphabet City, Chelsea, East Village, Greenwich Village,\nLittle Italy, Lower East Side, Meatpacking, Midtown, SoHo, Upper East Side, West Village, Williamsburg? ")
        price = input("What price range would you prefer: $, $$, $$$, $$$$? ")
        for i in range(len(food_brunch.brunch)):
            if location.lower() == food_brunch.brunch[i]["location"] and price.lower() == food_brunch.brunch[i]["pricing"]:
                print(food_brunch.brunch[i]["name"] + " (" + food_brunch.brunch[i]["cuisine"].title() + " food)")

elif preference.lower() == "restaurants":
    choice = input("Would you like to choose your restaurant by cuisine or location? ")
    if choice.lower() == "cuisine":
        cuisine = input("What type of cuisine would you prefer: American, Chinese, French, Irish, Italian, Japanese, Korean? ")
        price = input("What price range would you prefer: $, $$, $$$, $$$$? ")
        for i in range(len(food_restaurants.restaurants)):
            if cuisine.lower() == food_restaurants.restaurants[i]["cuisine"] and price.lower() == food_restaurants.restaurants[i]["pricing"]:
                print(food_restaurants.restaurants[i]["name"] + " in " + food_restaurants.restaurants[i]["location"].title())
    if choice.lower() == "location":
        location = input("What location would you like to eat at: Alphabet City, Chelsea, Chinatown, East Village, Flatiron, Greenwich Village, Little Italy, \nKoreatown, Lower East Side, Meatpacking, Midtown, NoHo, Nolita, SoHo, Tribeca, Upper East Side, West Village? ")
        price = input("What price range would you prefer: $, $$, $$$, $$$$? ")
        for i in range(len(food_restaurants.restaurants)):
            if location.lower() == food_restaurants.restaurants[i]["location"] and price.lower() == food_restaurants.restaurants[i]["pricing"]:
                print(food_restaurants.restaurants[i]["name"] + " (" + food_restaurants.restaurants[i]["cuisine"].title() + " food)")

elif preference.lower() == "cafe":
    choice = input("Would you prefer to choose your cafe by type or location? ")
    if choice.lower() == "type":
        type = input("What would you prefer: bakery, boba, cafe, coffee shop, juices, tea house? ")
        price = input("What price range would you prefer: $, $$? ")
        for i in range(len(food_cafe.cafe)):
            if type.lower() == food_cafe.cafe[i]["Type"] and price.lower() == food_cafe.cafe[i]["Price range"]:
                print(food_cafe.cafe[i]["Name"] + " in " + food_cafe.cafe[i]["Location"].title())
