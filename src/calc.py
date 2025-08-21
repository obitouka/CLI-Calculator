from argparse import ArgumentParser

if __name__ == "__main__":
        
    parser = ArgumentParser(
        prog='Calculator ',
        description='What my calculator does: ',
        epilog='Thank you for using my calculator!'
    )
    
    parser.add_argument("-n1", "--num1", help="First number", type=float, default=0, required=True)
    parser.add_argument("-n2", "--num2", help="Second number", type=float, default=0, required=True)
    parser.add_argument(
        "-op", 
        "--operation", 
        help="Operation type", 
        type=str, 
        choices=["+", "-", "*", "/"], 
        required=True
    )

    args = parser.parse_args()

    result = None

    match args.operation:
        case "+":
            result = args.num1 + args.num2
        case "-":
            result = args.num1 - args.num2
        case "*":
            result = args.num1 * args.num2
        case "/":
            result = args.num1 / args.num2

    print(result)
