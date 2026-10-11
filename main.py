def main():
    print("Penne Alla Vodka Receipe")
    make_sauce()
    main_step()
    cook_recipe()
    
    boil_water()
    list_ingredients()
    dish = make_dish("Pasta")



def list_ingredients():
    print("Pasta, onions, heavy cream, garlic, vodka, pasta water")

def make_sauce():
    print("first grab your tomato paste, heavy cream, onions, and garlic")
    print("chop your vegstables thinly, turn your stove on medium heat, and then add your choice of oil")
    print("once the pan is hot, add your onions and garlic. Once they are transparent you can add a full can of tomato paste, a splash of vodka, a 1/2 cup of pasta water, heavy cream, and cheese")

def main_step(): 
    print("Make sure you have: Penne Pasta, tomato pasta, heavy cream, cheese, onions, garlic")


def list_steps(main_step, second_step):
    print(f"Vodka Sauce: {main_step}")
    print(f"Pasta: {second_step}")

def start_dish(tomato_paste, heavy_cream):
    return f"{tomato_paste} and {heavy_cream} Surprise you have your sauce!"

def boil_water():
    print("Get a medium sized pot, and fill water a little bit more than half. Then sprinkle some salt, and turn the stove on medium heat. Once it starts to boil, add the pasta, and set a timer for about 12 minutes. *TIP keep stirring the pasta for about 2 minuties.")


def make_dish():
    print("gather your sauce, and your pasta, and put it together!")

def cook_recipe():
    print("Once your pasta is done boiling, set it aside, and wait for about 2 minutes. While that is set aside, warm up your sauce on low heat, while that is warming up seperate the pasta water and the pasta (SAVE A CUP OF PASTA WATER). Once that is seperated combine the pasta and the sauce. IF the sauce seems a little dry add a bit of pasta water")

   
    print("YAYY!! It is all finished, enjoy your Penne Alla Vodka:")


    if __name__ == "__main__":
    main()