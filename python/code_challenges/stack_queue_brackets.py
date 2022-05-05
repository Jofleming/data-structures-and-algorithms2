from data_structures.stack import Stack


def multi_bracket_validation(string):
    checking_stack = Stack()

    for char in string:
        if (char == '(' or char == '{' or char == '['):
           checking_stack.push(char) 
        if char == ')':
            if checking_stack.is_empty() == True:
                return False
            if checking_stack.peek() == '(':
                checking_stack.pop()
            else:
                return False
        if char == '}':
            if checking_stack.is_empty() == True:
                return False
            if checking_stack.peek() == '{':
                checking_stack.pop()
            else:
                return False
        if char == ']':
            if checking_stack.is_empty() == True:
                return False
            if checking_stack.peek() == '[':
                checking_stack.pop()
            else:
                return False
    return checking_stack.is_empty()
