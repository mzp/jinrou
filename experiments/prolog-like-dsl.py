# -*- coding:utf-8 -*-
class Goal(object):
    def __init__(self):
        self.tails = []

    def __call__(self, name):
        class _Goal:
            def __lshift__(_, conds):
                self.tails.append((name,conds))
        return _Goal()

    def satisfy(self, xs):
        for (name,conds) in self.tails:
            if all(map(lambda c: c(xs), conds)):
                return name

class Role(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "<Role(%s)>" % self.name

class Player(object):
    def __init__(self, name, role):
        self.name = name
        self.role = role

# util
def exceed(role):
    def _exceed(xs):
        matched = len(filter(lambda x: x.role == role,xs))
        return len(xs) < 2 * matched
    return _exceed

def exists(role):
    return lambda xs : role in map(lambda x: x.role,xs)

def no(f):
    return lambda xs : not f(xs)

def true():
    return lambda _ : True

# ------------------------------------------------------------
# 役割(role)の定義
# 人狼
wolf     = Role('wolf')

# 村人
villager = Role('villager')

# ------------------------------------------------------------
# 勝利条件の記述開始
win = Goal()

# wolfの勝利条件は、村の大半を占めること
win(wolf)     << (exceed(wolf),)

# villagerの勝利条件は、wolfが存在しなくなること
win(villager) << (no(exists(wolf)),)

# ------------------------------------------------------------
if __name__ == '__main__':
    p1 = Player('player a',wolf)
    p2 = Player('player b',wolf)
    p3 = Player('player c',villager)
    p4 = Player('player d',villager)
    p5 = Player('player e',villager)
    p6 = Player('player f',villager)
    p7 = Player('player g',villager)

    print win.satisfy([p1,p2,p3,p4,p5,p6,p7]) # => None
    print win.satisfy([p1,p2,p3]) # => wolf
    print win.satisfy([p3]) # => villager
