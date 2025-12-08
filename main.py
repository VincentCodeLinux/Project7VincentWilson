import comp151Colors
import dearpygui.dearpygui as graphics

graphics.create_context()
#This is some of the player variables
player_y = 5
player_x = 500
firebird_y = 175
firebird_x = 500
firebird1_y = 150
firebird1_x = 700
firebird2_y = 185
firebird2_x = 850
dog_y = 400
dog_x = 1100
dog1_y = 360
dog1_x = 400
bear_y = 380
bear_x = 400
car_y = 500
car_x = 400
car1_y = 500
car1_x = 600
car2_y = 500
car2_x = 800
target_car_y = 635
target_car_x = 735
player_speed = 10
person_scaling = 0.25
car_scaling = 0.25
dog_scaling = 0.10
bear_scaling = 0.25
target_car_scaling = 0.35
#This code loads the image
player_w, player_h, channels, player_raw_data = graphics.load_image("PersonSprite.png")
#This code loads the image for the first car picture
firebird_w, firebird_h, channels, firebird1_raw_data = graphics.load_image("FirebirdSprite.png")
#This code loads the image for the second car picture
firebird1_w, firebird1_h, channels, firebird2_raw_data = graphics.load_image("FirebirdSprite.png")
#this loads the third car image
firebird2_w, firebird2_h, channels, firebird3_raw_data = graphics.load_image("FirebirdSprite.png")
#This is the code to load the dog
dog_w, dog_h, channels, dog_raw_data = graphics.load_image("CookieSprite.png")
#This code loads the second dog
dog1_w, dog1_h, channels, dog1_raw_data = graphics.load_image("CookieSprite.png")
#This code loads the bear
bear_w, bear_h, channels, bear_raw_data = graphics.load_image("BearSprite.png")
#This code loads the first car on the second street
car_w, car_h, channels, car_raw_data = graphics.load_image("CavalierSprite.png")
#This code loads the second car on the second street
car1_w, car1_h, channels, car1_raw_data = graphics.load_image("CavalierSprite.png")
#This code loads the third car on the second street
car2_w, car2_h, channels, car2_raw_data = graphics.load_image("CavalierSprite.png")
#This code loads the goal car at the end
target_car_w, target_car_h, channels, target_car_raw_data = graphics.load_image("CarDrawing.png")
#This code shrinks the player and makes him a proper size
shrink_player_w = int(player_w * person_scaling)
shrink_player_h = int(player_h * person_scaling)
#This code shrinks the first car and makes it a proper size
shrink_firebird_w = int(firebird_w * car_scaling)
shrink_firebird_h = int(firebird_h * car_scaling)
#This code shrinks the second car in the line
shrink_firebird1_w = int(firebird1_w * car_scaling)
shrink_firebird1_h = int(firebird1_h * car_scaling)
#This code shrinks the third car in the line
shrink_firebird2_w = int(firebird2_w * car_scaling)
shrink_firebird2_h = int(firebird2_h * car_scaling)
#This code shrinks the dog sprite
shrink_dog_w = int(dog_w * dog_scaling)
shrink_dog_h = int(dog_h * dog_scaling)
#This code shrinks the second dog sprite
shrink_dog1_w = int(dog1_w * dog_scaling)
shrink_dog1_h = int(dog1_h * dog_scaling)
#This code shrinks the bear
shrink_bear_w = int(bear_w * bear_scaling)
shrink_bear_h = int(bear_h * bear_scaling)
#This code shrinks the car on the second street
shrink_car_w = int(car_w * car_scaling)
shrink_car_h = int(car_h * car_scaling)
#This code shrinks the second car on the second street
shrink_car1_w = int(car1_w * car_scaling)
shrink_car1_h = int(car1_h * car_scaling)
#This code shrinks the third car on the second street
shrink_car2_w = int(car2_w * car_scaling)
shrink_car2_h = int(car2_h * car_scaling)
#This code shrinks the final car at the end
shrink_target_car_w = int(target_car_w * target_car_scaling)
shrink_target_car_h = int(target_car_h * target_car_scaling)
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
    graphics.add_static_texture(firebird_w, firebird_h, firebird1_raw_data, tag="FirebirdSprite")
    graphics.add_static_texture(firebird1_w, firebird1_h, firebird2_raw_data, tag="Firebird1Sprite")
    graphics.add_static_texture(firebird2_w, firebird2_h, firebird3_raw_data, tag="Firebird2Sprite")
    graphics.add_static_texture(dog_w, dog_h, dog_raw_data, tag="dogSprite")
    graphics.add_static_texture(dog1_w, dog1_h, dog_raw_data, tag="dog1Sprite")
    graphics.add_static_texture(bear_w, bear_h, bear_raw_data, tag="bearSprite")
    graphics.add_static_texture(car_w, car_h, car_raw_data, tag="carSprite")
    graphics.add_static_texture(car1_w, car1_h, car_raw_data, tag="car1Sprite")
    graphics.add_static_texture(car2_w, car2_h, car_raw_data, tag="car2Sprite")
    graphics.add_static_texture(target_car_w, target_car_h, target_car_raw_data, tag="target_car_Sprite")


# This will be where the collision code is

def do_overlap(l1, r1, l2, r2):
            # If one rectangle is to the left of the other
            if l1.get('x') > r2.get('x') or l2.get('x') > r1.get('x'):
                return False

            # If one rectangle is above the other
            if r1.get('y') < l2.get('y') or r2.get('y') < l1.get('y'):
                return False

            return True










with graphics.handler_registry():
    graphics.add_key_press_handler(callback=move_player)
graphics.create_viewport(title="Project 7", width=1480, height=1200)
with graphics.window(label="Project 7", width=1600, height=1200):
    with graphics.drawlist(width=1500, height=800):
        graphics.draw_text((400, 400), "Game Over", color=comp151Colors.RED, size=50, tag='game_over_txt', show=False)

        game_over = False
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
        #This code draws the sign for the store
        graphics.draw_text((130, 20), f"Grocery Store",
                      color=comp151Colors.WHITE, size=25)
        #code
        # This draws the player
        graphics.draw_image("PersonSprite", (player_x, player_y), (player_x + shrink_player_w, player_y + shrink_player_h),
                            tag="player_update")
        graphics.draw_image("FirebirdSprite", (firebird_x, firebird_y),
                            (firebird_x + shrink_firebird_w, firebird_y + shrink_firebird_h),
                            tag="firebird_update")
        graphics.draw_image("FirebirdSprite", (firebird1_x, firebird1_y),
                            (firebird1_x + shrink_firebird1_w, firebird1_y + shrink_firebird1_h),
                            tag="firebird1_update")
        graphics.draw_image("FirebirdSprite", (firebird2_x, firebird2_y),
                            (firebird2_x + shrink_firebird2_w, firebird2_y + shrink_firebird2_h),
        tag="firebird2_update")
        graphics.draw_image("dogSprite", (dog_x, dog_y),
                            (dog_x + shrink_dog_w, dog_y + shrink_dog_h),
                            tag="dog_update")
        graphics.draw_image("dogSprite", (dog1_x, dog1_y),
                            (dog1_x + shrink_dog1_w, dog1_y + shrink_dog1_h),
                            tag="dog1_update")
        graphics.draw_image("bearSprite", (bear_x, bear_y),
                            (bear_x + shrink_bear_w, bear_y + shrink_bear_h),
                            tag="bear_update")
        graphics.draw_image("carSprite", (car_x, car_y),
                            (car_x + shrink_car_w, car_y + shrink_car_h),
                            tag="car_update")
        graphics.draw_image("carSprite", (car1_x, car1_y),
                            (car1_x + shrink_car1_w, car1_y + shrink_car1_h),
                            tag="car1_update")
        graphics.draw_image("carSprite", (car2_x, car2_y),
                            (car2_x + shrink_car2_w, car2_y + shrink_car2_h),
                            tag="car2_update")
        graphics.draw_image("target_car_Sprite", (target_car_x, target_car_y),
                            (target_car_x + shrink_target_car_w, target_car_y + shrink_target_car_h),
                            tag="target_car_update")


        # This is where I move the sprites
        def move_firebird():
            global firebird_x, firebird_y, shrink_firebird_w, shrink_firebird1_h, firebird1_x, firebird1_y, shrink_firebird1_w, shrink_firebird1_h, firebird2_x, firebird2_y, shrink_firebird2_w, shrink_firebird2_h
            firebird_x -= 3
            if firebird_x < 0:
                firebird_x = 1500
            firebird1_x -= 3
            if firebird1_x < 0:
                firebird1_x = 1500
            firebird2_x -= 3
            if firebird2_x < 0:
                firebird2_x = 1500
            graphics.configure_item("firebird_update", pmin=(firebird_x, firebird_y),
                                    pmax=(firebird_x + shrink_firebird_w, firebird_y + shrink_firebird_h))
            graphics.configure_item("firebird1_update", pmin=(firebird1_x, firebird1_y),
                                    pmax=(firebird1_x + shrink_firebird1_w, firebird1_y + shrink_firebird1_h))
            graphics.configure_item("firebird2_update", pmin=(firebird2_x, firebird2_y),
                                    pmax=(firebird2_x + shrink_firebird2_w, firebird2_y + shrink_firebird2_h))


        pass





def collisioncar_check():
                global player_x, player_y, game_over
                player_top_left = {"x": player_x, "y": player_y}
                player_bottom_right = {"x": player_x + shrink_player_w, "y": player_y + shrink_player_h}

                cars = [
                    {"x": firebird_x, "y": firebird_y, "w": shrink_firebird_w, "h": shrink_firebird_h},
                    {"x": firebird1_x, "y": firebird1_y, "w": shrink_firebird1_w, "h": shrink_firebird1_h},
                    {"x": firebird2_x, "y": firebird2_y, "w": shrink_firebird2_w, "h": shrink_firebird2_h}
                ]
                dogs = [
                    {"x": dog_x, "y": dog_y, "w": shrink_dog_w, "h": shrink_dog_h},
                    {"x": dog1_x, "y": dog1_y, "w": shrink_dog1_w, "h": shrink_dog1_h},
                ]
                for car in cars:
                    car_top_left = {"x": car["x"], "y": car["y"]}
                    car_bottom_right = {"x": car["x"] + car["w"], "y": car["y"] + car["h"]}
                    if do_overlap(player_top_left, player_bottom_right, car_top_left, car_bottom_right):
                        game_over = True
                        graphics.configure_item("game_over_txt", show=True)
                        return True





graphics.setup_dearpygui()
graphics.show_viewport()
while graphics.is_dearpygui_running():
    move_firebird()
    if collisioncar_check():
        graphics.configure_item("game_over_txt", show=True)


    graphics.render_dearpygui_frame()
graphics.start_dearpygui()
graphics.destroy_context()