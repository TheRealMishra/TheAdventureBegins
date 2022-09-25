def intro_dots():
    WIDTH = 140
    HEIGHT = 2
    x = 0
    y = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print('.' , end='')
            x = x+1
        print()
def slow_text(s):
    import sys, time
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.03)
