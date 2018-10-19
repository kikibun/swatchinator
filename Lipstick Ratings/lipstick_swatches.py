from turtle import *

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()

lipsticks = {}

file = open('swatches.txt', 'r')
for line in file.read().splitlines():
    color, brand, line, finish, coffee, kiss, comments, image = line.split(', ')
    lipsticks[color] = [brand, line, finish, coffee, kiss, comments, image]
    screen.register_shape(image)
file.close()
#print(lipsticks)

characteristics = {'brand': 0, 'line': 1, 'finish': 2, 'coffee survivability': 3, 'kiss survival': 4, 'comments': 5}
#for line in list(lipsticks.keys())[:-1]:
#    print(line, end=', ')
#print(list(lipsticks.keys())[-1])
#print(line)

print('Characterstics: Color Name, Brand, Finish, Coffee Survivability, Kiss Survival')
option = characteristics[input('Choose a characteristic: ')]
#print(option)
value = input('Search term: ')

for lipstick in lipsticks:
    #print(lipstick)
    #print(lipsticks[lipstick][option])
    if value == lipsticks[lipstick][option]:
        print(lipstick)
        #print(lipsticks[lipstick][option])
        style = ('Veranda', 14, 'bold')
        info = lipsticks[lipstick]
        goto(-150, 100)
        shape(info[6])
        setheading(90)
        stamp()
        setheading(-90)
        forward(60)
