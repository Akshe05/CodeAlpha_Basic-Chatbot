print("Welcome to simple chatbot")
ip_list=["hello","how are you","bye"]
op_list=["Hi!","I'm fine! Thanks","Goodbye!"]

ip=input("Ask Anything (enter exit to stop):")

while True:
    if ip == "exit":
        print("Exit")
        break
    else:
        if ip in ip_list:
            print(op_list[ip_list.index(ip)])
        else:
            print("Sorry, I don't understand.")
    ip=input("Ask Anything (enter exit to stop):")
