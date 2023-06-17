# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside a function: {enemies}")

# increase_enemies()
# print(f"enemies outside a function: {enemies}")

# # Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# # Global Scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

# # There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombies", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# # Modifying Global Scope
# enemies = "Skeleton"

# def increase_enemies():
#     global enemies
#     enemies = "Zombie"
#     print(f"enemies inside a function: {enemies}")

# increase_enemies()
# print(f"enemies outside a function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@johnivanpuayap"