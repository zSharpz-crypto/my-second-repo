# Simple Battle Simulator

This is a basic Python battle simulation between a heroic Knight and two enemies: a mischievous Goblin and an Orc. The game demonstrates object-oriented programming principles such as classes, methods, and interaction between objects.

## File Structure

- `character.py`: Defines the `Character` class with attributes and methods for combat.
- `main.py`: Runs the battle simulation using instances of `Character`.

## Character Class

Located in `character.py`, the `Character` class includes:

### Attributes
- `name` (str): The character's name.
- `hp` (int): Hit points (health).
- `attack_power` (int): Damage dealt per attack.

### Methods
- `attack(other)`: Reduces the `other` character's HP by a random 30%-90% of the initial `attack_power` and prints an attack message.
- `is_alive()`: Returns `True` if HP is greater than 0.
- `__str__()`: Returns a string representation of the character's current HP.

##  How the Battle Works

The battle logic in `main.py` follows these steps:

1. Create three characters: the Knight, a Goblin and an Orc.
2. Print their initial stats.
3. Loop while both are alive:
   - Knight attacks each living enemy.
   - Each surviving enemy attacks Knight.
   - Print updated stats.
4. Declare the winner when the Knight or both enemies reach zero HP.

##  Running the Game

To run the simulation, execute `main.py`:

```bash
python main.py
```
