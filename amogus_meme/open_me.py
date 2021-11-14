import os
import pyglet
import pygame
pygame.init()

ikonka = os.path.dirname(os.path.realpath(__file__)) + "\\icon.png"
gifka = os.path.dirname(os.path.realpath(__file__)) + "\\c57.gif"
music_sound = os.path.dirname(os.path.realpath(__file__)) + "\\don't listen.mp3"
animation = pyglet.image.load_animation(gifka)
animSprite = pyglet.sprite.Sprite(animation)

sound = pygame.mixer.Sound(music_sound)
sound.set_volume(0.008)

w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(width=w, height=h, caption='ඞYOUඞAREඞSUSSYඞBAKAඞ')

icon = pyglet.image.load(ikonka)
window.set_icon(icon)

r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

pyglet.gl.glClearColor(r, g, b, alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()

sound.play(-1)
pyglet.app.run()