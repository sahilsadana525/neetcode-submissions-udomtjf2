class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                l.append(int(token))
            elif token == '+':
                a = l.pop()
                b = l.pop()
                l.append(b + a)
            elif token == '-':
                a = l.pop()
                b = l.pop()
                l.append(b - a)
            elif token == '*':
                a = l.pop()
                b = l.pop()
                l.append(b * a)
            else:  # '/'
                a = l.pop()
                b = l.pop()
                l.append(int(b / a))  # truncate toward zero

        return l[-1]

