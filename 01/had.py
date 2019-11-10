import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Ahoj vole?', x=10, y=10)


@window.event
def on_text (text):
    label.text = label.text + text
    print(label. text)

@window.event
def on_key_press(key_code, modifier):
    if key_code== pyglet.window.key.ENTER:
        label.text= label.text [:-1]
@window.event
def on_key_press(key_code, modifier):
    if key_code== pyglet.window.key.BACKSPACE:
        label.text= label.text [:-1]
@window.event
def on_draw():
    window.clear()
    label.draw()











pyglet.app.run()
print ('Hotovo!')
