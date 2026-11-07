## Python Practice Question: GameZone Tournament Registration 🎮

### Concepts to Practice

- Default parameters
- Variable-length positional parameters (`*args`)
- Conditional statements
- Functions
- Basic calculations

### Problem Statement

Create a Python program for a gaming tournament called GameZone.

Players can register for a tournament by selecting a game and adding optional gaming accessories. Your task is to create a function that calculates the total registration cost.

### Requirements

Create a function named `register_player()` with the following parameters:

```
def register_player(player_name, game="Minecraft", *accessories):
    pass
```

Your function should:

1. Accept the player's name.
2. Use `"Minecraft"` as the default game.
3. Accept any number of accessories using variable parameters.
4. Calculate the registration fee based on the selected game:

| Game      | Registration Fee |
| --------- | ---------------- |
| Minecraft | ₹200             |
| FIFA      | ₹300             |
| Valorant  | ₹400             |

5\. Each accessory costs ₹50.

Available accessories:

- Gaming Headset
- Gaming Mouse
- Mechanical Keyboard
- Controller
- Gaming Chair

6. If a player selects Valorant and orders 3 or more accessories, provide a 15% discount on the total cost.
7. Display the player's name, selected game, accessories, registration fee, accessory cost, discount, and final amount.
8. If no accessories are selected, display `"No accessories selected"`.

### Sample Function Calls

```
register_player("Alex")
register_player("Emma", "FIFA", "Controller")
register_player("Ryan", "Valorant", "Gaming Headset", "Gaming Mouse", "Mechanical Keyboard")
register_player("Sophia", "Minecraft", "Gaming Chair", "Controller")
```

### Expected Output

For the following function call:

```
register_player("Ryan", "Valorant", "Gaming Headset", "Gaming Mouse", "Mechanical Keyboard")
```

```
Player Name: Ryan
Game: Valorant
Accessories: Gaming Headset, Gaming Mouse, Mechanical Keyboard
Registration Fee: ₹400
Accessories Cost: ₹150
Discount: ₹82.50
Final Amount: ₹467.50
```
