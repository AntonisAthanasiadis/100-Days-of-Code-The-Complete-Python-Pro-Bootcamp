#A little text based game I made based on the random module and control flows/loops
import random
import time

def game_loop():
    player_hp = 100
    monster_hp = 100
    monster_name = random.choice(["Gorgon", "Shadow Stalker", "Iron Golem"])

    print(f"--- A wild {monster_name} appears! ---")

    while player_hp > 0 and monster_hp > 0:
        print(f"\nYour HP: {player_hp} | {monster_name} HP: {monster_hp}")
        action = input("Type (A)ttack or (H)eal: ").lower()

        #1. Player Turn
        if action == "a":
            # randint for range-based damage
            damage = random.randint(10, 25)

            # random.random() for a 15% critical hit chance
            if random.random() < 0.15:
                damage *= 2
                print(f"CRITICAL HIT! You dealt {damage} damage!")
            else:
                print(f"You hit the {monster_name} for {damage} damage.")
            monster_hp -= damage
        elif action == "h":
            heal = random.randint(15, 30)
            player_hp += heal
            print(f"You recovered {heal} HP!")
        else:
            print("You stumbled and missed your turn!")

        if monster_hp <= 0:
            print(f"The {monster_name} has been defeated!")
            break

        #2. Monster Turn
        print(f"The {monster_name} is attacking...")
        time.sleep(1)  # Adds a little dramatic pause

        #random.choice for different monster moves
        move = random.choice(["Strike", "Bite", "Special Move"])
        if move == "Special Move":
            m_damage = random.randint(20, 35)
            print(f"Oh no! The {monster_name} used a Special Move for {m_damage} damage!")
        else:
            m_damage = random.randint(5, 15)
            print(f"The {monster_name} used {move} and dealt {m_damage} damage.")

        player_hp -= m_damage

        if player_hp <= 0:
            print("You have been defeated. Game Over.")


if __name__ == "__main__":
    print("Welcome to the Python Monster Arena!")
    game_loop()