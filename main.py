import food_brunch
import food_cafe
import food_desserts
import food_fastfood
import food_restaurants
#pricing, type of food (brunch/restaurant/etc), location, cuisine
#suggest restaurant

preference = input("What type of food would you prefer to eat: Brunch, Cafes, Fast Food, Desserts, Restaurants? ")

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

