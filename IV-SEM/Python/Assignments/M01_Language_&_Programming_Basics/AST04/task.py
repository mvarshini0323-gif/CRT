def Reverse_String(s: str) -> str:
    #Task
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str


if __name__ == '_main_':
    s = input()
    print(Reverse_String(s))