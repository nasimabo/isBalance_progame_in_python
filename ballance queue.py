
"""def isBalance(input_str):
    stack = []

    for ch in input_str:
        if ch in ["(","{","["]:
            stack.append(ch)
        else:
            if not stack:
                return False
            current_value = stack.pop()
            if current_value == "(":
                if ch != ")":
                    return False
            
            if current_value == "{":
                if ch != "}":
                    return False
            
            if current_value == "[":
                if ch != "]":
                    return False

    if stack:
        return False
    else:
        return True

input_str = input("Enter this ballance")
result = isBalance(input_str)
print(result)"""


def isBalance(input_str):
    stack = []

    for ch in input_str:
        if ch in ["(","{","["]:
            stack.append(ch)
        else:
            if not stack:
                return False
            current_str = stack.pop()
            if current_str == "(":
                if ch != ")":
                    return False
            if current_str == "{":
                if ch != "}":
                    return False
            if current_str == "[":
                if ch != "]":
                    return False


    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    input_str = input("Enter this Balance")
    #result = isBalance(input_str)
    if isBalance(input_str):
        print(input_str,"is Balance")
    else:
        
        print(input_str,"is not Balance")
            





























            
