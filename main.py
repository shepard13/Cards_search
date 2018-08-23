
from cards import cards
from clear_inputs import clear_inputs
from filter_data import filter_data
from inputs import get_inputs
from show_item import show_item
def main():
    while True:
        inp_dict = get_inputs()
        try:
            clear_dict = clear_inputs(inp_dict)
        except ValueError:
            print('________________________________')
            print('Value incorrect please try again')
            print('________________________________')
            continue
        else:
            final_list = filter_data(cards, clear_dict)
            final_str = show_item(final_list)
            print('\n'.join(final_str))
        break
if __name__ == '__main__':
    main()
