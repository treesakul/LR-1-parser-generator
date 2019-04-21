def parser(table, string):
    stack = ['$',0]
    input_string = string+'$'
    input_index = 0
    table = {0: {'c': ('s', 1), 'd': ('s', 2), 'S': ('s', 3), 'C': ('s', 4), "S'": ('', 'accept')}, 1: {'c': ('s', 1), 'd': ('s', 2), 'C': ('s', 5)}, 2: {'d': ('r', ('C', ('d',))), 'c': ('r', ('C', ('d',)))}, 3: {'$': ('r', ("S'", ('S',)))}, 4: {'c': ('s', 6), 'd': ('s', 7), 'C': ('s', 8)}, 5: {'d': ('r', ('C', ('c', 'C'))), 'c': ('r', ('C', ('c', 'C')))}, 6: {'c': ('s', 6), 'd': ('s', 7), 'C': ('s', 9)}, 7: {'$': ('r', ('C', ('d',)))}, 8: {'$': ('r', ('S', ('C', 'C')))}, 9: {'$': ('r', ('C', ('c', 'C')))}}
    start_symbol = "S'"
    while stack[-1] != 'accept':
        print(stack)
        current_state = stack[-1]
        if input_string[input_index] not in table[current_state]:
            # reject the string
            print('reject')
            break
        action, goto = table[current_state][input_string[input_index]]
        if action == 's':
            stack.append(input_string[input_index])
            stack.append(goto)      
            input_index += 1
        elif action == 'r':
            new_symbol, RHS = goto
            for item in RHS:
                stack.pop() # state number
                stack.pop() # symbol
            stack.append(new_symbol)
            if new_symbol not in table[stack[-2]]:
                # reject the string
                print('reject')
                break
            _, goto = table[stack[-2]][new_symbol]
            stack.append(goto)    
    if stack[-1] == 'accept':
        print('accept')
