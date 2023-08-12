#1 Map and Lambda Function
cube = lambda x: x ** 3
def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#2 List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);    






#3 Matching Specific String
Regex_Pattern = r"hackerrank"


import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

#4 Matching Digits & Non-Digit Characters
Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#5Matching Specific Characters

Regex_Pattern = r'^[1-3][0-2][xs0][30Aa][xsu][.,]$'    


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#6 Matching Character Ranges
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#7 Matching Start & End

Regex_Pattern = r"^\d\w{4}\.$"


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
