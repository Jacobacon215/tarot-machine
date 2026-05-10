import pygame
import words
from random import randint, choice

FPS = 60

# GLOBAL VARIABLE DEFINITION FOR IMAGE USE
tarot_cards = ["tower"]
cards = {card: (pygame.image.load(f"assets/the_{card}_sprite.png"),
                pygame.image.load(f"assets/the_{card}_full.png"))
         for card in tarot_cards}


def display_reading(card_array, synthesis, screen, clock):
    # initialization
    running = True
    proceed = False
    full_x = 200
    full_y = 90
    full_real_y = 1080
    pull_full_percent = 0
    pull_full_speed = 10
    pull_full_max = 900
    full_width = 522
    pull_frames = 0
    pull_frames_target = 120
    text = False
    title_x = full_x + full_width + 100
    title_y = full_y + 25
    desc_x = title_x
    desc_y = title_y + 110
    index = 0
    synthesizing = False
    synthesis_x = 300
    synthesis_y = 100

    # assets
    background = pygame.image.load("assets/tarot_background.png")
    title_font = pygame.font.Font(
        "/usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-SemiBold.ttf", size=110)
    desc_font = pygame.font.Font(
        "/usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-SemiBold.ttf", size=80)

    texts = {x[0]: (
        temp1 := title_font.render(x[0].capitalize(), True, pygame.Color(0, 0, 0, 0)),
        temp2 := desc_font.render(x[1], True, pygame.Color(0, 0, 0, 0)),
        temp3 := pygame.Rect(title_x - 10, title_y - 10,
                             temp2.get_width() + 20, temp1.get_height() + temp2.get_height() + 20),
        pygame.Surface((temp3.width, temp3.height))
    ) for x in card_array}

    synthesis_text = desc_font.render(
        synthesis, True, pygame.Color(0, 0, 0, 0))
    synthesis_surface = pygame.Surface((20 + synthesis_text.get_width() +
                                        20, 20 + synthesis_text.get_height() + 20))
    synthesis_surface.set_alpha(100)
    synthesis_surface.fill((200, 200, 200))

    for _, val in texts.items():
        val[3].set_alpha(100)
        val[3].fill((200, 200, 200))

    # loop
    while running:
        # poll for events
        # pygame.QUIT event means clicked X to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        running = False
                    case pygame.K_SPACE:
                        proceed = True

        # logic
        if proceed:
            full_real_y = 1080
            pull_full_percent = 0
            index += 1
            proceed = False

        if index == 3:
            synthesizing = True
        elif index >= 4:
            return

        if not synthesizing:
            if pull_full_percent < pull_full_max:
                pull_full_percent += pull_full_speed
            elif pull_full_percent > pull_full_max:
                pull_full_percent = pull_full_max

            if full_real_y > full_y:
                full_real_y -= pull_full_speed
            elif full_real_y < full_y:
                full_real_y = full_y
        elif synthesizing:
            pass

        # rendering
        screen.blit(background, (0, 0))

        if not synthesizing:
            screen.blit(cards[card_array[index][0]][1], (full_x, full_real_y),
                        area=pygame.Rect(0, 0, full_width, pull_full_percent))
            if full_real_y <= full_y:
                screen.blit(texts[card_array[index][0]][3],
                            texts[card_array[index][0]][2].topleft)
                screen.blit(texts[card_array[index][0]][0], (title_x, title_y))
                screen.blit(texts[card_array[index][0]][1], (desc_x, desc_y))
        elif synthesizing:
            screen.blit(synthesis_surface,
                        (synthesis_x - 20, synthesis_y - 20))
            screen.blit(synthesis_text, (synthesis_x, synthesis_y))

        pygame.display.flip()
        dt = clock.tick(60)/1000


def fishing_minigame():
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
    pull_speed = 5
    pull_percent_max = 200
    pull_full_percent = 0
    pull_full_speed = 10
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
    full_y = 90
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

    cards_to_pull = []
    cards_pulled = 0

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
                            # cards_to_pull = words.choose_cards()
                            cards_to_pull = [
                                ("tower", "description"), ("tower", "description"), ("tower", "description")]
                    case pygame.K_t:
                        display_reading([("tower", "description"), ("tower",
                                        "description"), ("tower", "description")], "test synthesis.", screen, clock)

        # now do game logic

        if done and casting:
            casting = False
            fish_bar_y = fish_back_y + 355
            active_alex = alex1
            alex_y -= 150
            catch_percent = 0
            pulling = True
            pull_percent = 0
            pull_frames = 0
            pull_full_percent = 0
            full_real_y = 1080

        if cards_pulled == 3:
            display_reading(
                cards_to_pull[0], cards_to_pull[1], cards_to_pull[2], screen, clock)
            cards_to_pull = []
            cards_pulled = 0

        if pulling:
            if pull_percent < pull_percent_max:
                pull_percent += pull_speed
            elif pull_percent > pull_percent_max:
                pull_percent = pull_percent_max

            if pull_percent == pull_percent_max:
                if pull_full_percent < pull_full_max:
                    pull_full_percent += pull_full_speed
                elif pull_full_percent > pull_full_max:
                    pull_full_percent = pull_full_max

            if pull_percent == pull_percent_max and full_real_y > full_y:
                full_real_y -= pull_full_speed
            elif pull_percent == pull_percent_max and full_real_y <= full_y:
                pull_frames += 1

            if pull_frames == 120:
                cards_pulled += 1
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
            screen.blit(cards[cards_to_pull[cards_pulled][0]][0], (card_x, card_y + (pull_percent_max - pull_percent)),
                        area=pygame.Rect(0, 0, card_width, pull_percent))
            screen.blit(cards[cards_to_pull[cards_pulled][0]][1], (full_x, full_real_y),
                        area=pygame.Rect(0, 0, full_width, pull_full_percent))

        # rendering
        pygame.display.flip()
        dt = clock.tick(60)/1000
        framecount += 1


if __name__ == "__main__":
    fishing_minigame()
