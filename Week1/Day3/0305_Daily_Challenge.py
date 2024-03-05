#challenge_1
word = input("Enter a word: ")
indexes_dict = {}
for index, letter in enumerate(word):
    if letter not in indexes_dict:
        indexes_dict[letter] = []
    indexes_dict[letter].append(index)
print(indexes_dict)

#challenge_2
items_purchase = { "Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = input("How much money do you have?")
products = []
costs = []
my_list = []
def clean_items(w):
    return float(w.strip().replace("$", "").replace(",", ""))

for x,y in items_purchase.items():
    products.append(x)
    costs.append(clean_items(y))

new_item_purchase = dict(zip(products, costs))

wallet = clean_items(wallet)

for item, i in new_item_purchase.items():
    if wallet > float(i):
        my_list.append(item)
        wallet -= float(i)

if len(my_list) == 0:
    print('Nothing')
else:
    my_list.sort()
    print(my_list)
