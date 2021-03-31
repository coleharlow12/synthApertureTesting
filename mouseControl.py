from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

mouse.position = (500,251)
mouse.click(Button.left,1)