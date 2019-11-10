import pyglet
from random import randrange
from time import time
SIZE = 64
window = pyglet.window.Window()
print((window.width))
print (window.height)
label = pyglet.text.Label('Score: ', x=2, y=2)

green = pyglet.image.load ('green.png')
apple = pyglet.image.load ('apple.png')
snake_tiles = {}
for start in ['bottom', 'top', 'left', 'right', 'end']:
    for end in ['bottom', 'top', 'left', 'right', 'end', 'dead', 'tongue']:
        key = start + '-' + end
        snake_tiles[key] = pyglet.image.load('snake-tiles/' + key + '.png')

def direction(a, b):
    if b == 'end':
        return 'end'
    x_a, y_a = a
    x_b, y_b = b
    if x_a == x_b - 1:
        return 'right'
    elif x_a == x_b + 1:
        return 'left'
    elif y_a == y_b - 1:
        return 'top'
    elif y_a == y_b + 1:
        return 'bottom'
    else:
        return 'end'

class GameState:
    def __init__(self):
        self.score = 0

    def draw(self):
        label.text = 'Score: ' + str(self.score)
        label.draw()
        for x, y in self.food:
            apple.blit(x*SIZE,y*SIZE, width=SIZE, height=SIZE)
        for coords, before, after in zip(
                self.snake,
                ['end'] + self.snake[:-1],
                self.snake[1:] + ['end'],

        ):
            x, y = coords
            after_direction = direction (coords, after)
            if after_direction == 'end':
                if time() % 1 < 0.5:
                    after_direction = 'tongue'
                if self.alive == False:
                    after_direction = 'dead'

            key = direction(coords, before) + '-' + after_direction
            snake_tiles[key].blit(x*SIZE, y*SIZE, width=SIZE, height=SIZE)

    def move(self,dt):
        if self.alive == False:
            return
        dir_x, dir_y = game.direction
        old_head = self.snake[-1]
        old_x, old_y = old_head
        new_x = old_x + dir_x
        new_y = old_y + dir_y
        new_head = new_x, new_y
        if new_head in self.snake:
            game.alive = False
        if new_y < 0:
            game.alive = False
        if new_x < 0:
            game.alive = False
        if new_x >= window.width // SIZE:
            game.alive = False
        if new_y >= window.height // SIZE:
            game.alive = False
        self.snake.append(new_head)

        if new_head in self.food:
            self.score += 1
            self.food.remove(new_head)
            x= randrange (10)
            y= randrange (5)
            new_food = x,y
            self.food.append (new_food)

        else:
             del self.snake[0]

game = GameState()
game.snake = [(1, 2), (2, 2)]
game.food = [(0,4), (5,7),(8,2),(4,4),(7,2)]
game.alive = True
game.direction = 1,0
pyglet.clock.schedule_interval (game.move, 1/5)
@window.event
def on_text (text):
    label.text = label.text + text
    print(label. text)




@window.event
def on_key_press(key_code, modifier):
    if key_code== pyglet.window.key.BACKSPACE:
        label.text= label.text [:-1]
    if key_code== pyglet.window.key.UP:
        game.direction = 0,1
    if key_code== pyglet.window.key.DOWN:
        game.direction = 0,-1
    if key_code== pyglet.window.key.LEFT:
        game.direction = -1,0
    if key_code== pyglet.window.key.RIGHT:
        game.direction = 1,0

@window.event
def on_draw():
    window.clear()
    game.draw()
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)











pyglet.app.run()
print ('Hotovo!')
