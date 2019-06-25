print("Введите предложение, в конце которого пробел или точка: ")
text = str(input())
print(text)
newt = list(text)
a = len(text)
n = 0
r = 0
for i in range(a-1):
        if (text[i] != ' '):
            r = r+1
            if (newt[i+1] == ' ' or newt[i+1] == '.' or newt[i+1] == ',' or newt[i+1] == ':' or newt[i+1] == '-'):
                n = i+1
                b = newt[n-1]
                newt[n-1] = newt[n-r]
                newt[n-r] = b
                r = 0
text2 = ''
for i in newt:
    text2 += i
print(text2)


