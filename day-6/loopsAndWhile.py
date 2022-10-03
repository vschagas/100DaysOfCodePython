'''exercise at site reeborg.ca'''

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_rigth():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()

# for step in range(6):
#     jump()


number_of_hurdles = 6:
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
