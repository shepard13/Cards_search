
def get_inputs():
    inp_dict = {}
    inp_dict['min_price'] = input('Enter min price: ')
    inp_dict['max_price'] = input('Enter max price: ')
    inp_dict['min_memory_interface_bit'] = input('Enter the min interface of memory bit: ')
    inp_dict['max_memory_interface_bit'] = input('Enter the max interface of memory bit: ')
    inp_dict['min_gpu_mgh'] = input('Enter the min GPU mgh: ')
    inp_dict['max_gpu_mgh'] = input('Enter the max GPU mgh: ')
    inp_dict['is_sold'] = input('Enter the status of cards: ')
    inp_dict['is_nvidia_family'] = input('Enter the family of cards Nvidia of AMD: ')
    return inp_dict
