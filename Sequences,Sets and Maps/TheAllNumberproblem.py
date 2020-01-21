def get_evenodd_list():
    odd = []
    even = []
    
    while True:
        user_number = int(input())
        
        if str(user_number) == "-1":
            break
        elif user_number % 2 != 0:
            odd.append(user_number)
        else:
            even.append(user_number)
    
    return odd,even

def main():
    odds, evens = get_evenodd_list()
    print(odds)
    print(evens)

if __name__ == "__main__":
    main()