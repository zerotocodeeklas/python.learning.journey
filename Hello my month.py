import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings 
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Birthday Month - Story Compact")
clock = pygame.time.Clock()

# Colors
BG_DARK = (15, 15, 26)
BG_HAPPY = (28, 16, 42)
GOLD_TEXT = (255, 205, 85)
WHITE_TEXT = (245, 245, 250)
ACCENT_MUTED = (170, 160, 190)

# 1. Background Floating Particles
class BackgroundParticle:
    def __init__(self):
        self.reset()
        self.y = random.randint(0, HEIGHT)

    def reset(self):
        self.x = random.randint(15, WIDTH - 15)
        self.y = HEIGHT + random.randint(10, 40)
        self.size = random.uniform(2, 4)
        self.speed = random.uniform(0.8, 2.0)
        self.alpha = random.randint(80, 200)

    def move(self):
        self.y -= self.speed
        if self.y < -10:
            self.reset()

    def draw(self, surface):
        s = pygame.Surface((int(self.size * 2), int(self.size * 2)), pygame.SRCALPHA)
        pygame.draw.circle(s, (255, 195, 85, self.alpha), (int(self.size), int(self.size)), int(self.size))
        surface.blit(s, (self.x, self.y))

# 2. Explosion Shards
class ExplosionShard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(4, 14)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.size = random.uniform(3, 6)
        self.color = random.choice([(255, 205, 85), (255, 120, 80), (255, 255, 255), (210, 130, 255)])
        self.alpha = 255
        self.decay = random.uniform(3, 6)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15
        self.alpha -= self.decay

    def draw(self, surface):
        if self.alpha > 0:
            s = pygame.Surface((int(self.size * 2), int(self.size * 2)), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, int(self.alpha)), (int(self.size), int(self.size)), int(self.size))
            surface.blit(s, (self.x, self.y))

# Objects Initialization
bg_particles = [BackgroundParticle() for _ in range(30)]
explosion_shards = []

# Fonts Setup
font_big_title = pygame.font.SysFont("georgia", 34, bold=True)
font_clock = pygame.font.SysFont("impact", 68)
font_date = pygame.font.SysFont("arial", 20, bold=True)
font_subtitle = pygame.font.SysFont("arial", 18, bold=True)
font_code_text = pygame.font.SysFont("consolas", 13)

# Pre-rendered Texts
text_hello = font_subtitle.render("W E L C O M E   T O", True, ACCENT_MUTED)
text_bday_month = font_big_title.render("MY BIRTHDAY MONTH", True, GOLD_TEXT)
text_sub = font_subtitle.render("September Chapter 👑✨", True, WHITE_TEXT)

code_line_1 = font_code_text.render("const isBirthdayMonth = true;", True, (130, 200, 255))
code_line_2 = font_code_text.render("mode.set('Party & Coding 💻🎉');", True, (150, 230, 150))
code_quote  = font_code_text.render("// Another year of code, growth & magic.", True, (180, 180, 190))

# Timer & State Variables
seconds_left = 10
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

is_september = False
flash_alpha = 0

# Main Loop
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == timer_event:
            if seconds_left > 0:
                seconds_left -= 1
            elif seconds_left == 0 and not is_september:
                is_september = True
                flash_alpha = 255
                explosion_shards = [ExplosionShard(WIDTH // 2, HEIGHT // 2 - 50) for _ in range(90)]

    # 1. Background Fill
    screen.fill(BG_HAPPY if is_september else BG_DARK)

    # 2. Draw Floating Background Particles
    for p in bg_particles:
        p.move()
        p.draw(screen)

    # 3. Main Content Rendering
    if not is_september:
        current_sec = 50 + (10 - seconds_left)
        clock_str = f"11:59:{current_sec:02d}"
        txt_clock = font_clock.render(clock_str, True, WHITE_TEXT)
        screen.blit(txt_clock, txt_clock.get_rect(center=(WIDTH//2, 210)))

        txt_date = font_date.render("31 / 08 / 2026", True, ACCENT_MUTED)
        screen.blit(txt_date, txt_date.get_rect(center=(WIDTH//2, 280)))

        # Waiting Glass Box
        box_w, box_h = 420, 130
        box_x, box_y = WIDTH//2 - box_w//2, 380
        
        glass = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        pygame.draw.rect(glass, (255, 255, 255, 10), (0, 0, box_w, box_h), border_radius=16)
        pygame.draw.rect(glass, (255, 255, 255, 25), (0, 0, box_w, box_h), width=1, border_radius=16)
        screen.blit(glass, (box_x, box_y))

        txt_wait = font_subtitle.render("Entering My Birthday Month... 🎂", True, GOLD_TEXT)
        screen.blit(txt_wait, txt_wait.get_rect(center=(WIDTH//2, box_y + 40)))
        
        txt_code_wait = font_code_text.render("// Preparing birthday vibes & goals...", True, ACCENT_MUTED)
        screen.blit(txt_code_wait, txt_code_wait.get_rect(center=(WIDTH//2, box_y + 85)))

    else:
        
        y_center = 160
        
        # Header Text
        screen.blit(text_hello, text_hello.get_rect(center=(WIDTH//2, y_center)))
        screen.blit(text_bday_month, text_bday_month.get_rect(center=(WIDTH//2, y_center + 50)))
        screen.blit(text_sub, text_sub.get_rect(center=(WIDTH//2, y_center + 95)))

        # Main Birthday Glass Box
        box_w, box_h = 420, 190
        box_x, box_y = WIDTH//2 - box_w//2, 350
        
        glass = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        pygame.draw.rect(glass, (255, 255, 255, 14), (0, 0, box_w, box_h), border_radius=18)
        pygame.draw.rect(glass, GOLD_TEXT, (0, 0, box_w, box_h), width=1, border_radius=18)
        screen.blit(glass, (box_x, box_y))

        # Code & Wish Lines Inside Box
        screen.blit(code_line_1, (box_x + 30, box_y + 35))
        screen.blit(code_line_2, (box_x + 30, box_y + 80))
        screen.blit(code_quote, (box_x + 30, box_y + 130))

        # Footer Date Accent
        font_footer = pygame.font.SysFont("arial", 13, bold=True)
        text_foot = font_footer.render("✨ SEPTEMBER 2026 | BIRTHDAY SEASON ✨", True, ACCENT_MUTED)
        screen.blit(text_foot, text_foot.get_rect(center=(WIDTH//2, 620)))

    # 4. Update & Draw Explosion Shards
    for shard in explosion_shards:
        shard.update()
        shard.draw(screen)

    # 5. Flash Effect
    if flash_alpha > 0:
        flash_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        flash_surf.fill((255, 255, 255, flash_alpha))
        screen.blit(flash_surf, (0, 0))
        flash_alpha -= 10

    pygame.display.flip()

pygame.quit()
sys.exit()