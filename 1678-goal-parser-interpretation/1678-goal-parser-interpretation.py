class Solution:
    def interpret(self, command: str) -> str:
        st = ''
        for i in range(len(command)):
            
            if command[i] == 'G':
                st += 'G'
            elif command[i] == '(' and command[i+1] == ')':
                st += 'o'
            elif command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                st += 'al'
        return st