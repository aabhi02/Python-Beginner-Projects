import random

#sel = random.choice(["snake", "water", "gun"])  # type: ignore
pt1, pt2 = 0, 0
turn = 0

while turn<3:
    user = input("You: ").lower()
    sel = random.choice(["snake", "water", "gun"])  # type: ignore
    if user == sel:
        print("Bot:", sel)
        continue

    elif user == "snake":
        if sel == "water":
            print("Bot:", sel)
            pt1 = pt1 + 1
        if sel == "gun":
            print("Bot:", sel)
            pt2 = pt2 + 1

    elif user == "water":
        if sel == "gun":
            print("Bot:", sel)
            pt = pt1 + 1
        if sel == "snake":
            print("Bot:", sel)
            pt2 = pt2 + 1

    elif user == 'gun':
        if sel == 'water':
            print("Bot:", sel)
            pt = pt1 + 1
        if sel == 'snake':
            print("Bot:", sel)
            pt2 = pt2 + 1
    turn = turn + 1
print(
    "Points:\n",
    "You\tBot\n",
     pt1,"\t",pt2
)

if pt1 == pt2:
    print("Draw match...")
elif pt1 > pt2:
    print("You Win!!! :)")
else:
    print("You loose :(")