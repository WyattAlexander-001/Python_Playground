robot= {
    'color': 'red',
    'size': 2,
    'weight': 3,
    'speed': 4,
    'name': 'Robo'
}

print(robot['color']) # red
print(robot['size'] == 2) # True
print(robot.get('size', 0)) # 2
print(robot.get("colorz", "No color found")) # No color found

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)