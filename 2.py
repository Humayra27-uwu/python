def greet_members(names):
    greetings = []
    for name in names:
        greetings.append(f"welcome, {name}!")
    return greetings

members = ["alice", "bob", "charlie"]
print(greet_members(members))
