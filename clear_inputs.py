def clear_inputs(inp_dict):
    clear_dict = {
        'min_price': None,
        'max_price': None,
        'min_memory_interface_bit': None,
        'max_memory_interface_bit': None,
        'min_gpu_mgh': None,
        'max_gpu_mgh': None,
        'is_sold': None,
        'is_nvidia_family': None,
        'manufacturer': None,
    }

    row_manufacturer = inp_dict['manufacturer']
    if row_manufacturer:
        clear_dict['manufacturer'] = row_manufacturer

    row_min_price = inp_dict['min_price']
    if row_min_price:
        if not row_min_price.isdigit():
            raise ValueError
        clear_dict['min_price'] = int(row_min_price)

    row_max_price = inp_dict['max_price']
    if row_max_price:
        if not row_max_price.isdigit():
            raise ValueError
        clear_dict['max_price'] = int(row_max_price)

    min_row_memory_interface_bit = inp_dict['min_memory_interface_bit']
    if min_row_memory_interface_bit:
        if not min_row_memory_interface_bit.isdigit():
            raise ValueError
        clear_dict['min_memory_interface_bit'] = int(min_row_memory_interface_bit)

    max_row_memory_interface_bit = inp_dict['max_memory_interface_bit']
    if max_row_memory_interface_bit:
        if not max_row_memory_interface_bit.isdigit():
            raise ValueError
        clear_dict['max_memory_interface_bit'] = int(max_row_memory_interface_bit)

    min_row_gpu_mgh = inp_dict['min_gpu_mgh']
    if min_row_gpu_mgh:
        if not min_row_gpu_mgh.isdigit():
            raise ValueError
        clear_dict['min_gpu_mgh'] = int(min_row_gpu_mgh)

    max_row_gpu_mgh = inp_dict['max_gpu_mgh']
    if max_row_gpu_mgh:
        if not max_row_gpu_mgh.isdigit():
            raise ValueError
        clear_dict['max_gpu_mgh'] = int(max_row_gpu_mgh)

    row_is_sold = inp_dict['is_sold']
    if row_is_sold:
        if not (row_is_sold == '0' or row_is_sold == '1'):
            raise ValueError
        clear_dict['is_sold'] = bool(int(row_is_sold))

    row_is_nvidia_family = inp_dict['is_nvidia_family']
    if row_is_nvidia_family:
        if not (row_is_nvidia_family == '0' or row_is_nvidia_family == '1'):
            raise ValueError
        clear_dict['is_nvidia_family'] = bool(int(row_is_nvidia_family))

    return clear_dict
