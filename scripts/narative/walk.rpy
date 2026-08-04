init python:
    
    class You(renpy.Displayable):

        def __init__(self, image, x, y, **kwargs):
            super(You, self).__init__(**kwargs)
            self.image = image
            self.x = x
            self.y = y

            self.width = 0
            self.hight = 0

            self.PLAYER_WIDTH = 110
            self.PLAYER_HEIGHT = 170
            self.SCENE_WIGHT = config.screen_width 
            self.SCENE_HIGHT = config.screen_height

            self.player_speed = 3
            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.move_down = False
            
            # Position of player
            self.px = 250
            self.py = 840

        def render(self, width, height, st, at):
            
            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)
            
            player = renpy.displayable(self.image) 
            
            player_r = renpy.render(player, 900, 900, 0, 0)
            
            r.blit(player_r, (self.x, self.y))
            
            # Determines the speed 
            if self.move_left:
                self.x -= self.player_speed
            elif self.move_right:
                self.x += self.player_speed
            
            if self.move_up:
                self.y -= self.player_speed
            elif self.move_down:
                self.y += self.player_speed

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

    add You(image='ui/sprites/walk_down1.png', x=100, y=100)

screen park:
    add 'ui/park1.jpg'


label walk:

    # window hide
    show screen you
    call screen park

    pause
    return