def generate(k, global_lst=[], lst=['0:0'], win=0, lose=0):
    
    if win == lose == 0:
        global_lst = []

    if win == k or lose == k:
        return lst

    if win < k:
        global_lst.append(generate(k, global_lst, lst + [f'{win+1}:{lose}'], win+1, lose))

    if lose < k:
        global_lst.append(generate(k, global_lst, lst + [f'{win}:{lose+1}'], win, lose+1))
    
    if win == lose == 0:
        return list(filter(None, global_lst))

generate_all_possible_matches = generate