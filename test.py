from clear_inputs import clear_inputs
from filter_data import filter_data

clear_inputs_test_cards = [
    {
        'inputs': {'manufacturer': '', 'min_price': '4000', 'max_price': '', 'min_memory_interface_bit': '',
                   'max_memory_interface_bit': '', 'min_gpu_mgh': '', 'max_gpu_mgh': '', 'is_sold': '',
                   'is_nvidia_family': ''},
        'cleared': {'manufacturer': None, 'min_price': 4000, 'max_price': None, 'min_memory_interface_bit': None,
                    'max_memory_interface_bit': None, 'min_gpu_mgh': None, 'max_gpu_mgh': None, 'is_sold': None,
                    'is_nvidia_family': None}
    },
    {
        'inputs': {'manufacturer': 'G', 'min_price': '4000', 'max_price': '10000', 'min_memory_interface_bit': '',
                   'max_memory_interface_bit': '', 'min_gpu_mgh': '', 'max_gpu_mgh': '', 'is_sold': '',
                   'is_nvidia_family': '1'},
        'cleared': {'manufacturer': 'G', 'min_price': 4000, 'max_price': 10000, 'min_memory_interface_bit': None,
                    'max_memory_interface_bit': None, 'min_gpu_mgh': None, 'max_gpu_mgh': None, 'is_sold': None,
                    'is_nvidia_family': True}
    },
    {
        'inputs': {'manufacturer': 'M', 'min_price': '4000', 'max_price': '', 'min_memory_interface_bit': '',
                   'max_memory_interface_bit': '', 'min_gpu_mgh': '', 'max_gpu_mgh': '', 'is_sold': '0',
                   'is_nvidia_family': '0'},
        'cleared': {'manufacturer': 'M', 'min_price': 4000, 'max_price': None, 'min_memory_interface_bit': None,
                    'max_memory_interface_bit': None, 'min_gpu_mgh': None, 'max_gpu_mgh': None, 'is_sold': False,
                    'is_nvidia_family': False}
    },
]

for test_case in clear_inputs_test_cards:
    try:
        assert clear_inputs(test_case['inputs']) == test_case['cleared'], 'clear_inputs failed'
    except AssertionError as e:
        print('inputs', test_case['inputs'])
        print('expected cleared', test_case['cleared'])
        import time

        time.sleep(0.01)
        raise e

cards = [{'manufacturer': 'MSI', 'model': 'GTX', 'model_number': 1000, 'gpu_mgh': 1183, 'memory_interface_bit': 128,
          'gpu_memory_mb': 2048, 'price': 3500,
          'is_sold': False, 'nvidia_graphics_family': True}, ]
assert filter_data(cards, {'min_price': 1,
                           'max_price': 10,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == []
assert filter_data(cards, {'min_price': 1,
                           'max_price': 10000,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': 200,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == cards
assert filter_data(cards, {'min_price': 1,
                           'max_price': 10,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == []
assert filter_data(cards, {'min_price': None,
                           'max_price': None,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == cards
assert filter_data(cards, {'min_price': None,
                           'max_price': None,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': 1000,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == cards
assert filter_data(cards, {'min_price': 1000,
                           'max_price': 10000,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == cards
assert filter_data(cards, {'min_price': 1000,
                           'max_price': 40,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': 'MSI', }) == []

cards = [{'manufacturer': 'Asus', 'model': 'GTX', 'model_number': 1040, 'gpu_mgh': 1283, 'memory_interface_bit': 192,
          'gpu_memory_mb': 4096, 'price': 4500,
          'is_sold': False, 'nvidia_graphics_family': True},
         {'manufacturer': 'Gigabyte', 'model': 'GTX', 'model_number': 1050, 'gpu_mgh': 1383,
          'memory_interface_bit': 256,
          'gpu_memory_mb': 6144, 'price': 8500,
          'is_sold': False, 'nvidia_graphics_family': True}, ]
assert filter_data(cards, {'min_price': None,
                           'max_price': None,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': None, }) == cards
assert filter_data(cards, {'min_price': 1,
                           'max_price': 10,
                           'min_memory_interface_bit': None,
                           'max_memory_interface_bit': None,
                           'min_gpu_mgh': None,
                           'max_gpu_mgh': None,
                           'is_sold': None,
                           'is_nvidia_family': None,
                           'manufacturer': None, }) == []
