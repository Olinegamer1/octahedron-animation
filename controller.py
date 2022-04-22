import pygame

from rotate3D import rotate, render_faces

ROTATE_SPEED = 0.1
angle_x = angle_y = angle_z = 0
show_coordinate = True
mouse_rotation = False
show_skeleton = False
hide_faces_figure = True
scale = 150


def action(event, figure, coordinate, window):
    global hide_faces_figure, show_skeleton, show_coordinate, show_coordinate_points_figure, angle_y, angle_x, angle_z, scale

    if event.type == pygame.QUIT:
        pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        angle_y = angle_x = angle_z = 0
        scale = 150
    if keys[pygame.K_a]:
        angle_y += ROTATE_SPEED
    if keys[pygame.K_d]:
        angle_y -= ROTATE_SPEED
    if keys[pygame.K_w]:
        angle_x += ROTATE_SPEED
    if keys[pygame.K_s]:
        angle_x -= ROTATE_SPEED
    if keys[pygame.K_q]:
        angle_z -= ROTATE_SPEED
    if keys[pygame.K_e]:
        angle_z += ROTATE_SPEED
    elif event.type == pygame.KEYDOWN:
        if keys[pygame.K_x]:
            show_coordinate = not show_coordinate
        if keys[pygame.K_z]:
            show_skeleton = not show_skeleton
        if keys[pygame.K_c]:
            hide_faces_figure = not hide_faces_figure

    __mouse_action(event)

    new_octahedron_points = rotate(figure.get_octahedron_points(), angle_x, angle_y, angle_z, window, scale=scale)

    if hide_faces_figure:
        render_faces(new_octahedron_points, figure, window)

    if show_skeleton:
        figure.draw(new_octahedron_points, window)

    if show_coordinate:
        new_coordinate_points = rotate(coordinate.get_coordinate_points(), angle_x, angle_y, angle_z, window,
                                       scale=scale)
        coordinate.draw(new_coordinate_points, window)


def __mouse_action(event):
    global scale, mouse_rotation, angle_x, angle_y, angle_z
    left_mouse_button = pygame.mouse.get_pressed()[0]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
            scale += 10
        elif event.button == 5:
            scale = max(scale - 10, 0)

    if left_mouse_button:
        if not mouse_rotation:
            mouse_rotation = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
            pygame.mouse.get_rel()
        else:
            x, y = pygame.mouse.get_rel()
            angle_x += y * 0.01
            angle_y -= x * 0.01

    if event.type == pygame.MOUSEBUTTONUP:
        mouse_rotation = False
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
