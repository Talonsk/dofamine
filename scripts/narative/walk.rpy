init python:

    from enum import Enum

    class CharacterState(Enum):
        Down = ['ui/sprites/walk_down1.png', 'ui/sprites/walk_down2.png', 'ui/sprites/walk_down3.png']
        Up = ['ui/sprites/walk_up1.png', 'ui/sprites/walk_up2.png', 'ui/sprites/walk_up3.png']
        Left = ['ui/sprites/walk_left1.png', 'ui/sprites/walk_left2.png', 'ui/sprites/walk_left1.png']
        Right = ['ui/sprites/walk_right1.png', 'ui/sprites/walk_right2.png', 'ui/sprites/walk_right1.png']
    

    class You(renpy.Displayable):

        def __init__(self, state, x, y, **kwargs):
            super(You, self).__init__(**kwargs)
            self.x = x
            self.y = y

            self.width = 43
            self.hight = 76

            self.PLAYER_WIDTH = 45
            self.PLAYER_HEIGHT = 75
            self.PLAYER_STATE = CharacterState[state].value
            self.SCENE_WIGHT = config.screen_width
            self.SCENE_HIGHT = config.screen_height

            self.animation_speed = 5
            self.player_speed = 1
            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.move_down = False

        def render(self, width, height, st, at):                        
            # Determines the speed 
            if self.move_left:
                self.x -= self.player_speed
                self.PLAYER_STATE = CharacterState.Left.value
            elif self.move_right:
                self.x += self.player_speed
                self.PLAYER_STATE = CharacterState.Right.value
            
            if self.move_up:
                self.y -= self.player_speed
                self.PLAYER_STATE = CharacterState.Up.value
            elif self.move_down:
                self.y += self.player_speed
                self.PLAYER_STATE = CharacterState.Down.value
            
            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            is_move = self.move_left or self.move_right or self.move_up or self.move_down

            current_frame = int(st*self.animation_speed) % 3 if is_move else 0
            
            current_image = self.PLAYER_STATE[current_frame]
            player = renpy.displayable(current_image)
            
            player_r = renpy.render(player, self.width, self.hight, 0, 0)

            
            r.blit(player_r, (self.x, self.y))

            # Set the position of the player.
            self.x = min(max(self.x, 0), self.SCENE_WIGHT - self.PLAYER_WIDTH)
            self.y = min(max(self.y, 0), self.SCENE_HIGHT - self.PLAYER_HEIGHT)
            
            # Ask that we be re-rendered ASAP, so we can show the next frame.
            renpy.redraw(self, 0)
        
            return r

            render = renpy.Render(self.width, self.hight)
            
            return render

        def event(self, ev, x, y, st):
                
            import pygame
            
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
            elif ev.type == pygame.KEYUP:

                if ev.key == pygame.K_LEFT:
                    self.move_left = False
                elif ev.key == pygame.K_RIGHT:
                    self.move_right = False
                    
                if ev.key == pygame.K_UP:
                    self.move_up = False
                elif ev.key == pygame.K_DOWN:
                    self.move_down = False
            else:
                renpy.IgnoreEvent()
            


screen you:
    zorder 10

    add You(state='Right', x=10, y=350)

screen swing:
    zorder 20

    imagebutton:
        idle 'swing'
        hover "swing_hover"
        xpos 483
        ypos 447
        action Jump("swing")

screen syringe:
    imagebutton:
        idle 'syringe'
        hover "syringe_hover"
        xpos 143
        ypos 96
        action Jump("syringe")

screen bench1:
    zorder 20

    imagebutton:
        idle 'bench1'
        hover "bench1_hover"
        xpos 408
        ypos 290
        action Jump("bench")

screen bench2:
    zorder 20

    imagebutton:
        idle 'bench2'
        hover "bench2_hover"
        xpos 182
        ypos 440
        action Jump("bench")

screen park:
    on "show" action [Show("swing"), Show("syringe"), Show("bench1"), Show("bench2")]


label walk:
    show bg park1

    # window hide
    show screen you
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