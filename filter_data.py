from suitable import is_card_suitable

def filter_data(cards, clear_dict):
    final_list = []
    for card in cards:
        if is_card_suitable(card, clear_dict):
            final_list.append(card)
    return final_list
