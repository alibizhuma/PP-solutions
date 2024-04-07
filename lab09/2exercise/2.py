import pygame
from random import randrange as rnd
import sys

pygame.init()

WIDTH, HEIGHT = 1100, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
color = (255, 255, 255)
bg_mus = pygame.image.load('flower.png').convert_alpha()
play = pygame.image.load('play_arkanoid.png').convert_alpha()
pause_mus = pygame.image.load('pause_arkanoid.png').convert_alpha()
mus_exit = pygame.image.load('exit1_arkanoid.png').convert_alpha()
play_mus = pygame.image.load('play_mus_arkanoid.png').convert_alpha()
exitt = pygame.image.load('exit_arkanoid.png').convert_alpha()
background_image = pygame.image.load('background.png').convert_alpha()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def detect_collision(dx, dy, ball, rect, is_breakable):
    if is_breakable:
        pass
    else:
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top
        
        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
    return dx, dy


def pause_screen():
    pause_font = pygame.font.SysFont("Arial", 64)
    pause_text = pause_font.render('Music', True, (200, 200, 200))
    pause_text_rect = pause_text.get_rect(center=(WIDTH // 2, 100))

    
    pause_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
     
    pause_surface.fill((128, 128, 128))

    screen.blit(bg_mus, (0, 0)) 
    screen.blit(pause_text, pause_text_rect)

    
    play_music_button = Button(600, 250, play_mus)
    pause_music_button = Button(400, 250, pause_mus)
    exit_music_button = Button(500, 400, mus_exit) 
    
    play_music_button.draw()
    pause_music_button.draw()
    exit_music_button.draw()

    
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_music_button.is_clicked(pygame.mouse.get_pos()):
                pygame.mixer.music.unpause()  
            elif pause_music_button.is_clicked(pygame.mouse.get_pos()):
                pygame.mixer.music.pause()
            elif exit_music_button.is_clicked(pygame.mouse.get_pos()):  
                pygame.quit()
                sys.exit()
 
    pygame.display.flip()

start_button = Button(450, 300, play)
exit_button = Button(450, 400, exitt) 
font = pygame.font.SysFont("Georgia", 64)
paused = False
run = True

while run:
    
    screen.blit(background_image, (0, 0))
    start_button.draw()
    exit_button.draw()

    text = font.render('ARCANOID', True, (222, 184, 135))
    text_rect = text.get_rect(center=(580, 200))
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked(pygame.mouse.get_pos()):
                fps = 60
                game_score = 0
                paddle_w = 230
                paddle_h = 25
                paddle_speed = 15
                paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
                ball_radius = 20
                ball_speed = 6
                ball_rect = int(ball_radius * 2 ** 0.5)
                ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
                dx, dy = 1, -1
                breakable_rows = [0, 1, 2]  
                rows = 4
                columns = 10
                block_list = []
                color_list = []

                for j in range(rows):
                    for i in range(columns):
                        is_breakable = (j == rows - 1 and i == 5) or (j < rows - 1)
                        block_rect = pygame.Rect(10 + 110 * i, 10 + 70 * j, 100, 50)
                        block_list.append((block_rect, is_breakable))
                        if is_breakable:
                            color_list.append((rnd(30, 256), rnd(30, 256), rnd(30, 256)))
                        else:
                            color_list.append((255, 255, 255))

                clock = pygame.time.Clock()
                collision_sound = pygame.mixer.Sound('catch_arkanoid.mp3')
                bonus_sound = pygame.mixer.Sound('bonus_arkanoid.mp3')

                while True:
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                paused = not paused

                    if paused:
                        pause_screen()
                        continue  

                    screen.fill('black')
                    for i, (block, is_breakable) in enumerate(block_list):
                        pygame.draw.rect(screen, color_list[i], block)
                    pygame.draw.rect(screen, pygame.Color('darkorange'), paddle)
                    pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_radius)
                    ball.x += ball_speed * dx
                    ball.y += ball_speed * dy
                    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
                        dx = -dx
                    if ball.centery < ball_radius:
                        dy = -dy

                    if ball.colliderect(paddle) and dy > 0:
                        dx, dy = detect_collision(dx, dy, ball, paddle, False)
                    hit_index = ball.collidelist([block[0] for block in block_list])
                    if hit_index != -1:
                        hit_rect, is_breakable = block_list[hit_index]
                        if is_breakable:
                            hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
                            pygame.draw.rect(screen, pygame.Color('black'), hit_rect)
                            collision_sound.play() 
                            game_score += 1
                            fps += 2
                            block_list.pop(hit_index)
                            color_list.pop(hit_index)
                            if is_breakable and hit_index == 5:  
                                paddle.width += 100
                                bonus_sound.play()  
                        else:
                            dx, dy = detect_collision(dx, dy, ball, hit_rect, is_breakable)

                    # Win, game over
                    if ball.bottom > HEIGHT:
                        print(game_score)
                        print('GAME OVER')
                        pygame.quit()
                        sys.exit()
                    elif not len([block for block, is_breakable in block_list if is_breakable]):
                        print(game_score)
                        print("WIN!!!!!!!!!!!!!!!!!!!!!!!!!")
                        pygame.quit()
                        sys.exit()
                        
                    key = pygame.key.get_pressed()
                    if key[pygame.K_LEFT] and paddle.left > 0:
                        paddle.left -= paddle_speed
                    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
                        paddle.right += paddle_speed

                    pygame.display.flip()

            elif exit_button.is_clicked(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()

    pygame.display.flip()
