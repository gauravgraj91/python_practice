# Program 1

def hello() :
    print("Hello")
    print("World")

hello()

# Program 2

def getInteger() :
    result = (int(input("Input Value")))
    return result

def Main() :
    print("Started")
    output = getInteger()
    print(output)

# Program 3

for step in range(5) :
    print(step)
    print(5)


# Program 4

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print("a =", a)
        
    inner_function()
    print("a =", a)

a = 10
outer_function()
print("a =", a)

# Program 5

def greet_users(user_name):
    print("Hello", user_name, "Welcome to py struggles.")
greet_users("Venkat")

def greet_daytime(mrng, eve):
    print("Hello Raj", mrng)
    print("Hello Raj", eve)

greet_daytime("Good Morning", "Good Evening")