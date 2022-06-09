def calculate(s):
    stack = []
    curr_num = 0
    operand = "+"

    for i, c in enumerate(s):
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        if c in "+*/-" or i == len(s) - 1:
            if operand == "+":
                stack.append(curr_num)
            elif operand == "-":
                stack.append(-curr_num)
            elif operand == "*":
                stack[-1] *= curr_num
            elif operand == "/":
                stack[-1] = int(stack[-1] / curr_num)
            operand, curr_num = c, 0

    return sum(stack)

def main():
    s = "3+2*2"
    print(calculate(s))


if __name__ == '__main__':
    main()
