import os

file_path = os.path.join(os.getcwd(),'Recipes.txt')

def list_of_recipes(file_name):
    cooK_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            key = line.strip()
            ingredients_list = []
            for i in range(int(file.readline().strip())):
                ingredients = file.readline().strip()
                ingredients_split = ingredients.split('|')
                ingredient_dict = {
                        'ingredient_name': ingredients_split[0],
                        'quantity': int(ingredients_split[1]),
                        'measure': ingredients_split[2],
                }
                ingredients_list.append(ingredient_dict)
            file.readline()
            cooK_book[key] = ingredients_list
        return cooK_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = list_of_recipes('Recipes.txt')
    ingredients_dict = {}
    for dish in dishes:
        for key, value in cook_book.items():
            if cook_book[dish] == cook_book[key]:
                for val in value:
                    key_dict= val['ingredient_name']
                    value_dict = {
                            'measure': val['measure'],
                            'quantity': val['quantity'] * person_count,
                    }
                    if key_dict not in ingredients_dict:
                        ingredients_dict[key_dict] = value_dict
                    else:
                        value_dict['quantity'] += value_dict['quantity']
                        ingredients_dict[key_dict] = value_dict                   
    ingredients_sorted = sorted(ingredients_dict.items(), key=lambda x: x[0])
    ingredients_dict_sorted = dict(ingredients_sorted)                 

    print(ingredients_dict_sorted)
         
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


