import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 580, 820
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Card Animation")
clock = pygame.time.Clock()

# Colors
BG_COLOR = (255, 192, 203)         # Light Pink Background
CARD_COLOR = (255, 255, 255)       # White Card
CAKE_BASE = (101, 55, 0)           # Layer 1: Dark Brown
CAKE_MIDDLE = (160, 95, 25)        # Layer 2: Medium Brown
CAKE_TOP = (210, 150, 80)          # Layer 3: Light Brown
CANDLE_COLOR = (147, 112, 219)     # Purple Candle
FLAME_OUTER = (255, 140, 0)        # Orange Flame
FLAME_INNER = (255, 215, 0)        # Yellow Flame Core
TEXT_COLOR = (40, 40, 40)          # Dark Gray Text

# Floating Balloon Class
class Balloon:
    def __init__(self):
        self.reset()
        self.y = random.randint(0, HEIGHT)

    def reset(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = HEIGHT + random.randint(10, 100)
        self.radius = random.randint(15, 25)
        self.speed = random.uniform(1.5, 3.5)
        self.color = [random.randint(80, 240) for _ in range(3)]

    def move(self):
        self.y -= self.speed
        if self.y < -self.radius * 2:
            self.reset()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.polygon(surface, self.color, [
            (self.x - 3, self.y + self.radius),
            (self.x + 3, self.y + self.radius),
            (self.x, self.y + self.radius + 5)
        ])
        pygame.draw.line(surface, (150, 150, 150), (self.x, self.y + self.radius + 5), (self.x, self.y + self.radius + 25), 1)

# Function to align paragraph text neatly
def render_paragraph(text, font, color, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
        
    return [font.render(line, True, color) for line in lines]

# Generate Balloons
balloons = [Balloon() for _ in range(22)]

# Setup Fonts
font_title1 = pygame.font.SysFont("arial", 28, bold=True)
font_title2 = pygame.font.SysFont("arial", 22, bold=True)
font_body = pygame.font.SysFont("arial", 15)

# Titles
text_title1 = font_title1.render("HELLO 24", True, (210, 105, 30))
text_title2 = font_title2.render("HAPPY BIRTHDAY TO ME!", True, TEXT_COLOR)

# Your Requested Text Paragraphs
paragraph1 = "Happy Birthday to me! Wishing myself a happy new year filled with joy and success."
paragraph2 = "A year of achieving my dreams, working hard, and taking real steps forward."
paragraph3 = "Dedicated to continuously learning and growing to become a professional programmer."
paragraph4 = "Here's to a great year ahead! 💻✨"

# Max width for text alignment
MAX_TEXT_WIDTH = 400

# Pre-render structured lines
lines_p1 = render_paragraph(paragraph1, font_body, (80, 80, 80), MAX_TEXT_WIDTH)
lines_p2 = render_paragraph(paragraph2, font_body, (80, 80, 80), MAX_TEXT_WIDTH)
lines_p3 = render_paragraph(paragraph3, font_body, (80, 80, 80), MAX_TEXT_WIDTH)
lines_p4 = render_paragraph(paragraph4, font_body, (30, 30, 30), MAX_TEXT_WIDTH)

# Animation variables
cake_scale = 0.0
candle_angle = 0

# Main Game Loop
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Background
    screen.fill(BG_COLOR)

    # 2. Update and draw balloons
    for balloon in balloons:
        balloon.move()
        balloon.draw(screen)

    # 3. Draw middle white card
    card_rect = pygame.Rect(40, 25, 500, 770)
    pygame.draw.rect(screen, CARD_COLOR, card_rect, border_radius=20)

    # 4. Cake animation scaling
    if cake_scale < 1.0:
        cake_scale += 0.02

    center_x = WIDTH // 2
    base_y = 280

    # Layer 1: Bottom (Dark Brown)
    w1, h1 = int(170 * cake_scale), int(35 * cake_scale)
    if w1 > 0:
        pygame.draw.rect(screen, CAKE_BASE, (center_x - w1//2, base_y - h1, w1, h1), border_radius=10)

    # Layer 2: Middle (Medium Brown)
    w2, h2 = int(125 * cake_scale), int(30 * cake_scale)
    if w2 > 0:
        pygame.draw.rect(screen, CAKE_MIDDLE, (center_x - w2//2, base_y - h1 - h2 + 2, w2, h2), border_radius=8)

    # Layer 3: Top (Light Brown)
    w3, h3 = int(85 * cake_scale), int(25 * cake_scale)
    if w3 > 0:
        pygame.draw.rect(screen, CAKE_TOP, (center_x - w3//2, base_y - h1 - h2 - h3 + 4, w3, h3), border_radius=6)

    # Moving Candle & Flame Animation
    if cake_scale >= 0.8:
        candle_y = base_y - h1 - h2 - h3 + 4
        
        candle_angle += 0.08
        candle_sway_x = math.sin(candle_angle) * 3.5
        candle_center_x = center_x + candle_sway_x
        
        flame_flicker_x = random.uniform(-1.5, 1.5)
        flame_flicker_y = random.uniform(-1.0, 1.0)

        # Purple Moving Candle Body
        pygame.draw.rect(screen, CANDLE_COLOR, (candle_center_x - 3, candle_y - 22, 6, 22), border_radius=2)
        
        # Flames
        pygame.draw.ellipse(screen, FLAME_OUTER, (candle_center_x - 5 + flame_flicker_x, candle_y - 35 + flame_flicker_y, 10, 15))
        pygame.draw.ellipse(screen, FLAME_INNER, (candle_center_x - 3 + flame_flicker_x, candle_y - 32 + flame_flicker_y, 6, 10))

    # 5. Render Texts
    y_offset = 310
    
    # Titles
    screen.blit(text_title1, text_title1.get_rect(center=(WIDTH//2, y_offset)))
    y_offset += 38
    screen.blit(text_title2, text_title2.get_rect(center=(WIDTH//2, y_offset)))
    y_offset += 45

    # Render Paragraphs
    paragraph_groups = [lines_p1, lines_p2, lines_p3, lines_p4]
    for group in paragraph_groups:
        for line_surface in group:
            screen.blit(line_surface, line_surface.get_rect(center=(WIDTH//2, y_offset)))
            y_offset += 24
        y_offset += 14

    pygame.display.flip()

pygame.quit()
sys.exit()