# imports
from terminaltables import AsciiTable
from colorama import init, Fore, Back, Style

init()

# globals
tableData = [["Item", "Amount", "Status"]]

# contains the number of clothing I should need, depending on how many days I go
clothingTemplate = {
    "shoes": 0,
    "socks": 1,
    "boxer": 1,
    "pants": 0.5,
    "shirts": 1,
    "pyjama pants": 0.5,
    "pyjama shirts": 0.65,
    "jacket": 0,
    "masks": 2,
}

hygiene = {
    "toothbrush": 1,
    "toothpaste": 1,
    "razor": 1,
    "shaving cream": 1,
    "shampoo": 1,
    "body wash": 1,
    "deodorant": 1,
    "q-tip": 1,
    "ear scraper": 1,
}

electronics = {
    "laptop": 1,
    "laptop charger": 1,
    "phone": 1,
    "phone charger": 1,
    "kindle": 1,
    "kindle charger": 1,
    "earphones": 1,
}

medication = {
    "benadryl": 1,
    "tylenol": 1,
    "nose medication": 1,
    "asthma medication": 1,
}

essentials = {
    "glasses": 1,
    "epipen": 1,
    "wallet": 1,
    "passport": 1,
    "water bottle (no liquid)": 1,
    "casual bag": 1,
}

# functions

# calculate number of clothing items
def clothing_items(travelDays):
    clothing = {}
    for key, val in clothingTemplate.items():
        if val == 0:
            clothing[key] = 1
        else:
            clothing[key] = round(val * travelDays)

    return clothing

def validate(item):
    res = input("{} (y/n) : ".format(item))
    if res == "y":
        return True
    else:
        return False

def question(section, mapping):
    print(Fore.YELLOW + section + Style.RESET_ALL)
    tableData.append([Fore.YELLOW + "* {}".format(section),"","" + Style.RESET_ALL])
    for key, val in mapping.items():
        if validate("{} {}".format(val, key)):
            tableData.append([key, val, Fore.GREEN + str(True) + Style.RESET_ALL])

        else:
            tableData.append([key, val, Fore.RED + str(False) + Style.RESET_ALL])

travelDays = int(input("how many days will you be traveling : "))

question("clothing", clothing_items(travelDays))
question("hygiene", hygiene)
question("electronics", electronics)
question("medication", medication)
question("essentials", essentials)

ttable = AsciiTable(tableData)
print(ttable.table)
