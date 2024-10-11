'''matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for item in row:
        print(item)//

numbers = [2,5,3,8,2,0,7,3] 
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


coordinates = (1,2,3)
x,y,z = coordinates
print(x)

customer = {
    "name": "John Smith",
    "age": 30,
    "is verified": True
}
customer ["name"] = "Godfrey"
print(customer.get("name"))

phone = input("Phone: ")
digit_mapping = {
    "1":"one",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten",
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output) '''   


prev2 = int(input("Enter the first Fibonacci number: "))
prev1 = int(input("Enter the second Fibonacci number: "))

print(prev2)
print(prev1)
for fibo in range(18):
    newfibo = prev2 + prev1
    print(newfibo)
    prev2 = prev1
    prev1 = newfibo
