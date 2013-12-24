import itertools

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    rank_selection = '23456789TJQKA'
    b_list = []
    r_list = []
    suit_b = 'SC'
    wild_b = itertools.product(rank_selection, suit_b)
    for (r, f) in wild_b:
        b_list.append(r + f)
    suit_r = 'HD'
    wild_r = itertools.product(rank_selection, suit_r)
    for (r, f) in wild_r:
        r_list.append(r + f)

    result_list = []
    num_b = hand.count('?B')
    num_r = hand.count('?R')
    if num_b == 1 and num_r == 0:
        hand.remove('?B')
        for stuff in b_list:
            newlist = hand + [stuff]
            result_list.append(newlist)
    elif num_b == 0 and num_r == 1:
        hand.remove('?R')
        for stuff in r_list:
            newlist = hand + [stuff]
            result_list.append(newlist)
    elif num_b == 1 and num_r == 1:
        hand.remove('?B')
        hand.remove('?R')
        two_jokers = itertools.product(b_list, r_list)
        for (b, r) in two_jokers:
            newlist = hand + [b] + [r]
            result_list.append(newlist)
    else:
        result_list = [hand]

    best, score = [], None

    for possible_hand in result_list:
        possible = itertools.combinations(possible_hand, 5)
        for t in possible:
            t_score = hand_rank(t)
            if t_score > score:
                score = t_score
                best = t

    return best

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has
    exactly n-of-a-kind of. Return None if there
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'