# Python3
import keyboard

# The dict for abbr
abbr = {
    'pp': ['\\frac{\\partial{}}{\\partial{}}', 14],
    'pp2':['\\frac{\\partial^{2}{}}{\\partial{}^{2}}', 18],
    'ff': ['\\frac{}{}', 3],
}

def replace_and_move(rp, back_num):
    keyboard.write(rp)
    for _ in range(back_num):
        keyboard.send(75)

def add_abbr(source_text, replacement):
    # implement of add_abbreviation
    rp = '\b'*(len(source_text)+1) + replacement[0]
    callback = lambda: replace_and_move(rp, replacement[1])
    return keyboard.add_word_listener(source_text, callback, match_suffix=False, timeout=1)

for source_text, replacement in abbr.items():
    add_abbr(source_text, replacement)

print('Helper is running now...')
keyboard.wait('alt+`')
