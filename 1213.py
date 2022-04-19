names = input()
odd=[]
even=''
odd=''
oddcnt=0
evencnt=0
namearr = [0 for _ in range(26)]
for name in names:
    namearr[ord(name)-65] +=1

for i in range(26):
    if namearr[i] != 0:
        if namearr[i]%2==1:
            oddcnt+=1
            odd+=chr(i+65)
    even += (chr(i+65) * (namearr[i]//2))
if oddcnt >=2:
    print("I'm Sorry Hansoo")
else:
    print(even + odd + even[::-1])
