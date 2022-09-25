import basics, time, random, attributes as att, inventory as inv, copy, re, os
from pathlib import Path
try:
    os.makedirs('./save')
except FileExistsError:   #save directory already exists
    pass
basics.intro_dots()
basics.slow_text('"Greetings, traveller! You must be tired from your day on the road. Welcome to the Tavern of the Setting Sun!"\n')
time.sleep(.5)
basics.slow_text('The man behind the counter eyes you with a friendly - and most likely pretty business minded - smile.\n')
time.sleep(.5)
basics.slow_text('Before you can properly answer, introduce yourself, and potentially get into some adventure, let us first determine who you are.')
name_check = 'N'
while name_check != 'Y':
    name = re.sub("\s\s+" , " ", input('What is your name?\n').strip()) # getting the name with no more than 1 consecutive space within, no spaces at the start or end
    name_check = input(f'You entered {name} for your name - is this correct? (Y/N)\n').strip().upper()
basics.slow_text(f'{name} - now that is a proper name for an adventurer! What might be your profession?')
fighter = rogue = wizard = cleric = False #assigning class and setting up the basics for inventory, spells & relations
spells_known = {'Healing(light)': '7 mana'}
backpack = {'bedroll': 1, 'rope(15ft)': 1, 'torch': 2}
ranged_weapon = 'dart'
melee_weapon = 'fist'
armor = 'clothing'
coins = random.randint(10,50)
money = {'gold coins': coins}
relations = {}
melee_stats = {'fist': '1d3', 'dagger': '1d4+1', 'shortsword': '1d6+1', 'longsword': '1d8+1', 'mace': '2d4', 'two-handed sword': '1d10+1'}
ranged_stats = {'dart': '1d3', 'sling': '1d4+1', 'shortbow': '1d6+1', 'longbow': '1d8+1', 'light crossbow': '2d4', 'heavy crossbow': '2d6'}
armor_class = {'clothing': '1', 'wizard robes': '2', 'stutted leather': '4', 'chainmail': '6', 'half plate': '8', 'full plate': '10'}
while fighter == False and rogue == False and wizard == False and cleric == False:
    basics.slow_text('Enter your choice from the following list of available classes - Fighter, Rogue, Cleric or Wizard:')
    adventurer = re.sub("\s\s+" , "", input().strip().lower().capitalize()) #stripping input of all spaces, getting it case insensitive
    if adventurer == 'Fighter' or adventurer == 'Ranger' or adventurer == 'Warlock' or adventurer == 'Paladin':
        fighter = True
        if adventurer != 'Warlock':
            ranged_weapon = 'longbow'
            melee_weapon = 'longsword'
            worn_armor = 'chainmail'
            spells_known['Illuminate'] = '5 mana'
        if adventurer == 'Paladin':
            ranged_weapon = 'light crossbow'
            melee_weapon = 'two-handed sword'
            worn_armor = 'half plate'
            backpack['healing potion'] = 2
    if adventurer == 'Rogue' or adventurer == 'Bard' or adventurer == 'Ranger':
        rogue = True
        if adventurer != 'Ranger':
            backpack['lockpick'] = 3
            ranged_weapon = 'shortbow'
            melee_weapon = 'shortsword'
            worn_armor = 'stutted leather'
            spells_known['Illuminate'] = '5 mana'
        if adventurer == 'Bard':
            spells_known['Healing(medium)'] = '12 mana'
    if adventurer == 'wizard' or adventurer == 'Bard' or adventurer == 'Warlock':
        wizard = True
        backpack['mana potion'] = 3
        if adventurer != 'Bard':
            ranged_weapon = 'sling'
            melee_weapon = 'dagger'
            worn_armor = 'wizard robes'           
            spells_known['Illuminate'] = '5 mana'
            spells_known['Knock-Knock'] = '10 mana'
            spells_known['Firebolt'] = '10 mana'
            spells_known['Healing(medium)'] = '12 mana'
        else:
            backpack['mana potion'] = 2
    if adventurer == 'Cleric' or adventurer == 'Druid' or adventurer == 'Paladin':
        cleric = True
        backpack['mana potion'] = 2
        spells_known['Healing(medium)'] = '12 mana'
        spells_known['Holy Smite'] = '10 mana'
        if adventurer != 'Paladin':
            ranged_weapon = 'sling'
            melee_weapon = 'mace'
            backpack['healing potion'] = 3
            spells_known['Healing(strong)'] = '15 mana'
            spells_known['Bless'] = '5 mana'
            if adventurer == 'Druid':
                ranged_weapon = 'light crossbow'
                worn_armor = 'stutted leather'
                spells_known['Holy Smite'] = '15 mana'
                spells_known['Healing(medium)'] = '11 mana'
                spells_known['Healing(strong)'] = '13 mana'
            else:
                worn_armor = 'chainmail'            
weapons = {str(ranged_weapon): str(ranged_stats[ranged_weapon]), str(melee_weapon): str(melee_stats[melee_weapon])}
armor = {str(worn_armor): str(armor_class[worn_armor])} 
complete_inventory = (backpack, money, weapons, armor, spells_known)
basics.slow_text(f'''Oh, so you are a {adventurer}! Your kind is most likely rather rare around here, but be asured you will be welcome nonetheless!
Now let us find out about your skills - I hope you have some dice around? They are an important tool for any proper adventurer, you know?
Let me quickly explain - you have a couple of attributes that determine how well you might be doing with various tasks.
Those attributes are Strength, Dexterity, Toughness, Intellect, Charisma and Willpower.
No matter what method you choose, your final attributes might or might not change during the character creation.\n''')
primary_attributes = {'Strength': 0, 'Dexterity': 0, 'Toughness': 0, 'Intellect': 0, 'Charisma': 0, 'Willpower': 0} #defining the attributes
    #method of generating the attributes
random = False
dice = False
while True:
    method = re.sub("\s\s+" , "", input('Would you like to roll the dice yourself - or do you trust the random generator with your attributes? Enter "dice" or "random":\n').strip().lower())
    if 'dice' in method:
        dice = True
        break
    if 'rand' in method:
        random = True
        break
if random == True:
    basics.slow_text('So we are feeling lucky with the randomizer - great!')
    while True:
        att.calculate_attributes_random(primary_attributes)
        basics.slow_text('Do you accept these attributes or do you want to randomize again? Type "accept" or "reroll" to continue.')
        while True:
            rand_check = re.sub("\s\s+" , "", input())
            if rand_check == "accept":
                accept = True
                break
            elif rand_check == "reroll":
                accept = False
                break
            else:
                basics.slow_text('Please enter "accept" or "reroll" to continue.')
                continue
        if accept == True:
            break
else:
    att.calculate_attributes_rolling(primary_attributes) #
if fighter == True and wizard != True and primary_attributes['Strength'] < 10: #adjusting attributes by class
    primary_attributes['Strength'] += 6
if rogue == True and primary_attributes['Dexterity'] < 10:
    primary_attributes['Dexterity'] += 6
if wizard == True and fighter != True and primary_attributes['Intellect'] < 10:
    primary_attributes['Intellect'] += 6
#enabling special attributes
secondary_attributes = {'strong': (primary_attributes['Strength'] > 12), 'nimble': (primary_attributes['Dexterity'] > 12), 'tough': (primary_attributes['Toughness'] > 12),
                        'clever': (primary_attributes['Intellect'] > 12), 'charming': (primary_attributes['Charisma'] > 12), 'ironwilled': (primary_attributes['Willpower'] > 12)}
#derived attributes
hitpoints = primary_attributes['Strength'] // 2 + primary_attributes['Toughness'] * 2
if fighter == True and wizard != True:
    hitpoints = hitpoints // 2 * 3
mana = primary_attributes['Intellect'] // 2 + primary_attributes['Willpower'] *2
if wizard == True or cleric == True and fighter != True:
    mana = mana // 2 * 3
combat_values = [primary_attributes, hitpoints, mana, armor, weapons]
basics.slow_text('So, let me summarize once more:\n')
basics.slow_text(f'You are {name}, the {adventurer}, and your attributes are:')
att.check_attributes(primary_attributes)
att.check_special(secondary_attributes)
basics.slow_text('\nAt the moment you have your current maximum of ' + str(hitpoints) + ' health and ' + str(mana) + ' mana.')
inv.display_inventory(backpack, money)
inv.weapon_check(weapons)
inv.armor_check(armor)
inv.listing_of_spells(spells_known)
basics.slow_text('\nNow it is time to actually get into your adventure, am I right? The man behind the counter, you remember?')
time.sleep(1)
basics.slow_text('''He is still looking at you, his smile ever so friendly, but you can tell from a little twitch in the corner of his left eye that he is\nstarting to get irritated by your long silence.\n
"So....", he begins, letting his word hang in the air between the both of you as if only waiting for you to finally take it (figuratively\nspeaking) and come forth with some words of your own.
You quickly clear your throat, waking from your stasis of character generation to answer.''')
if secondary_attributes['charming'] == True:
    basics.slow_text(f'"Oh, pardon me, good Sir, the day has been a long one, and I needed a few moments to catch myself. The name is {name}, I am a travelling \n{adventurer}, looking for a warm place for the night - and perhaps a hot meal and a good drink", you smoothly reply, widening the smile on the \nface of the innkeeper.')
    inv.relationship_increase(relations, 'the innkeeper')
else:
    basics.slow_text(f'"Oh, I am sorry - the day on the road was long, I needed a few moments to breath through. I am {name}, a travelling {adventurer} - would \nyou have a warm place for the night, and a meal and drink with it?", you hastily reply, noticing the innkeeper smiling even more welcoming \nat your words.\n')
basics.slow_text('AND you made it through this first part of what might become a bigger thing in the future. Enter EXIT to exit.')
ending = input().upper()
while ending != 'EXIT':
    basics.slow_text('Enter EXIT to exit.')
    ending = input().upper()
basics.slow_text('Goodbye!')
