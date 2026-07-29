class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0 

        for i in range(len(operations)):
            if operations[i] == "+":
                if len(stack) > 1 :
                    num1 = stack[-1]
                    num2 = stack[-2]
                    stack.append(num1 + num2)
                    print(stack)
                else:
                    stacka

            elif operations[i] == "C":
                if stack:
                    stack.pop()
                    print(stack)

            elif operations[i] == "D":
                if stack:
                    d = stack[-1]
                    stack.append(d*2)
                    print(stack)
            else:
                stack.append(int(operations[i]))
                print(stack)
        print(stack)
        total = sum(stack)

        return total 
        