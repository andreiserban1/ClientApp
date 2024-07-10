import os
from groq import Groq


api_key = os.getenv('GROQ_API_KEY')


if api_key:
    print(f"GROQ_API_KEY: {api_key}")
else:
    print("GROQ_API_KEY nu este setat")
    raise ValueError("GROQ_API_KEY nu este setat")

client = Groq(api_key=api_key)


user_request = input("Introduceti cerintele pentru aplicatie: ")


completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": f"Build an application for a client, having in mind the followings:\n- the client will have to provide the initial information and requirements to be able to generate the application (so he will write them from the keyboard).\n- you will have to register the client's request and you will analyze it based on your knowledge in the field of IT and programming.\n- you will have to describe the application according to the request.\n- you will have to mention the technologies used to develop the application (for example: technological stack, front-end, back-end, databases, etc.)\n- the concrete and detailed tasks necessary to develop the application, especially those not mentioned by the client (such as financial sections, invoicing, etc.) like in this example"
        },
        {
            "role": "assistant",
            "content": f"Please specify exactly what kind of application you want. Depending on your requirements, I will describe in detail the application, the technologies used for the development of the application (front-end, back-end, databases, etc.), the concrete tasks for the development of the application (financial sections, invoicing, etc. ) and also the possible prices for those tasks."
        },
        {
            "role": "user",
            "content": user_request
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)


output_file = "output.txt"


with open(output_file, 'w') as file:

    for chunk in completion:
        file.write(chunk.choices[0].delta.content or "")

print(f"Output-ul a fost salvat in fisierul {output_file}")

# se foloseste $env:GROQ_API_KEY = " " in terminalul Python (nu PowerShell)