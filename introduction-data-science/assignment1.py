import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
    for item in re.finditer("([ \w]*)(: B)", grades):
        print(item.groups())            
grades()  
