def is_rich(amount):
    if amount > 30000:
        return True
    else:
        return False

def get_notation(proba_non_payment):
    if proba_non_payment > 0.8:
        return 'C'
    elif proba_non_payment > 0.5:
        return 'B'
    else:
        return 'A'
