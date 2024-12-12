import utils


items = []
count = 0
rules, updates = utils.get_data()

for update in updates:
    if not utils.is_valid(update, rules):
        items.append(update)

for item in items:
    count += utils.get_middle_item(utils.get_fixed(item, rules))

print(count)
