class Solution:

    @staticmethod
    def decimalval(binaryStr: str) -> int:
        decival = 0 
        for bit in binaryStr:
            decival = (decival << 1) | int(bit)
        return decival

    @staticmethod
    def val_to_binary(val: int) -> str:
        
        if val == 0:
            return "0"
            
        output = ""
       
        while val > 0:
            res = val % 2
           
            output = str(res) + output
            val = val // 2 

        return output 

    def addBinary(self, a: str, b: str) -> str:
        
        a_val = self.decimalval(a)
        b_val = self.decimalval(b)

        c = a_val + b_val 

        output = self.val_to_binary(c)
        return output