calls = 0

def count_calls (calls):
    global calls
    calls += 1
    count_calls()
    calls = string_info + is_contains
    print(calls)


def string_info (string):
    count_calls()
    return (tuple(len(string),(string.upper()),(string.lower())))



def is_contains (string,list_to_search):
    count_calls()
    if string in list_to_search == True:
        return True
    else:
        return False
    print(is_contains())


print(calls)






















