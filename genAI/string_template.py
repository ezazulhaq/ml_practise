from generate_model import GenerateModel

model = GenerateModel()

prompt_template = """
{priming}

{question}

{decorator}

Your solution:
"""

priming_text = "You are an expert at writing clear, concise, Python code."
decorator = "Insert comments for each line of code."


def string_template():
    print("String Template Demo")
    print("======================")
    print("1. Generate Text")
    print("2. Exit")
    print("======================")
    try:
        choice = int(input("Enter Choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        print("======================")

        string_template()

    if choice == 1:
        question = input("Input Prompt : ")
        prompt = prompt_template.format(priming=priming_text,
                                        question=question,
                                        decorator=decorator)
        complete = model.generate_text(prompt)
        print(complete.result)
        print("======================")
        string_template()
    elif choice == 2:
        exit()
    else:
        print("Invalid Choice")
        string_template()


string_template()
