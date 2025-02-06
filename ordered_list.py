def get_ordered_list(lst=None):
    if lst is None:
        user_input_input('Enter a list of integers (comma-separated):')
        lst = [int(num.strp()) for num in user_input.split(',')]
    return sorted(lst)
    