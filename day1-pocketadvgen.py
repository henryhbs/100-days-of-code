import time
import random

def roll_adventure(name, rival, time_of_day, power, city, food, skip):
    weather_pool = ["sunny", "warm", "cold", "cloudy"]
    weather = random.choice(weather_pool)

    print(f"\n\nSo here we are at {city} in a {weather} {time_of_day}, at the brink of an epic decisive battle between {name} and {rival}...")
    time.sleep(2)
    print(f"\nTension grows as {name} shows up eating a {food} while {rival} missed their {skip} just to show up in time for this clash.")
    time.sleep(2)
    print(f"\nAnd here it is! The beginning or the end of all things as {name} unleashes the full potention of their {power}! We cannot foresee the outcome of this event!")

    # End
    input()
    exit()

def main():
    print("Welcome to our very short adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!\n")

    name = input("- What is your name? ").capitalize()
    rival = input("- Name your rival: ").capitalize()
    time_of_day = input("- What time of day is it? ").lower()
    power = input("- Name a very useless superpower: ").upper()
    city = input("- Tell me the location of our battle: ").title()
    food = input("- What is your favorite food? ").lower()
    skip = input("- Name a fun thing your rival would skip in order to battle you: ").lower()

    # Pass
    roll_adventure(name, rival, time_of_day, power, city, food, skip)

if __name__ == "__main__":
    main()
