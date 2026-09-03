default px = 10
default py = 330
default pw = 61
default ph = 106
default hover_id = None
default player_state = CharacterState['Right'].value

init python:
    from enum import Enum

    class CharacterState(Enum):
        Down = ['ui/sprites/walk_down1.png', 'ui/sprites/walk_down2.png', 'ui/sprites/walk_down3.png']
        Up = ['ui/sprites/walk_up1.png', 'ui/sprites/walk_up2.png', 'ui/sprites/walk_up3.png']
        Left = ['ui/sprites/walk_left1.png', 'ui/sprites/walk_left2.png', 'ui/sprites/walk_left1.png']
        Right = ['ui/sprites/walk_right1.png', 'ui/sprites/walk_right2.png', 'ui/sprites/walk_right1.png']

    COLLIDERS = [
        # bench1
        {'x': 408, 'y': 290, 'width': 104, 'height': 66},
        # bench2
        {'x': 182, 'y': 440, 'width': 104, 'height': 68},
        # swing1
        {'x': 475, 'y': 447, 'width': 35, 'height': 191},
        # swing2
        {'x': 673, 'y': 447, 'width': 35, 'height': 191},

        # bin1
        {'x': 510, 'y': 330, 'width': 27, 'height': 22},
        # bin2
        {'x': 154, 'y': 485, 'width': 27, 'height': 24},
        # lamp_post1
        {'x': 170, 'y': 255, 'width': 36, 'height': 86},
        # lamp_post2
        {'x': 410, 'y': 435, 'width': 33, 'height': 84},
        # lamp_post3
        {'x': 636, 'y': 330, 'width': 35, 'height': 85},

        # # bush1
        # {'x': 42, 'y': 30, 'width': 106, 'height': 103},
        # # bush2
        # {'x': 131, 'y': 184, 'width': 105, 'height': 101},
        # # bush3
        # {'x': 705, 'y': 192, 'width': 105, 'height': 101},
        # # bush4
        # {'x': 14, 'y': 460, 'width': 105, 'height': 100},
        # # bush5
        # {'x': 196, 'y': 710, 'width': 105, 'height': 101},

        # tree1
        {'x': 345, 'y': 150, 'width': 56, 'height': 152},
        # tree2
        {'x': 591, 'y': 162, 'width': 60, 'height': 152},
        # tree3
        {'x': 215, 'y': 525, 'width': 59, 'height': 154},
        # tree4
        {'x': 756, 'y': 487, 'width': 59, 'height': 151},
        # tree5
        {'x': 426, 'y': 647, 'width': 58, 'height': 151},
        # tree6
        {'x': 40, 'y': 662, 'width': 5, 'height': 154},
    ]

    PARK_OBJ = [
        {
            'x': 408,
            'y': 290,
            'width': 61,
            'height': 66,
            'idle': 'bench1',
            'hover': 'bench1_hover',
        },
        {
            'x': 182,
            'y': 440,
            'width': 61,
            'height': 68,
            'idle': 'bench2',
            'hover': 'bench2_hover',
        },
        {
            'x': 483,
            'y': 447,
            'width': 61,
            'height': 191,
            'idle': 'swing',
            'hover': 'swing_hover',
        },
        
        {
            'x': 510,
            'y': 330,
            'width': 27,
            'height': 22,
            'idle': 'bin1',
        },
        {
            'x': 154,
            'y': 485,
            'width': 27,
            'height': 24,
            'idle': 'bin2',
        },

        {
            'x': 170,
            'y': 255,
            'width': 36,
            'height': 86,
            'idle': 'lamp_post1',
        },
        {
            'x': 410,
            'y': 435,
            'width': 33,
            'height': 84,
            'idle': 'lamp_post2',
        },
        {
            'x': 636,
            'y': 330,
            'width': 35,
            'height': 85,
            'idle': 'lamp_post3',
        },

        {
            'x': 42,
            'y': 30,
            'width': 106,
            'height': 103,
            'idle': 'bush1',
        },
        {
            'x': 131,
            'y': 184,
            'width': 105,
            'height': 101,
            'idle': 'bush2',
        },
        {
            'x': 705,
            'y': 192,
            'width': 105,
            'height': 101,
            'idle': 'bush3',
        },
        {
            'x': 14,
            'y': 460,
            'width': 105,
            'height': 100,
            'idle': 'bush4',
        },
        {
            'x': 196,
            'y': 710,
            'width': 105,
            'height': 101,
            'idle': 'bush5',
        },

        {
            'x': 305,
            'y': 150,
            'width': 136,
            'height': 152,
            'idle': 'tree1',
        },
        {
            'x': 551,
            'y': 162,
            'width': 140,
            'height': 152,
            'idle': 'tree2',
        },
        {
            'x': 175,
            'y': 525,
            'width': 139,
            'height': 154,
            'idle': 'tree3',
        },
        {
            'x': 716,
            'y': 487,
            'width': 139,
            'height': 151,
            'idle': 'tree4',
        },
        {
            'x': 386,
            'y': 647,
            'width': 138,
            'height': 151,
            'idle': 'tree5',
        },
        {
            'x': 0,
            'y': 662,
            'width': 85,
            'height': 154,
            'idle': 'tree6',
        },
    ]


    def get_collision(next_x, next_y):
        leg_h = 10
        width_diff = 18
        collision_h = 15

        player_left = next_x
        player_right = next_x + store.pw
        player_bottom = next_y + store.ph
        player_top = player_bottom - leg_h


        for _object in COLLIDERS:

            object_right = _object['x'] + _object['width']
            object_bottom = _object['y'] + _object['height']
            object_top = object_bottom - collision_h

            is_collision = (
                player_left < (object_right - width_diff) and 
                player_right > (_object['x'] + width_diff) and
                player_top < object_bottom and
                player_bottom > object_top
            )

            if is_collision:
                return True

    class You(renpy.Displayable):

        def __init__(self, state, **kwargs):
            super(You, self).__init__(**kwargs)

            self.width = store.pw
            self.hight = store.ph
            
            self.SCENE_WIGHT = config.screen_width
            self.SCENE_HIGHT = config.screen_height

            self.animation_speed = 5
            self.player_speed = 1
            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.move_down = False

        def render(self, width, height, st, at): 
            global px
            global py
            global player_state

            next_px = px
            next_py = py                      
            # Determines the speed 
            if self.move_left:
                next_px -= self.player_speed
                player_state = CharacterState.Left.value
            elif self.move_right:
                next_px += self.player_speed
                player_state = CharacterState.Right.value
            
            if self.move_up:
                next_py -= self.player_speed
                player_state = CharacterState.Up.value
            elif self.move_down:
                next_py += self.player_speed
                player_state = CharacterState.Down.value
            

            if not get_collision(next_px, next_py):
                px = next_px
                py = next_py

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            is_move = self.move_left or self.move_right or self.move_up or self.move_down

            current_frame = int(st*self.animation_speed) % 3 if is_move else 0
            
            current_image = player_state[current_frame]
            player = renpy.displayable(current_image)
            
            player_r = renpy.render(player, self.width, self.hight, 0, 0)

            # Set the position of the player.
            px = min(max(px, 0), self.SCENE_WIGHT - self.width)
            py = min(max(py, 0), self.SCENE_HIGHT - self.hight)
            
            r.blit(player_r, (px, py))

            # Ask that we be re-rendered ASAP, so we can show the next frame.
            renpy.redraw(self, 0)
        
            return r

        def event(self, ev, x, y, st):               
            import pygame

            movement_keys = (
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_UP,
                pygame.K_DOWN,
            )
            
            # Keyboard controls
            if ev.type == pygame.KEYDOWN:

                if ev.key == pygame.K_LEFT:
                    self.move_left = True
                    self.move_right = False
                elif ev.key == pygame.K_RIGHT:
                    self.move_right = True
                    self.move_left = False
                
                if ev.key == pygame.K_UP:
                    self.move_up = True
                    self.move_down = False
                elif ev.key == pygame.K_DOWN:
                    self.move_up = False
                    self.move_down = True

                if ev.key in movement_keys:
                    raise renpy.IgnoreEvent()
            elif ev.type == pygame.KEYUP:

                if ev.key == pygame.K_LEFT:
                    self.move_left = False
                elif ev.key == pygame.K_RIGHT:
                    self.move_right = False
                    
                if ev.key == pygame.K_UP:
                    self.move_up = False
                elif ev.key == pygame.K_DOWN:
                    self.move_down = False

                if ev.key in movement_keys:
                    raise renpy.IgnoreEvent()

    class ParkScene(renpy.Displayable):
        def __init__(self, player, **kwargs):
            super(ParkScene, self).__init__(**kwargs)

            self.player = player
            
        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            player_render = renpy.render(self.player, width, height, st, at)

            layers = [
                {
                    'x': 0,
                    'y': 0,
                    'render': player_render,
                    'deep_y': store.py + store.ph,
                }
            ]

            for obj in PARK_OBJ:
                image_name = 'idle' if store.hover_id != obj['idle'] else 'hover'

                print(obj['idle'], image_name, store.hover_id)
                obj_image = renpy.displayable(obj[image_name])
                obj_render = renpy.render(obj_image, obj['width'], obj['height'], 0, 0)

                layers.append(
                    {
                        'x': obj['x'],
                        'y': obj['y'],
                        'render': obj_render,
                        'deep_y': obj['y'] + obj['height'],
                    }
                )

            sorted_layers = sorted(layers, key=lambda dist: dist['deep_y'])

            for layer in sorted_layers:
                r.blit(layer['render'], (layer['x'], layer['y']))

            renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            return self.player.event(ev, x, y, st)


screen scene:
    $ player = You(state="Right")
    add ParkScene(player)

screen syringe:
    zorder -1
    imagebutton:
        idle 'syringe'
        hover 'syringe_hover'
        xpos 143
        ypos 96
        sensitive not dialogue_active
        action Jump("syringe")

screen bench1:
    imagebutton:
        idle Null(104, 66)
        xpos 406
        ypos 286
        sensitive not dialogue_active
        hovered SetVariable('hover_id', 'bench1')
        unhovered SetVariable('hover_id', None)
        action [SetVariable('hover_id', None), Jump("bench")]

screen bench2:
    imagebutton:
        idle Null(104, 68)
        xpos 177
        ypos 438
        sensitive not dialogue_active
        hovered SetVariable('hover_id', 'bench2')
        unhovered SetVariable('hover_id', None)
        action [SetVariable('hover_id', None), Jump("bench")]

screen swing:
    zorder -1

    imagebutton:
        idle Null(218, 191)
        xpos 480
        ypos 444
        sensitive not dialogue_active
        hovered SetVariable('hover_id', 'swing')
        unhovered SetVariable('hover_id', None)
        action [SetVariable('hover_id', None), Jump("swing")]

screen bushes:
    zorder 900

    add "bushes":
        xpos 0
        ypos 851

screen park:
    on "show" action [Show("swing"), Show("syringe"), Show("bench1"), Show("bench2"), Show("bushes")]

label walk:
    show bg park1

    show screen scene
    call screen park

    pause
    return

label swing:
    u 'В парке качели. Я останавливаюсь'

    u 'Ой, а помнишь? — говорю я вслух. - Ты меня качала. Сильно-сильно. Я боялась, что улечу. А ты смеялась и говорила: «Лети, я поймаю»'

    u 'Никогда не ловила. Но это неважно. Главное -обещала'

    jump walk

    return

label syringe:
    u 'Хм....кто-то играл в скорую помощь? Надеюсь тот, кто потерял это, то найдет. Один раз я потеряла свою любимую куклу и долго плакала...'

    jump walk

    return

label bench:
    u 'Я часто уставала и любила посидеть. А она смеялась надо мной...подумаешь! Сейчас я стала сильнее.'

    jump walk

    return
