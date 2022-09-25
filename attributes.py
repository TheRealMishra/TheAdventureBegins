def calculate_attributes_random(attributes):
    import random, time, basics
    for k in attributes:
        attributes[k] = random.randint(5, 18)
        if attributes[k] < 8:
            basics.slow_text('I rolled ' + str(attributes[k]) + ' for your ' + k + ' - could be worse, I guess?')
        elif attributes[k] < 13:
            basics.slow_text('I got a solid ' + str(attributes[k]) + ' for your ' + k + ' - not bad!')
        else:
            basics.slow_text('Your ' + k + ' is an impressive ' + str(attributes[k]) + ' - outstanding!')
        time.sleep(.3)
def calculate_attributes_rolling(attributes):
    import basics
    basics.slow_text('For each attribute, you will need to roll 3d6 and enter the total sum of all three dice - so you will have values between 3 and 18.')
    for k in attributes:
        raw = input('Let\'s roll your ' + str(k) + ' with 3d6:\n')
        while raw.isdecimal() != True or int(raw) < 3 or int(raw) > 18:
            raw = input('You must enter a number between 3 and 18 for your attributes.\n')
        attributes[k] = int(raw)
        if attributes[k] < 8:
            basics.slow_text('That makes your ' + k + ' score for now a mediocre ' + str(attributes[k]) + ' - could be worse, I guess?')
        elif attributes[k] < 13:
            basics.slow_text('That makes your ' + k + ' score for now a total of ' + str(attributes[k]) + ' - not bad!')
        else:
            basics.slow_text('Your ' + k + ' currently is an impressive ' + str(attributes[k]) + ' - outstanding!')
def check_attributes(attributes):
    import basics
    for k, v in attributes.items():
        basics.slow_text('  ' + k.ljust(10) + str(v).rjust(3))
def check_special(attributes):
    import basics
    basics.slow_text('You have the following special traits:')
    ind = '  '
    for k, v in attributes.items():
        if v == True:            
            basics.slow_text(ind + k.ljust(10))
            ind += ' '
