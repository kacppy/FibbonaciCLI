import sys

def print_help():
    print("Help information:")
    print("-h, --help: Display this help message.")
    print("<value>: Specify a value for Fibonacci Sequence")
    print("Example:")
    print("python FibbonaciCLI.py 15")


def fibonacci(fib):
    numbers_list = [0, 1]
    
    if fib <= 0:
        return ' \r\n (!) Enter a number above zero '
    elif fib == 1:
        return [0]
    
    while len(numbers_list) < fib:
        next_number = numbers_list[-1] + numbers_list[-2]
        numbers_list.append(next_number)
    
    return numbers_list

def main(args):
    if "-h" in args or "--help" in args or len(args) == 0:
        print_help()
        return

    try:
        fib_amount = int(args[0])
        print(f"Fibonacci sequence of {fib_amount} numbers: {fibonacci(fib_amount)}")
        return
    except:
        print('Please pass a int as argument, or use --help for example')
        return

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
