from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemies = [Character("Goblin", 20, 3), Character("Orc", 20, 3)]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(e.is_alive() for e in enemies):
        # Hero attacks every enemy that is still alive
        for enemy in enemies:
            if enemy.is_alive():
                hero.attack(enemy)
        # Every surviving enemy fights back
        for enemy in enemies:
            if enemy.is_alive() and hero.is_alive():
                enemy.attack(hero)
        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")

if __name__ == "__main__":
    main()
