

def is_card_suitable(card, clear_dict):
    if clear_dict['manufacturer'] is not None:
        if not clear_dict['manufacturer'] in card['manufacturer']:
            return False
    if clear_dict['min_price'] is not None:
        if clear_dict['min_price'] > card['price']:
            return False
    if clear_dict['max_price'] is not None:
        if clear_dict['max_price'] < card['price']:
            return False
    if clear_dict['min_memory_interface_bit'] is not None:
        if clear_dict['min_memory_interface_bit'] > card['memory_interface_bit']:
            return False
    if clear_dict['max_memory_interface_bit'] is not None:
        if clear_dict['max_memory_interface_bit'] < card['memory_interface_bit']:
            return False
    if clear_dict['min_gpu_mgh'] is not None:
        if clear_dict['min_gpu_mgh'] > card['gpu_mgh']:
            return False
    if clear_dict['max_gpu_mgh'] is not None:
        if clear_dict['max_gpu_mgh'] < card['gpu_mgh']:
            return False
    if clear_dict['is_sold'] is not None:
        if clear_dict['is_sold'] != card['is_sold']:
            return False
    if clear_dict['is_nvidia_family'] is not None:
        if clear_dict['is_nvidia_family'] != card['nvidia_graphics_family']:
            return False
    return True
