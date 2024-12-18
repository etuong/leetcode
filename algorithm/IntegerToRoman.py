# Convert integer to roman
class Solution:
  def intToRoman(self, num: int) -> str:    
    roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    result = ""
    for value in roman.keys():
      while num >= value:
        result += roman[value]
        num -= value
    return result 

s = Solution()
print(s.intToRoman(3749))  
print(s.intToRoman(58))