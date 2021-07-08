import food_brunch
#pricing, type of food (brunch/restaurant/etc), location, cuisine
#suggest restaurant

preference = input("What type of food would you prefer to eat: Brunch, Cafes, Fast Food, Desserts, Restaurants? ")
if preference.lower() == "brunch":
    cuisine = input("What type of cuisine would you prefer: American, French, Irish, Italian, Seafood, Spanish? ")
    price = input("What price range would you prefer: $, $$, $$$, $$$$? ")
    for i in range(len(food_brunch.brunch)):
        if cuisine.lower() == food_brunch.brunch[i]["cuisine"] and price.lower() == food_brunch.brunch[i]["pricing"]:
            print(food_brunch.brunch[i]["name"] + " in " + food_brunch.brunch[i]["location"].title())