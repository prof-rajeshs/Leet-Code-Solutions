class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # The maximum possible length of the product is len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))
        
        # Reverse iterate through both strings to simulate manual multiplication
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Multiply the digits (converting character to int using ASCII math)
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Add to the current position (i + j + 1)
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                # Update the carry at p1 and the value at p2
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Convert the digits array back to a string, skipping any leading zeros
        result_str = []
        for digit in res:
            if not (len(result_str) == 0 and digit == 0):
                result_str.append(str(digit))
                
        return "".join(result_str)
