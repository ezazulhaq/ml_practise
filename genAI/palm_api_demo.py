from generate_model import GenerateModel

model = GenerateModel()


def palm_api_demo():
    print("Palm API Demo")
    print("======================")
    print("1. Generate Text")
    print("2. Exit")
    print("======================")
    try:
        choice = int(input("Enter Choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        print("======================")

        palm_api_demo()

    if choice == 1:
        prompt = input("Input Prompt : ")
        complete = model.generate_text(prompt)
        print(complete.result)
        print("======================")
        palm_api_demo()
    elif choice == 2:
        exit()
    else:
        print("Invalid Choice")
        palm_api_demo()


palm_api_demo()
