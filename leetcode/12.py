class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        temp = num

        while temp > 0:
            if(temp >= 1000):
                answer += 'M' * (temp//1000)
                temp %= 1000
            elif(temp >= 900):
                answer += 'CM'
                temp -= 900
            elif(temp >= 500):
                answer += 'D'
                temp -= 500
            elif(temp >= 400):
                answer += 'CD'
                temp -= 400
            elif(temp >= 100):
                answer += 'C'*(temp//100)
                temp %= 100
            elif(temp >= 90):
                answer += 'XC'
                temp -= 90
            elif(temp >= 50):
                answer += 'L'
                temp -= 50
            elif(temp >= 40):
                answer += 'XL'
                temp -= 40
            elif(temp >= 10):
                answer += 'X'*(temp//10)
                temp %= 10
            elif(temp == 9):
                answer += 'IX'
                break
            elif(temp >= 5):
                answer += 'V'
                temp -= 5
            elif(temp == 4):
                answer += 'IV'
                break
            else:
                answer += 'I'*temp
                break

        return answer