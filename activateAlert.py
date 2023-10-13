import pygame
pygame.init()
pygame.mixer.pre_init(44100,-16,2,512)
p = pygame.mixer.Sound("alert.wav")
p.set_volume(0.5)
def run(state):
        if state == 1:
                p.play()
        else:
                p.stop()
