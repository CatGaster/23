import pprint

def my_cook_book():
    with open('Recipes.txt', encoding='utf-8') as file:
        meal = {}  
        for line in file.read().split('\n\n'):
            ingredients_quantity = []  # ингридиенты количество
            name, *ingredients = line.split('\n')
            for ingredient in ingredients[1:]:
                ingredient_name, quantity, measure = ingredient.split('|')
                ingredients_quantity.append(
                          {
                              'ingredient_name': ingredient_name,
                              'quantity': int(quantity),
                              'measure': measure
                          }
                      )
                meal[name] = ingredients_quantity
        return meal

cook_book = my_cook_book()

def get_shop_list_by_dishes(dishes, person_count):
    counted_list = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for i in ingredients:
                ingredient_name = i['ingredient_name']
                count = {
                    ingredient_name: {
                        'measure': i['measure'],
                        'quantity': i['quantity'] * person_count
                    }
                }
                counted_list.update(count)
    return counted_list
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))