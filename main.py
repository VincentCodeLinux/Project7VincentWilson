import comp151Colors
import dearpygui.dearpygui as graphics



graphics.create_context()
#This is some of the player variables
player_y = 10
player_x = 500
firebird_y = 125
firebird_x = 500
player_speed = 10
person_scaling = 0.25
car_scaling = 0.50
#This code loads the image
player_w, player_h, channels, player_raw_data = graphics.load_image("PersonSprite.png")
firebird_w, firebird_h, channels, firebird_raw_data = graphics.load_image("FirebirdSprite.png")

#This code shrinks the player and makes him a proper size
shrink_player_w = int(player_w * person_scaling)
shrink_player_h = int(player_h * person_scaling)
#This code shrinks the first car and makes it a proper size
shrink_firebird_w = int(firebird_w * car_scaling)
shrink_firebird_h = int(firebird_h * car_scaling)
#This code sets up the movement for the character
def move_player(sender, app_data):
    global player_x, player_y, player_speed, shrink_player_w, shrink_player_h
    key = app_data
    if key == graphics.mvKey_Left:
        player_x -= player_speed
    elif key == graphics.mvKey_Right:
        player_x += player_speed
    elif key == graphics.mvKey_Up:
        player_y -= player_speed
    elif key == graphics.mvKey_Down:
        player_y += player_speed
    with graphics.mutex():
        graphics.configure_item("player_update", pmin=(player_x, player_y), pmax=(player_x+shrink_player_w, player_y+shrink_player_h))
with graphics.texture_registry():
    graphics.add_static_texture(player_w, player_h, player_raw_data, tag="PersonSprite")
    graphics.add_static_texture(firebird_w, firebird_h, firebird_raw_data, tag="FirebirdSprite")
with graphics.handler_registry():
    graphics.add_key_press_handler(callback=move_player)
graphics.create_viewport(title="Project 7", width=1480, height=1200)
with graphics.window(label="Project 7", width=1600, height=1200):
    with graphics.drawlist(width=1500, height=800):
        #This draws the player
        #Code for the store
        graphics.draw_rectangle((0, 0), (1500, 200), fill=comp151Colors.MAROON)
        graphics.draw_rectangle((550, 0), (950, 200), fill=comp151Colors.WHITE)
        graphics.draw_rectangle((740, 0), (760, 200), fill=comp151Colors.BLACK)
        graphics.draw_rectangle((680, 95), (710, 105 ), fill=comp151Colors.BLACK)
        graphics.draw_rectangle((820, 95), (790, 105), fill=comp151Colors.BLACK)
        #Code for the first road
        graphics.draw_rectangle((0, 200), (1500, 350), fill=comp151Colors.BLACK)
        #Code for the grassy area
        graphics.draw_rectangle((0, 350), (1500, 500), fill=comp151Colors.GREEN)
        #Code for 2nd road
        graphics.draw_rectangle((0, 500), (1500, 650), fill=comp151Colors.BLACK)
        #Code for the parking lot/end
        graphics.draw_rectangle((0, 650), (150, 800))
        graphics.draw_rectangle((0, 650), (300, 800))
        graphics.draw_rectangle((0, 650), (450, 800))
        graphics.draw_rectangle((0, 650), (600, 800))
        graphics.draw_rectangle((0, 650), (750, 800))
        graphics.draw_rectangle((0, 650), (900, 800))
        graphics.draw_rectangle((0, 650), (1050, 800))
        graphics.draw_rectangle((0, 650), (1200, 800))
        graphics.draw_rectangle((0, 650), (1350, 800))
        graphics.draw_rectangle((0, 650), (1500, 800))
        #code
        # This draws the player
        graphics.draw_image("PersonSprite", (player_x, player_y), (player_x + shrink_player_w, player_y + shrink_player_h),
                            tag="player_update")
        graphics.draw_image("FirebirdSprite", (firebird_x, firebird_y),
                            (firebird_x + shrink_firebird_w, firebird_y + shrink_firebird_h),
                            tag="firebird_update")




graphics.setup_dearpygui()
graphics.show_viewport()
graphics.render_dearpygui_frame()
graphics.start_dearpygui()
graphics.destroy_context()