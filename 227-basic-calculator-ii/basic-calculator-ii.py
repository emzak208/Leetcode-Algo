class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        prev_sign = '+'

        for c in s + '+':
            if c.isdigit():
                current_number =  current_number * 10 + int(c)
            elif c in "+-*/":
                if prev_sign == '+':
                    stack.append(current_number)
                elif prev_sign == '-':
                    stack.append(-current_number)
                elif prev_sign == '*':
                    stack.append(stack.pop() * current_number)
                else: 
                    stack.append(math.trunc(stack.pop() / current_number))

                current_number = 0
                prev_sign = c

        return sum(stack)






        