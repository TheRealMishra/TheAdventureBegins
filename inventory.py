melee_stats = {'fist': '1d3', 'dagger': '1d4+1', 'shortsword': '1d6+1', 'longsword': '1d8+1', 'mace': '2d4', 'two-handed sword': '1d10+1'}
ranged_stats = {'dart': '1d3', 'sling': '1d4+1', 'shortbow': '1d6+1', 'longbow': '1d8+1', 'light crossbow': '2d4', 'heavy crossbow': '2d6'}
armor_class = {'clothing': '1', 'wizard robes': '2', 'stutted leather': '4', 'chainmail': '6', 'half plate': '8', 'full plate': '10'}
def display_inventory(inventory, money):
    import basics
    basics.slow_text('\nIn your inventory you find the following:')
    for k, v in inventory.items():
        basics.slow_text(str(v).rjust(5) + 'x ' + k)
    for k, v in money.items():
        basics.slow_text(str(v).rjust(5) + 'x ' + k)
def listing_of_spells(spells_):
    import basics
    basics.slow_text('\nYour magic abilities allow you to cast the following spells:')
    for k, v in spells_.items():
        basics.slow_text('   ' + k.ljust(20) + (v + ' per cast').rjust(17))
def add_loot_to_inventory(inventory, items_to_add):
    for loot in items_to_add:
        inventory.setdefault(loot, 0)
        inventory[loot] += items_to_add[loot]
    return(inventory)
def relationship_increase(rel, person):
    import basics
    rel.setdefault(person, 0)
    rel[person] += 1
    basics.slow_text(' = Your relationship with ' + person + ' has increased to ' + str(rel.get(person)) + '. = ')
def weapon_check(weapon):
    import basics
    print()
    for k, v in weapon.items():
        if k in melee_stats:
            basics.slow_text('Your current melee weapon is a ' + k + ', dealing ' + v + ' points of damage per hit.')
        if k in ranged_stats:
            basics.slow_text('Your current ranged weapon is a ' + k + ', dealing ' + v + ' points of damage per hit.')
def armor_check(armor):
    import basics
    for k, v in armor.items():
        basics.slow_text('You are currently wearing ' + k + ', giving you ' + v + ' points of protecction.')
