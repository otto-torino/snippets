# A ⟷ B

def iif(a, b):
    return ~(bool(a) ^ bool(b))

# A ⟶ B

def imply(a, b):
    return not bool(a) or bool(b)
