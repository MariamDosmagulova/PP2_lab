import pygame
import math



def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 5
    mode = 'blue'  
    drawing = False
    last_pos = None

    # Freehand strokes
    strokes = []

    # Shapes to store
    rectangles = []
    circles = []
    squares = []
    right_triangles = []
    equi_triangles = []
    rhombuses = []

    # Temporary start position for shapes
    start_pos = None

    while True:
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:

                # Quit
                if event.key == pygame.K_ESCAPE:
                    return

                # Color modes
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'

                # Shapes
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_s:
                    mode = 'square'
                elif event.key == pygame.K_y:
                    mode = 'right_triangle'
                elif event.key == pygame.K_q:
                    mode = 'equi_triangle'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'

            # Mouse pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Start drawing shapes
                    if mode in ('rectangle', 'circle', 'square',
                                'right_triangle', 'equi_triangle', 'rhombus'):
                        start_pos = event.pos
                    else:
                        # Freehand brush start
                        drawing = True
                        last_pos = event.pos

                # Brush size scroll
                elif event.button == 4:
                    radius = min(200, radius + 1)
                elif event.button == 5:
                    radius = max(1, radius - 1)

            # Mouse release
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    end = event.pos

                    # Finalize shapes
                    if start_pos is not None:
                        if mode == 'rectangle':
                            rectangles.append((start_pos, end))

                        elif mode == 'circle':
                            circles.append((start_pos, end))

                        elif mode == 'square':
                            squares.append((start_pos, end))

                        elif mode == 'right_triangle':
                            right_triangles.append((start_pos, end))

                        elif mode == 'equi_triangle':
                            equi_triangles.append((start_pos, end))

                        elif mode == 'rhombus':
                            rhombuses.append((start_pos, end))

                    # Reset shape temp
                    start_pos = None
                    drawing = False
                    last_pos = None

            # Freehand drawing
            if event.type == pygame.MOUSEMOTION and drawing and mode not in (
                'rectangle', 'circle', 'square',
                'right_triangle', 'equi_triangle', 'rhombus'):

                pos = event.pos
                if last_pos is not None:
                    strokes.append((last_pos, pos, radius, mode))
                last_pos = pos


        screen.fill((0, 0, 0))

        # Freehand lines
        for start, end, width, color_mode in strokes:
            drawLineBetween(screen, start, end, width, color_mode)

        # Render stored shapes
        for st, en in rectangles:
            drawRectangle(screen, st, en)
        for st, en in circles:
            drawCircle(screen, st, en)
        for st, en in squares:
            drawSquare(screen, st, en)
        for st, en in right_triangles:
            drawRightTriangle(screen, st, en)
        for st, en in equi_triangles:
            drawEquilateralTriangle(screen, st, en)
        for st, en in rhombuses:
            drawRhombus(screen, st, en)

        # Preview current shape
        if start_pos is not None and mode in (
            'rectangle', 'circle', 'square',
            'right_triangle', 'equi_triangle', 'rhombus'):

            mouse = pygame.mouse.get_pos()

            if mode == 'rectangle':
                drawRectangle(screen, start_pos, mouse, preview=True)
            elif mode == 'circle':
                drawCircle(screen, start_pos, mouse, preview=True)
            elif mode == 'square':
                drawSquare(screen, start_pos, mouse, preview=True)
            elif mode == 'right_triangle':
                drawRightTriangle(screen, start_pos, mouse, preview=True)
            elif mode == 'equi_triangle':
                drawEquilateralTriangle(screen, start_pos, mouse, preview=True)
            elif mode == 'rhombus':
                drawRhombus(screen, start_pos, mouse, preview=True)

     

        font = pygame.font.SysFont(None, 24)
        controls = [
            "R/G/B - Colors", 
            "E - Eraser",
            "T - Rectangle",
            "C - Circle",
            "S - Square",
            "Y - Right Triangle",
            "Q - Equilateral Triangle",
            "H - Rhombus",
            "Scroll - Brush Size",
            "ESC - Quit"
        ]
        y = 5
        for text in controls:
            img = font.render(text, True, (255, 255, 255))
            screen.blit(img, (10, y))
            y += 20

        pygame.display.flip()
        clock.tick(60)



def color_from_mode(mode):
    if mode == 'blue': return (0, 0, 255)
    if mode == 'red': return (255, 0, 0)
    if mode == 'green': return (0, 255, 0)
    if mode == 'eraser': return (0, 0, 0)
    return (255, 255, 255)


def drawLineBetween(screen, start, end, width, mode):
    """Draws interpolated circles between two points to make a smooth line."""
    color = color_from_mode(mode)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(abs(dx), abs(dy))

    for i in range(steps):
        t = i / steps
        x = int(start[0] * (1 - t) + end[0] * t)
        y = int(start[1] * (1 - t) + end[1] * t)
        pygame.draw.circle(screen, color, (x, y), width)


def drawRectangle(screen, start, end, preview=False):
    """Regular rectangle"""
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, 1)


def drawCircle(screen, start, end, preview=False):
    """Circle defined by distance from center to mouse."""
    color = (255, 255, 255)
    radius = int(math.dist(start, end))
    pygame.draw.circle(screen, color, start, radius, 1)


def drawSquare(screen, start, end, preview=False):
    """Square based on smallest side."""
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end

    side = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(screen, color, rect, 1)


def drawRightTriangle(screen, start, end, preview=False):
    """Draws a right triangle with right angle at start."""
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end

    points = [(x1, y1), (x2, y1), (x2, y2)]
    pygame.draw.polygon(screen, color, points, 1)


def drawEquilateralTriangle(screen, start, end, preview=False):
    """Equilateral triangle based on horizontal base."""
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)
    height = (math.sqrt(3) / 2) * side

    p1 = (x1, y1)
    p2 = (x1 + side, y1)
    p3 = (x1 + side / 2, y1 - height)

    pygame.draw.polygon(screen, color, [p1, p2, p3], 1)


def drawRhombus(screen, start, end, preview=False):
    """Rhombus defined by diagonal points."""
    color = (255, 255, 255)

    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    dx = abs(x2 - x1) / 2
    dy = abs(y2 - y1) / 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(screen, color, points, 1)


main()
