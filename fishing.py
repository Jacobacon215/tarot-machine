import pygame
from random import randint, choice

FPS = 60


def run():
    dt = 0
    framecount = 0
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    casting = False
    triggered = False
    castframes = 0
    done = True
    bar_pixels_moved = 4
    fish_speed = 3
    catch_percent = 0
    catch_percent_increase = 3
    catch_percent_target = 432
    pulling = False
    card_width = 116
    pull_frames = 0
    pull_percent = 0
    pull_speed = 3
    pull_percent_max = 200
    pull_full_percent = 0
    pull_full_speed = 8
    pull_full_max = 900
    full_width = 522

    # sprite location
    alex_x = 900
    alex_y = 390
    fish_back_x = 600
    fish_back_y = 200
    fish_bar_x = fish_back_x + 59
    fish_bar_y = fish_back_y + 352
    fish_x = fish_bar_x + 2
    fish_y = fish_bar_y - 100
    fish_target_y = fish_y - 50
    card_x = alex_x + 50
    card_y = alex_y + 20
    full_x = 699
    full_y = 990
    full_real_y = 1080

    # asset loading
    ocean = pygame.image.load("assets/ocean.png")
    pier = pygame.image.load("assets/pier.png")
    alex1 = pygame.image.load("assets/alex1.png")
    alex2 = pygame.image.load("assets/alex2.png")
    active_alex = alex1
    fish_back = pygame.image.load("assets/fishing_back.png")
    fish_bar = pygame.image.load("assets/fish_bar.png")
    fish = pygame.image.load("assets/fish.png")
    progress_bar = pygame.image.load("assets/progress_bar.png")

    cards = {}
    cards['tower'] = (pygame.image.load("assets/the_tower_sprite.png"),
                      pygame.image.load("assets/the_tower_full.png"))
    card = None

    # game loop
    while running:
        # poll for events
        # pygame.QUIT event means clicked X to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        running = False
                    case pygame.K_SPACE:
                        if done and not casting and not pulling:
                            casting = True
                            done = False
                            active_alex = alex2
                            alex_y += 150

        # now do game logic
        if done and casting:
            casting = False
            fish_bar_y = fish_back_y + 355
            active_alex = alex1
            alex_y -= 150
            catch_percent = 0
            pulling = True
            card = choice(list(cards.values()))
            pull_percent = 0
            pull_frames = 0
            pull_full_percent = 0
            full_real_y = 1080

        if pulling:
            if pull_percent < pull_percent_max:
                pull_percent += pull_speed
            elif pull_percent > pull_percent_max:
                pull_percent = pull_percent_max

            if pull_percent == pull_percent_max:
                if pull_full_percent < pull_full_max:
                    pull_percent += pull_full_speed
                elif pull_percent > pull_full_max:
                    pull_percent = pull_percent_max

            if pull_full_percent == pull_full_max and full_real_y < full_y:
                full_real_y -= pull_full_speed
            elif pull_full_percent == pull_full_max and full_real_y >= full_y:
                pull_frames += 1

            if pull_frames == 48:
                pulling = False

        if fish_y - fish_speed <= fish_target_y <= fish_y + fish_speed:
            fish_target_y = randint(fish_back_y + 10, fish_back_y + 390)
        elif fish_y < fish_target_y:
            fish_y += fish_speed
        elif fish_y > fish_target_y:
            fish_y -= fish_speed

        keys = pygame.key.get_pressed()
        if casting and not done:
            if keys[pygame.K_SPACE] and fish_bar_y > fish_back_y + 10:
                fish_bar_y -= bar_pixels_moved
            elif fish_bar_y < fish_back_y + 352:
                fish_bar_y += bar_pixels_moved

        if fish_bar_y <= fish_y <= fish_bar_y + 67:
            catch_percent += catch_percent_increase

        if catch_percent >= catch_percent_target:
            done = True
            catch_percent = catch_percent_target

        # drawing
        screen.fill(pygame.Color(65, 151, 230, 0))

        screen.blit(ocean, (-50, 100))
        for i in range(22):
            for j in range(11):
                screen.blit(
                    ocean, (-150 + (i * 100 + ((1920/(FPS * 9)) * framecount)) % 2200, j * 100))

        if casting:
            screen.blit(fish_back, (fish_back_x, fish_back_y))
            screen.blit(fish_bar, (fish_bar_x, fish_bar_y))
            screen.blit(fish, (fish_x, fish_y))
            for i in range(catch_percent):
                screen.blit(progress_bar, (fish_back_x +
                            104, fish_back_y + 437 - i))

        screen.blit(pier, (610, 780))

        screen.blit(active_alex, (alex_x, alex_y))

        if pulling:
            screen.blit(cards['tower'][0], (card_x, card_y + (pull_percent_max - pull_percent)),
                        area=pygame.Rect(0, 0, card_width, pull_percent))
            screen.blit(cards['tower'][1], (full_x, full_real_y),
                        area=pygame.Rect(0, 0, full_width, pull_full_percent))

        # rendering
        pygame.display.flip()
        dt = clock.tick(60)/1000
        framecount += 1


if __name__ == "__main__":
    run()
