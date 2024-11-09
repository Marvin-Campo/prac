def game_mistakes(category, seq):
    if seq == ():
        return (0,0)
    used_words = set()
    alice = 0
    bob = 0
    if seq[0] in category:
        used_words.add(seq[0])
    else:
        alice += 1
    for i in range(1,len(seq)):
        if seq[i] not in category:
            if i%2 == 0:
                alice += 1
            else:
                bob += 1
        elif seq[i] in used_words:
            if i%2 == 0:
                alice += 1
            else:
                bob += 1
        else: 
            used_words.add(seq[i])
            if seq[i-1][-1] != seq[i][0]:
                if i%2 == 0:
                    alice += 1
                else:
                    bob += 1
    return (alice,bob)

assert game_mistakes((
    'porkchop', 'kanin', 'ketchup', 'chopsuey', 'bulalo', 'adobo',
    'chicken', 'mami', 'longsilog', 'tocilog', 'tapsi', 'pancit',
    'lugaw', 'lomi', 'tokwatbaboy', 'paresbeef', 'friedsiomai',
    'siopao', 'burger', 'avocado', 'gulaman', 'apple', 'spaghetti',
    'taho', 'nut', 'croissant', 'linguine', 'pineapple', 'kutsinta',
    'edamame', 'hazelnut', 'yema', 'tinapay', 'durian', 'pizza',
    'orange', 'iodizedsalt', 'tea', 'eggplant', 'puto', 'legumes',
    'oatmeal', 'noodles', 'tofu', 'nutella', 'egg', 'udon', 'sago',
), (
    'pizza', 'apple', 'egg', 'hazelnut', 'tofu', 'udon', 'nut',
    'tinapay', 'yema', 'edamame', 'eggplant', 'durian', 'nutella',
    'avocado', 'orangutan', 'noodles', 'spaghetti', 'iodizedsalt',
    'toatmeal', 'linguine', 'egg', 'gulaman', 'nut', 'tea', 'uh',
)) == (5, 3)