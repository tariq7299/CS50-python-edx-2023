



userGreeting = input("Greeting: ").lower().strip()

match userGreeting :
    case "how you doing?":
        print("$20")
    case "what's happening?" | "what's up?":
        print("$100")
    case _:
        print("$0")