thoughts = []

def get_user_selection():
    print('options 1,2 or 3')
    user_selection = input('please input 1,2 or 3:  ')
    return user_selection

def thought_ask():
    thought = input('Enter your thought: ')
    thoughts.append(thought)

def print_thought():
    for thought in thoughts:
        print(thought)


def continue_ask():
    while(True):
        user_selection = get_user_selection()
        if(user_selection == '1'):
            thought_ask()
        elif(user_selection == '2'):
            print_thought()
        elif(user_selection == '3'):
            print('goodbye')
            return

continue_ask()
    

 


