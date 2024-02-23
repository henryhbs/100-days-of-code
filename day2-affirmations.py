class bcolors:
    WARNING = '\033[93m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    TIP = '\033[92m'

real_days = ("sunday",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday")

questions = ("- What is your favorite band? ",
            "- What is your favorite color? ",
            "- What is your favorite sport? ",
            "- What is your favorite movie? ",
            "- What is your favorite animal? ",
            "- What is your favorite food? ",
            "- What is your favorite hobby? ")



def check_forbidden_chars(user_input, forbidden_chars):
    for c in user_input:
        if c in forbidden_chars:
            return True
    return False



def check_name(name):
    forbidden_chars = set("0123456789!@#$%^&*()_-+=<>,./?;:'\"[]{}\\|`~")

    while check_forbidden_chars(name, forbidden_chars):
        print(f"{bcolors.WARNING}\t[!] Wait, what? That's a really inhuman name!{bcolors.NORMAL}")
        name = input(f"\t- Please tell me your real name {bcolors.BOLD}(letters only and no symbols){bcolors.NORMAL}:")

    return name



def check_day(day):
    while day not in real_days:
        print(f"{bcolors.WARNING}\t[!] Seems we have a typo here!{bcolors.NORMAL}")
        day = input("\t- Please enter a valid day: ").strip()
    
    for i in range(len(real_days)):
        if day.lower() == real_days[i]:
            return i-1



def generate_affirmations(name, day):
    answer = input(questions[day])

    print(f"{bcolors.TIP}\n Tip of the day:{bcolors.NORMAL}")

    if day == 0:
        print(f" I hope it's a good monday for you to go and listen to some {answer.title()} at the highest safe volume possible, {name}!") # Band

    elif day == 1:
        print(f" I think it's a nice tuesday for you to paint your entire house {answer.upper()}!") # Color

    elif day == 2:
        print(f" I do believe wednesday is the best day to watch or play {answer}!") # Sport

    elif day == 3:
        print(f" Thursday feels like almost-friday, doesn't it {name}? Then I guess you should just chill and watch {answer.title()} after work!") # Movie

    elif day == 4:
        print(f" It's finally friday, {name}, and the perfect weather out there to pet every {answer} you find on the way home!") # Animal

    elif day == 5:
        print(f" Saturday feels like the perfect day to eat some {answer}, your personal favorite.") # Food

    elif day == 6:
        print(f" Sunday is so warm and boring that you should try cheering it up by spending some time doing what you really like, {name}: {answer}!") # Hobbie



def main():
    name = check_name(input("- What is your name? ").strip()).capitalize()
    day = input("- What day of the week is this? ").strip()
    day_index = check_day(day) # handle day if not a real day, returns index

    generate_affirmations(name, day_index) # generate affirmations based on which day it is
    
    input()



if __name__ == "__main__":
    main()
