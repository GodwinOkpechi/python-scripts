'''
try:
    num1=int(input('enter first number: '))
    num2=int(input('enter second number: '))
    sum=num1+num2
    print(sum)
except:
    print('an error occurred in ur input')
'''


try:
    def reverse(word):
        result=''
        for x in word:
            result=x+result
        return result
except:
    print('an error occurred in ur input')



