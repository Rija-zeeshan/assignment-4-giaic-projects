
def main():

    number = float(input("\033[1;3m Type a number to see its square: \033[1;3m"))
    
    # Calculate the square of the number
    square = number * number
    
    print(f"{number} squared is {square}")



if __name__ == '__main__':
    main()