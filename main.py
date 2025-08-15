from utils import greet

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    occupation = input("Enter your occupation: ")
    print(f"{greet(name)}, you're {age} years old and your occupation is: {occupation}")

if __name__ == "__main__":
    main()
