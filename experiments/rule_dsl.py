rules = []
def win(name):
    def wrap(f):
        rules.append((name,f))
    return wrap

@win('wolf')
def if_exceed_villager(xs):
    # fox is villager, or not?
    return (len([x for x in xs if x == 'wolf']) >=
            len([x for x in xs if x == 'villager']))

@win('villager')
def otherwise(xs):
    return True

def win(xs):
    """
>>> win(['wolf','wolf'])
'wolf'

>>> win(['villager','villager'])
'villager'

>>> win(['wolf','villager'])
'wolf'

>>> win(['wolf','villager','villager'])
'villager'
    """
    for (role,cond) in rules:
        if cond(xs):
            return role

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
