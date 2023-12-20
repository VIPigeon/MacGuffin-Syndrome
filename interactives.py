
funcs = {}


def snow(moving):
    moving.addText("*скрип снега*")
    moving.status = 'freeze'


funcs[','] = snow


def border(moving):
    ...
funcs['_'] = border
funcs['-'] = border
funcs['|'] = border

