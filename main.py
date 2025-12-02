import comp151Colors
import dearpygui.dearpygui as graphics

graphics.create_context()
graphics.create_viewport(title="Project 7", width=1480, height=1200)
with graphics.window(label="Project 7", width=1600, height=1200):
    with graphics.drawlist(width=1500, height=800):
        #Code for the store
        graphics.draw_rectangle((0, 0), (1500, 200), fill=comp151Colors.MAROON)
        graphics.draw_rectangle((550, 0), (950, 200), fill=comp151Colors.WHITE)
        graphics.draw_rectangle((740, 0), (760, 200), fill=comp151Colors.BLACK)
        graphics.draw_rectangle((680, 95), (710, 105 ), fill=comp151Colors.BLACK)
        graphics.draw_rectangle((820, 95), (790, 105), fill=comp151Colors.BLACK)
        #Code for the first road
        graphics.draw_rectangle((0, 200), (1500, 450), fill=comp151Colors.BLACK)
        #Code for the grassy area
        graphics.draw_rectangle((0, 450), (1500, 700), fill=comp151Colors.GREEN)

graphics.setup_dearpygui()
graphics.show_viewport()
graphics.start_dearpygui()
graphics.destroy_context()