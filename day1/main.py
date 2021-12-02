

def main():
    increased = 0
    print("Hello World!")
    
    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]
    
    numbers = list(map(int, lines))
    
    for i in range(len(numbers)):

        if numbers[i] > numbers[i-1]:
            increased += 1

    print(increased)

if __name__ == "__main__":
    main()