from pprint import pprint
from cards import cards
from clear_inputs import clear_inputs
from filter_data import filter_data
from inputs import get_inputs


def main():
    inp_dict = get_inputs()
    clear_dict = clear_inputs(inp_dict)
    final_list = filter_data(cards, clear_dict)
    pprint(final_list)


if __name__ == '__main__':
    main()
