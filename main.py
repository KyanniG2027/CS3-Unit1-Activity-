def main():
    print("Penne Alla Vodka Receipe")
    make_sauce()
    main_step()
    cook_recipe()
      

def make_sauce():
    print("first grab your tomato paste, heavy cream, onions, and garlic")
    print("chop your vegstables thinly, turn your stove on medium heat, and then add your choice of oil")
    print("once the pan is hot, add your onions and garlic. Once they are transparent you can add a full can of tomato paste, a splash of vodka, a 1/2 cup of pasta water, heavy cream, and cheese")

def main_step(): 
    print("Make sure you have: Penne Pasta, tomato pasta, heavy cream, cheese, onions, garlic")


def list_steps(main_step, second_step):
    print(f"Vodka Sauce: {main_step}")
    print(f"Pasta: {second_step}")

def start_dish(tomato paste, heavy cream):
    return f"{tomato paste} and {heavy cream} Surprise you have your sauce!"

def cook_recipe():
    boil_water()
    list_ingredients("Pasta, onions, heavy cream, garlic, vodka, pasta water")
    dish = make_dish("Pasta")
    print("Penne Alla Vodka:", dish)
    





if __name__ == "__main__":
    main()