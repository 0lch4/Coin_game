import pygame
import random
import time

pygame.init()
pygame.mouse.set_visible(False)
widthWindow = 1920
heightWindow = 1080
window = pygame.display.set_mode((widthWindow, heightWindow))
points_counter = -1
level = 0
number_devils = 0
number_fasts = 0
number_mutants = 0
number_ghosts = 0
number_obstacles = 8
max_obstacles = 18
font = pygame.font.Font(None, 36)
x = 100
y = 100
p_key_pressed = False
p_key_released = True
o_key_pressed = False
o_key_released = True
i_key_pressed = False
i_key_released = True
m_key_pressed = False
m_key_released = True
powershield = False
CX = 0
CY = 0

speed = 8
max_speed = 15


menu = pygame.image.load("textures/menu.png")
background1 = pygame.image.load('textures/tlo.jpg')
background2 = pygame.image.load('textures/tlo2.jpg')
background1 = pygame.transform.scale(background1, window.get_size())
background2 = pygame.transform.scale(background2, window.get_size())
background_list = [background1, background2]
background = background1


def random_background():
    background = random.choice(background_list)
    return background


player1_texture = pygame.transform.scale(
    pygame.image.load('textures/player.png'), (40, 40))
player1_rect = player1_texture.get_rect()

player1_texture_shield1 = pygame.image.load('textures/playershield1.png')

player_dead_animation = [pygame.image.load('textures/playerdead1.png'), pygame.image.load(
    'textures/playerdead2.png'), pygame.image.load('textures/playerdead3.png')]

player1_rect.x = x
player1_rect.y = y

treeWidth = 70
treeHeight = 100
tree_texture = pygame.transform.scale(
    pygame.image.load('textures/drzewo.png'), (treeWidth, treeHeight))
tree_rect = tree_texture.get_rect()

stoneWidth = 50
stoneHeight = 50
stone_texture = pygame.transform.scale(
    pygame.image.load('textures/kamien.png'), (stoneWidth, stoneHeight))
stone_rect = stone_texture.get_rect()

goldWidth = 20
goldHeight = 20
gold_texture = pygame.transform.scale(
    pygame.image.load('textures/gold.png'), (goldWidth, goldHeight))
gold_rect = gold_texture.get_rect()

bushWidth = 40
bushHeight = 40
bush_texture = pygame.transform.scale(
    pygame.image.load('textures/krzak.png'), (bushWidth, bushHeight))
bush_rect = bush_texture.get_rect()

bonesWidth = 70
bonesHeight = 30
bones_texture = pygame.transform.scale(
    pygame.image.load('textures/bones.png'), (bonesWidth, bonesHeight))
bones_rect = bones_texture.get_rect()

sarnaWidth = 50
sarnaHeight = 30
sarna_texture = pygame.transform.scale(
    pygame.image.load('textures/sarna.png'), (bonesWidth, bonesHeight))
sarna_rect = sarna_texture.get_rect()

deadtreeWidth = 70
deadtreeHeight = 100
deadtree_texture = pygame.transform.scale(
    pygame.image.load('textures/deadtree.png'), (deadtreeWidth, deadtreeHeight))
deadtree_rect = deadtree_texture.get_rect()


devilWidth = 50
devilHeight = 50
devilSpeed = 5
devilCollision = 50
devil_texture = pygame.transform.scale(
    pygame.image.load('textures/enemy.png'), (devilWidth, devilHeight))
devil_rect = devil_texture.get_rect()

devil_corpses = pygame.transform.scale(pygame.image.load(
    'textures/devildead3.png'), (devilWidth, devilHeight))
devil_dead_animation = [pygame.transform.scale(pygame.image.load('textures/devildead1.png'), (devilWidth, devilHeight)), pygame.transform.scale(pygame.image.load(
    'textures/devildead2.png'), (devilWidth, devilHeight)), pygame.transform.scale(pygame.image.load('textures/devildead3.png'), (devilWidth, devilHeight))]


fastWidth = 40
fastHeight = 40
fastSpeed = 15
fastCollision = 40
fast_texture = pygame.transform.scale(
    pygame.image.load('textures/fast.png'), (fastWidth, fastHeight))
fast_rect = fast_texture.get_rect()
fast_corpses = pygame.transform.scale(pygame.image.load(
    'textures/fastdead3.png'), (fastWidth, fastHeight))
fast_dead_animation = [pygame.transform.scale(pygame.image.load('textures/fastdead1.png'), (fastWidth, fastHeight)), pygame.transform.scale(pygame.image.load(
    'textures/fastdead2.png'), (fastWidth, fastHeight)), pygame.transform.scale(pygame.image.load('textures/fastdead3.png'), (fastWidth, fastHeight))]

mutantWidth = 100
mutantHeight = 100
mutantSpeed = 2
mutantCollision = 100
mutant_texture = pygame.transform.scale(
    pygame.image.load('textures/mutantL.png'), (mutantWidth, mutantHeight))
mutant_rect = mutant_texture.get_rect()

mutant_textureL = mutant_texture

mutant_textureR = pygame.transform.scale(
    pygame.image.load('textures/mutantR.png'), (mutantWidth, mutantHeight))
mutant_rect = mutant_texture.get_rect()
mutant_corpses = pygame.transform.scale(pygame.image.load(
    'textures/mutantdead3L.png'), (mutantWidth, mutantHeight))
mutant_dead_animation = [pygame.transform.scale(pygame.image.load('textures/mutantdead1L.png'), (mutantWidth, mutantHeight)), pygame.transform.scale(pygame.image.load(
    'textures/mutantdead2L.png'), (mutantWidth, mutantHeight)), pygame.transform.scale(pygame.image.load('textures/mutantdead3L.png'), (mutantWidth, mutantHeight))]

ghostWidth = 50
ghostHeight = 50
ghostSpeed = 10
ghostCollision = 50
ghost_texture = pygame.transform.scale(
    pygame.image.load('textures/ghostL.png'), (ghostWidth, ghostHeight))
ghost_rect = ghost_texture.get_rect()

ghost_textureL = ghost_texture

ghost_textureR = pygame.transform.scale(
    pygame.image.load('textures/ghostR.png'), (ghostWidth, ghostHeight))
ghost_rect = ghost_texture.get_rect()
ghost_corpses = pygame.transform.scale(pygame.image.load(
    'textures/ghostdead3L.png'), (ghostWidth, ghostHeight))
ghost_dead_animation = [pygame.transform.scale(pygame.image.load('textures/ghostdead1L.png'), (ghostWidth, ghostHeight)), pygame.transform.scale(pygame.image.load(
    'textures/ghostdead2L.png'), (ghostWidth, ghostHeight)), pygame.transform.scale(pygame.image.load('textures/ghostdead3L.png'), (ghostWidth, ghostHeight))]

move_sound = pygame.mixer.Sound('sounds/kroki.mp3')
pickup_sound = pygame.mixer.Sound('sounds/pickup.mp3')
intro_sound = pygame.mixer.Sound('sounds/intro.mp3')
player_dead_sound = pygame.mixer.Sound('sounds/playerdead.mp3')
ghost_dead_sound = pygame.mixer.Sound('sounds/ghostdead.mp3')
devil_dead_sound = pygame.mixer.Sound('sounds/devildead.mp3')
devil_dead_sound.set_volume(0.5)
monsters1_sound = pygame.mixer.Sound('sounds/monsters.mp3')
monsters2_sound = pygame.mixer.Sound('sounds/monsters2.mp3')
fast_dead_sound = pygame.mixer.Sound('sounds/fastdead.mp3')
fast_dead_sound.set_volume(0.5)
mutant_dead_sound = pygame.mixer.Sound('sounds/mutantdead.mp3')
monsters1_sound = pygame.mixer.Sound('sounds/monsters.mp3')
monsters1_sound.set_volume(0.5)
monsters2_sound = pygame.mixer.Sound('sounds/monsters2.mp3')

monsters_sounds = [monsters1_sound, monsters2_sound]

speed_sound = pygame.mixer.Sound('sounds/speed.mp3')
shield_sound = pygame.mixer.Sound('sounds/shield.mp3')
refresh_sound = pygame.mixer.Sound('sounds/refresh.mp3')


def play_sound(sound):
    if not pygame.mixer.get_busy():
        sound.play()


def stop_sound(sound):
    sound.stop()


def start():
    intro1 = pygame.image.load("textures/intro.png")
    intro2 = pygame.image.load("textures/intro2.png")
    intro3 = pygame.image.load("textures/intro3.png")
    olchastudio = pygame.image.load("textures/olchastudio.png")
    window.blit(olchastudio, (1, 1))
    intro_sound.play()
    pygame.display.update()
    time.sleep(4.4)
    window.blit(intro1, (1, 1))
    pygame.display.update()
    time.sleep(2.4)
    window.blit(intro2, (1, 1))
    pygame.display.update()
    time.sleep(4.6)
    window.blit(intro3, (1, 1))
    pygame.display.update()
    window.blit(menu, (1, 1))
    time.sleep(4)
    pygame.display.update()
    waiting = True
    while waiting:
        play_sound(intro_sound)
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False
                stop_sound(intro_sound)


def deadscreen():
    dead = pygame.image.load("textures/deadscreen.png")
    global level
    global points_counter
    global number_devils
    global number_fasts
    global number_mutants
    global number_ghosts
    global number_obstacles
    global p_key_pressed
    global p_key_released
    global o_key_pressed
    global o_key_released
    global i_key_pressed
    global i_key_released
    global m_key_pressed
    global m_key_released
    global powershield
    global speed
    global x
    global y
    waiting = True
    w8 = True
    end_width, end_height = 1920, 1080
    end_surface = pygame.Surface((end_width, end_height))
    end_texture = pygame.transform.scale(pygame.image.load(
        "textures/end.png"), (end_width, end_height))
    end_texture_rect = end_texture.get_rect()
    end_surface.blit(end_texture, end_texture_rect)
    end_x = 0
    end_y = 0
    window.blit(end_surface, (end_x, end_y))
    pygame.display.update()
    time.sleep(2)
    window.blit(dead, (0, 0))
    Dfont = pygame.font.Font('font/snap.ttf', 100)
    points_text = Dfont.render(
        f'Your score: {level}', True, (255, 0, 0))
    window.blit(points_text, (widthWindow/4 + 70, heightWindow/4))
    pygame.display.update()
    while waiting:
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False
                window.blit(menu, (1, 1))
                pygame.display.update()
                while w8:
                    for i in pygame.event.get():
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE]:
                            time.sleep(0.5)
                            points_counter = -1
                            number_devils = 0
                            number_fasts = 0
                            number_mutants = 0
                            number_ghosts = 0
                            number_obstacles = 8
                            p_key_pressed = False
                            p_key_released = True
                            o_key_pressed = False
                            o_key_released = True
                            i_key_pressed = False
                            i_key_released = True
                            m_key_pressed = False
                            m_key_released = True
                            powershield = False
                            speed = 8
                            x = 100
                            y = 100
                            level = 0
                            w8 = False
                            pygame.display.update()
                            break
            elif keys[pygame.K_ESCAPE]:
                quit()


def pause():
    pauza = pygame.image.load("textures/pauza.png")
    waiting = True
    while waiting:
        window.blit(pauza, (1, 1))
        pygame.display.update()
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                waiting = False
                time.sleep(0.5)


def speed_boost():
    speed_boost_banner = pygame.transform.scale(
        pygame.image.load("textures/turbo.png"), (300, 200))
    max_speed_banner = pygame.transform.scale(
        pygame.image.load("textures/maxspeed.png"), (300, 200))
    if speed < 15:
        speed_sound.play()
        window.blit(speed_boost_banner,
                    (widthWindow/2-140, heightWindow/2-140))
    else:
        window.blit(max_speed_banner, (widthWindow /
                    2 - 140, heightWindow/2 - 140))
    pygame.display.update()
    time.sleep(1)


def refresh():
    refresh_sound.play()
    refresh_banner = pygame.transform.scale(
        pygame.image.load("textures/refresh.png"), (300, 200))
    window.blit(refresh_banner, (widthWindow/2 - 140, heightWindow/2 - 140))
    pygame.display.update()
    time.sleep(1)


def shield():
    shield_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/shield.png"), (300, 200))
    window.blit(shield_banner, (widthWindow/2 - 140, heightWindow/2 - 140))
    pygame.display.update()
    time.sleep(1)


def load(quantity, objectt, lista, rect):
    for i in range(quantity):
        x = random.randint(0, widthWindow)
        y = random.randint(0, heightWindow)
        collision = True
        while collision:
            collision = False
            for o in lista:
                if rect.move(x, y).colliderect(o.rect) or rect.move(x, y).colliderect(player1_rect):
                    collision = True
                    x = random.randint(0, widthWindow)
                    y = random.randint(0, heightWindow)
                    break
        objectt(x, y)


class Border:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)


def borders():
    borders_list = []

    up = Border(1, 1, 1920, 1)
    borders_list.append(up)

    down = Border(1, 1079, 1920, 1)
    borders_list.append(down)

    left = Border(1, 1, 1, 1080)
    borders_list.append(left)

    right = Border(1919, 1, 1, 1080)
    borders_list.append(right)

    return borders_list


borders_list = borders()


class Obstacle:
    def __init__(self, x, y, width, height, texture):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture

    def draw(self, surface):
        surface.blit(self.texture, self.rect)


def obstacles():
    obstacles_list = []

    def tree(xtree, ytree):
        tree = Obstacle(xtree, ytree, treeWidth,
                        treeHeight, tree_texture)
        obstacles_list.append(tree)

    def stone(xstone, ystone):
        stone = Obstacle(xstone, ystone, stoneWidth,
                         stoneHeight, stone_texture)
        obstacles_list.append(stone)

    def bush(xbush, ybush):
        bush = Obstacle(xbush, ybush, bushWidth,
                        bushHeight, bush_texture)
        obstacles_list.append(bush)

    def bones(xbones, ybones):
        bones = Obstacle(xbones, ybones, bonesWidth,
                         bonesHeight, bones_texture)
        obstacles_list.append(bones)

    def sarna(xsarna, ysarna):
        sarna = Obstacle(xsarna, ysarna, sarnaWidth,
                         sarnaHeight, sarna_texture)
        obstacles_list.append(sarna)

    def deadtree(xdeadtree, ydeadtree):
        deadtree = Obstacle(xdeadtree, ydeadtree, deadtreeWidth,
                            deadtreeHeight, deadtree_texture)
        obstacles_list.append(deadtree)

    if background == background1:
        load(number_obstacles, tree, obstacles_list, tree_rect)
        load(number_obstacles-4, sarna, obstacles_list, sarna_rect)
        load(number_obstacles-2, bush, obstacles_list, bush_rect)
        load(number_obstacles-7, bones, obstacles_list, bones_rect)
        load(number_obstacles-6, stone, obstacles_list, stone_rect)

    if background == background2:
        load(number_obstacles, deadtree, obstacles_list, deadtree_rect)
        load(number_obstacles-2, bones, obstacles_list, bones_rect)
        load(number_obstacles-1, stone, obstacles_list, stone_rect)
        load(number_obstacles-2, sarna, obstacles_list, sarna_rect)

    return obstacles_list


obstacles_list = obstacles()


def death_animation(death_frames, x, y):
    for i in death_frames:
        window.blit(i, (x, y))
        pygame.display.update()
        pygame.time.wait(100)

    def __init__(self, x, y, texture):
        self.rect = pygame.Rect(x, y)
        self.texture = texture

    def draw(self, surface):
        surface.blit(self.texture, self.rect)


dead_enemy_list = []


class Enemy:
    def __init__(self, x, y, width, height, texture, speed, collison, enemy_type):
        alive = True
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = speed
        self.collison = collison
        self.direction = (1, 0)
        self.type = enemy_type

    def update(self, obstacles_list):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        for i in obstacles_list:
            if self.type == 'ghost':
                continue
            if self.rect.colliderect(i.rect):
                if self.rect.x < i.rect.left:
                    self.rect.x = i.rect.left - self.collison
                elif self.rect.x > i.rect.right:
                    self.rect.x = i.rect.right
                elif self.rect.y < i.rect.top:
                    self.rect.y = i.rect.top - self.collison
                else:
                    self.rect.y = i.rect.bottom

        for i in borders_list:
            if self.rect.colliderect(i):
                if i == borders_list[0]:
                    self.rect.y = + 5
                elif i == borders_list[1]:
                    self.rect.y = - 55
                elif i == borders_list[2]:
                    self.rect.x = + 5
                elif i == borders_list[3]:
                    self.rect.x = - 55

        if random.random() < 0.05:
            self.change_direction()

    def change_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.choice(directions)
        self.direction = new_direction

    def mirror(self, L, R):
        self.L = L
        self.R = R
        new_direction = self.direction
        if self.type == 'mutant':
            if new_direction == (1, 0):
                self.texture = R
            elif new_direction == (-1, 0):
                self.texture = L
        elif self.type == 'ghost':
            if new_direction == (1, 0):
                self.texture = R
            elif new_direction == (-1, 0):
                self.texture = L

    def delete(self):
        window.blit(fast_corpses, (self.rect.x, self.rect.y))
        dead_enemy_list.append(self)
        enemy_list.remove(self)
        del self


def enemies():
    enemy_list = []

    def devil(xdevil, ydevil):
        devil = Enemy(xdevil, ydevil, devilWidth,
                      devilHeight, devil_texture, devilSpeed, devilCollision, 'devil')
        enemy_list.append(devil)

    def fast(xfast, yfast):
        fast = Enemy(xfast, yfast, fastWidth,
                     fastHeight, fast_texture, fastSpeed, fastCollision, 'fast')
        enemy_list.append(fast)

    def mutant(xmutant, ymutant):
        mutant = Enemy(xmutant, ymutant, mutantWidth,
                       mutantHeight, mutant_texture, mutantSpeed, mutantCollision, 'mutant')
        enemy_list.append(mutant)

    def ghost(xghost, yghost):
        ghost = Enemy(xghost, yghost, ghostWidth,
                      ghostHeight, ghost_texture, ghostSpeed, ghostCollision, 'ghost')
        enemy_list.append(ghost)

    if level % 5 == 0:
        load(number_ghosts, ghost, obstacles_list, ghost_rect)
    elif level % 4 == 0:
        load(number_mutants, mutant, obstacles_list, mutant_rect)
    elif level % 3 == 0:
        load(number_fasts, fast, obstacles_list, fast_rect)
    else:
        load(number_devils, devil, obstacles_list, devil_rect)

    return enemy_list


enemy_list = enemies()


def points():
    gold_list = []

    def gold(xgold, ygold):
        global points_counter
        global number_devils
        global number_fasts
        global number_mutants
        global number_obstacles
        global number_ghosts
        global level
        gold = Obstacle(xgold, ygold, goldWidth,
                        goldHeight, gold_texture)
        gold_list.append(gold)
        if level != 0:
            pickup_sound.play()
        dead_enemy_list.clear()
        points_counter += 1
        level += 1
        if number_obstacles <= max_obstacles:
            number_obstacles += 1
        if level % 2 == 0:
            number_devils += 1
        if level % 3 == 0:
            number_fasts += 1
        if level % 4 == 0:
            number_mutants += 1
        if level % 5 == 0:
            number_ghosts += 1

    gold = load(1, gold, obstacles_list, gold_rect)
    return gold_list


gold_list = points()


def generate_new_obstacles():
    global obstacles_list
    obstacles_list.clear()
    obstacles_list = obstacles()


def generate_new_gold():
    global gold_list
    gold_list.clear()
    gold_list = points()
    play_sound(pickup_sound)


def generate_new_enemy():
    global enemy_list
    enemy_list = enemies()


start()
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


run = True
while run:
    pygame.time.Clock().tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
    xx, yy = 0, 0
    if keys[pygame.K_d]:
        play_sound(move_sound)
        xx += speed
    elif keys[pygame.K_a]:
        play_sound(move_sound)
        xx -= speed
    elif keys[pygame.K_s]:
        play_sound(move_sound)
        yy += speed
    elif keys[pygame.K_w]:
        play_sound(move_sound)
        yy -= speed
    else:
        stop_sound(move_sound)
    if keys[pygame.K_o]:
        if o_key_released:
            if points_counter > 0:
                o_key_pressed = True
                refresh()
            o_key_released = False
        else:
            o_key_pressed = False
            o_key_released = True

    if keys[pygame.K_i]:
        if i_key_released:
            if points_counter >= 3:
                i_key_pressed = True
                shield()
                points_counter -= 3
                powershield = True
            i_key_released = False
        else:
            i_key_pressed = False
            i_key_released = True

    if keys[pygame.K_p]:
        if p_key_released:
            p_key_pressed = True
            if speed <= max_speed and points_counter >= 2:
                speed_boost()
                speed += 1
                points_counter -= 2
            elif speed == max_speed:
                speed_boost()
            p_key_released = False
        else:
            p_key_pressed = False
            p_key_released = True

    if keys[pygame.K_m]:
        if m_key_released:
            m_key_pressed = True
            m_key_released = False
        else:
            m_key_pressed = False
            m_key_released = True

    old_x, old_y = x, y
    x += xx
    y += yy

    for i in borders_list:
        if player1_rect.colliderect(i):
            if i == borders_list[0]:
                y = i.rect.top + 5
            elif i == borders_list[1]:
                y = i.rect.bottom - 45
            elif i == borders_list[2]:
                x = i.rect.left + 5
            elif i == borders_list[3]:
                x = i.rect.right - 45

    for gold in gold_list:
        if player1_rect.colliderect(gold.rect):
            background = random_background()
            gold_list.remove(gold)
            generate_new_obstacles()
            generate_new_gold()
            generate_new_enemy()

        else:
            for i in obstacles_list:
                if player1_rect.colliderect(i.rect):
                    if x < i.rect.left:
                        x = i.rect.left - 40
                    elif x > i.rect.right:
                        x = i.rect.right
                    elif y < i.rect.top:
                        y = i.rect.top - 40
                    else:
                        y = i.rect.bottom

    if o_key_pressed:
        generate_new_obstacles()
        generate_new_gold()
        points_counter -= 2
        level -= 1

    if m_key_pressed:
        pause()

    window.blit(background, (0, 0))

    for gol in gold_list:
        gol.draw(window)

    for obj in obstacles_list:
        obj.draw(window)

    for border in borders_list:
        border.draw(window)

    if powershield == False:
        window.blit(player1_texture, player1_rect)
        player1_rect = pygame.rect.Rect(x, y, 40, 40)
    elif powershield == True:
        window.blit(player1_texture_shield1, player1_rect)
        player1_rect = pygame.rect.Rect(x, y, 40, 40)

    for enemy in enemy_list:
        enemy.update(obstacles_list)
        if enemy.type == 'mutant':
            enemy.mirror(mutant_textureL, mutant_textureR)
        elif enemy.type == 'ghost':
            enemy.mirror(ghost_textureL, ghost_textureR)
        window.blit(enemy.texture, enemy.rect)

        if abs(player1_rect.x - enemy.rect.x) <= 200 and abs(player1_rect.y - enemy.rect.y) <= 200:
            random_monster_sound = random.choice(monsters_sounds)
            play_sound(random_monster_sound)

        if enemy.rect.colliderect(player1_rect):
            if powershield == False:
                player_dead_sound.play()
                death_animation(player_dead_animation, x, y)
                time.sleep(1)
                deadscreen()
                generate_new_enemy()
                generate_new_gold()
                generate_new_obstacles()
                break
            elif powershield == True:
                if enemy.type == 'fast':
                    fast_dead_sound.play()
                    death_animation(fast_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                elif enemy.type == 'devil':
                    devil_dead_sound.play()
                    death_animation(devil_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                elif enemy.type == 'mutant':
                    mutant_dead_sound.play()
                    death_animation(mutant_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                elif enemy.type == 'ghost':
                    ghost_dead_sound.play()
                    death_animation(ghost_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                enemy.delete()
                powershield = False

    for enemy in dead_enemy_list:
        if enemy.type == 'fast':
            window.blit(fast_corpses, (enemy.rect.x, enemy.rect.y))
        if enemy.type == 'devil':
            window.blit(devil_corpses, (enemy.rect.x, enemy.rect.y))
        if enemy.type == 'mutant':
            window.blit(mutant_corpses, (enemy.rect.x, enemy.rect.y))
        if enemy.type == 'ghost':
            window.blit(ghost_corpses, (enemy.rect.x, enemy.rect.y))

    font = pygame.font.Font('font/snap.ttf', 30)
    points_text = font.render(
        f'Gold: {points_counter}', True, (255, 0, 0))
    window.blit(points_text, (1750, 10))
    points_text = font.render(
        f'Level: {level}', True, (255, 0, 0))
    window.blit(points_text, (20, 10))

    pygame.display.update()
