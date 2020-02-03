################################################################################
## Initialization
################################################################################

init offset = -1

init:
    $ config.keymap['quit'].append('K_ESCAPE')
    $ config.keymap['game_menu'].remove('K_ESCAPE')


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

## CG Gallery ##################################################################

init:
    image cg1 = "images/cg/cg1.jpg"
    image cg2 = "images/cg/cg2.jpg"
    image cg3 = "images/cg/cg3.jpg"
    image cg4a_1 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4a.png", (0,0), "images/cg/cg4/smile.png")
    image cg4a_2 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4a.png", (0,0), "images/cg/cg4/happy.png")
    image cg4a_3 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4a.png", (0,0), "images/cg/cg4/happyb.png")
    image cg4a_4 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4a.png", (0,0), "images/cg/cg4/shock.png")
    image cg4a_5 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4a.png", (0,0), "images/cg/cg4/sleep.png")
    image cg4a_6 = "images/cg/cg4/cg4a_zoom.jpg"
    image cg4b_1 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4b.png", (0,0), "images/cg/cg4/smile.png")
    image cg4b_2 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4b.png", (0,0), "images/cg/cg4/happy.png")
    image cg4b_3 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4b.png", (0,0), "images/cg/cg4/happyb.png")
    image cg4b_4 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4b.png", (0,0), "images/cg/cg4/shock.png")
    image cg4b_5 = im.Composite((1280, 720), (0,0), "images/cg/cg4/cg4b.png", (0,0), "images/cg/cg4/sleep.png")
    image cg5_1 = "images/cg/cg5_1.jpg"
    image cg5_2 = "images/cg/cg5_2.jpg"
    image cg6_1 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mcwince.png", (0,0), "images/cg/cg6/jconsiderate.png", (0,0), "images/cg/cg6/tail2.png")
    image cg6_2 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mcavoidb.png", (0,0), "images/cg/cg6/jhappyb.png", (0,0), "images/cg/cg6/tail.png")
    image cg6_3 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mchappy.png", (0,0), "images/cg/cg6/jhappy.png", (0,0), "images/cg/cg6/tail2.png")
    image cg6_4 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mchappyb.png", (0,0), "images/cg/cg6/jshockb.png", (0,0), "images/cg/cg6/tail.png")
    image cg6_5 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mcshock.png", (0,0), "images/cg/cg6/jshock.png", (0,0), "images/cg/cg6/tail2.png")
    image cg6_6 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mcsmile.png", (0,0), "images/cg/cg6/jsmile.png", (0,0), "images/cg/cg6/tail2.png")
    image cg6_7 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mcthink.png", (0,0), "images/cg/cg6/jthink.png", (0,0), "images/cg/cg6/tail2.png")
    image cg6_8 = im.Composite((1280, 720), (0,0), "images/cg/cg6/mcsmile.png", (0,0), "images/cg/cg6/jwatch.png", (0,0), "images/cg/cg6/tail2.png")
    image cg7_1 = "images/cg/cg7/cg7_1.jpg"
    image cg7_2 = "images/cg/cg7/cg7_2.jpg"
    image cg7_3 = "images/cg/cg7/cg7_3.jpg"
    image cg7_4 = "images/cg/cg7/cg7_4.jpg"
    image cg8_1 = "images/cg/cg8_1.jpg"
    image cg8_2 = "images/cg/cg8_2.jpg"
    image cg8_3 = "images/cg/cg8_3.jpg"
    image cg9_1 = im.Composite((1280, 720), (0,0), "images/cg/cg9/cg9_1.png", (0,0), "images/cg/cg9/cg9_1_keismile.png", (0,0), "images/cg/cg9/cg9_1_mccurious.png")
    image cg9_2 = im.Composite((1280, 720), (0,0), "images/cg/cg9/cg9_1.png", (0,0), "images/cg/cg9/cg9_1_keiblush.png", (0,0), "images/cg/cg9/cg9_1_mcblush.png")
    image cg9_3 = im.Composite((1280, 720), (0,0), "images/cg/cg9/cg9_2.png", (0,0), "images/cg/cg9/cg9_2_mc1.png")
    image cg9_4 = im.Composite((1280, 720), (0,0), "images/cg/cg9/cg9_2.png", (0,0), "images/cg/cg9/cg9_2_mc2.png")
    image cg10_kurusu = "images/cg/cg10/cg10_kurusu.jpg"
    image cg10_kagaho = "images/cg/cg10/cg10_kagaho.jpg"
    image cg10_shoko = "images/cg/cg10/cg10_shoko.jpg"
    image cg10_keisuke = "images/cg/cg10/cg10_keisuke.jpg"
    image cg10_1 = "images/cg/cg10/cg10_1.jpg"
    image cg10_2 = "images/cg/cg10/cg10_2.jpg"
    image cg11_1 = "images/cg/cg11/cg11_1.jpg"
    image cg11_2 = im.Composite((1280, 820), (0,0), "images/cg/cg11/cg11_2.png", (0,0), "images/cg/cg11/mc_nervous.png", (0,0), "images/cg/cg11/shoichi_kiss.png")
    image cg11_3 = im.Composite((1280, 820), (0,0), "images/cg/cg11/cg11_2.png", (0,0), "images/cg/cg11/mc_good.png", (0,0), "images/cg/cg11/shoichi_lick.png")
    image cg11_4 = im.Composite((1280, 820), (0,0), "images/cg/cg11/cg11_2.png", (0,0), "images/cg/cg11/mc_moanopen.png", (0,0), "images/cg/cg11/shoichi_suck.png")
    image cg11_5 = im.Composite((1280, 820), (0,0), "images/cg/cg11/cg11_2.png", (0,0), "images/cg/cg11/mc_moanclosed.png", (0,0), "images/cg/cg11/shoichi_suck2.png")
    image cg11_6 = im.Composite((1280, 820), (0,0), "images/cg/cg11/cg11_2.png", (0,0), "images/cg/cg11/mc_grit.png", (0,0), "images/cg/cg11/shoichi_cum.png")
    image cg11_7 = im.Composite((1280, 820), (0,0), "images/cg/cg11/cg11_2.png", (0,0), "images/cg/cg11/mc_afterglow.png", (0,0), "images/cg/cg11/shoichi_lickcum.png")
    image cg12_1 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_1.png", (0,0), "images/cg/cg12/Yuu_1.png", (0,0), "images/cg/cg12/Thrust_1.png")
    image cg12_2 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_2.png", (0,0), "images/cg/cg12/Yuu_2.png", (0,0), "images/cg/cg12/Thrust_2.png")
    image cg12_3 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_3.png", (0,0), "images/cg/cg12/Yuu_3.png", (0,0), "images/cg/cg12/Thrust_3.png")
    image cg12_4 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_4.png", (0,0), "images/cg/cg12/Yuu_4.png", (0,0), "images/cg/cg12/Thrust_4.png")
    image cg12_5 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_5.png", (0,0), "images/cg/cg12/Yuu_5.png", (0,0), "images/cg/cg12/Thrust_5.png")
    image cg12_6 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_6.png", (0,0), "images/cg/cg12/Yuu_6.png", (0,0), "images/cg/cg12/Thrust_6.png")
    image cg12_7 = im.Composite((1280, 720), (0,0), "images/cg/cg12/base.png", (0,0), "images/cg/cg12/Sho_6.png", (0,0), "images/cg/cg12/Yuu_7.png", (0,0), "images/cg/cg12/Thrust_7.png")
    image cg13_1 = "images/cg/cg13_1.jpg"
    image cg13_2 = "images/cg/cg13_2.jpg"
    image cg14 = "images/cg/cg14.jpg"
    image cg15 = "images/cg/cg15.jpg"
    image cg16_1 = im.Composite((1280, 720), (0,0), "images/cg/cg16/cg16_base.png", (0,0), "images/cg/cg16/cg16_closed.png")
    image cg16_2 = im.Composite((1280, 720), (0,0), "images/cg/cg16/cg16_base.png", (0,0), "images/cg/cg16/cg16_open.png")
    image cg17_a = im.Composite((1280, 720), (0,0), "images/cg/cg17/cg17_base.png", (0,0), "images/cg/cg17/cg17_mc1.png", (0,0), "images/cg/cg17/cg17_jun1.png")
    image cg17_c = im.Composite((1280, 720), (0,0), "images/cg/cg17/cg17_base.png", (0,0), "images/cg/cg17/cg17_mc2.png", (0,0), "images/cg/cg17/cg17_jun2.png")
    image cg17_b = "images/cg/cg17/cg17_2.jpg"
    image cg18 = "images/cg/cg18.jpg"
    image cg19 = "images/cg/cg19.jpg"
    image cg20 = "images/cg/cg20.jpg"

init python:
    from __future__ import division
    import math

    #list the CG gallery images here:
    gallery_cg_items = [
        ("cg_button_1", ["cg1"]),
        ("cg_button19", ["cg19"]),
        ("cg_button20", ["cg20"]),
        ("cg_button_2", ["cg2"]),
        ("cg_button18", ["cg18"]),
        ("cg_button_3", ["cg3"]),
        ("cg_button_6", ["cg6_1", "cg6_2", "cg6_3", "cg6_4", "cg6_5", "cg6_6", "cg6_7", "cg6_8"]),
        ("cg_button_13", ["cg13_1", "cg13_2"]),
        ("cg_button_15", ["cg15"]),
        ("cg_button_14", ["cg14"]),
        ("cg_button_16", ["cg16_1", "cg16_2"]),
        ("cg_button_17", ["cg17_a", "cg17_c", "cg17_b"]),
        ("cg_button_4a", ["cg4a_1", "cg4a_2", "cg4a_3", "cg4a_4", "cg4a_5", "cg4a_6"]),
        ("cg_button_5", ["cg5_1", "cg5_2"]),
        ("cg_button_7", ["cg7_1", "cg7_3", "cg7_2", "cg7_4"]),
        ("cg_button_8", ["cg8_1", "cg8_2"]),
        ("cg_button_10", ["cg10_1", "cg10_2"]),
        ("cg_button_9", ["cg9_1", "cg9_2", "cg9_3", "cg9_4"]),
        ("cg_button_11", ["cg11_1", "cg11_2", "cg11_3", "cg11_4", "cg11_5", "cg11_6", "cg11_7"]),
        ("cg_button_12", ["cg12_1", "cg12_2", "cg12_3", "cg12_4", "cg12_5", "cg12_6", "cg12_7"]),
        ("cg_button_4b", ["cg4b_1", "cg4b_2", "cg4b_3", "cg4b_4", "cg4b_5"])

    ]

    gal_rows = 3
    gal_cols = 2
    thumbnail_x = 256
    thumbnail_y = 144

    gal_cells = gal_rows * gal_cols
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item[0])
        for img in gal_item[1]:
            g_cg.unlock_image(img)
    g_cg.transition = fade
    cg_page=0
    total_cg_items = len(gallery_cg_items)
    total_cg_page = math.ceil(total_cg_items/gal_cells)

init +1 python:
    for gal_item in gallery_cg_items:
        renpy.image (gal_item[0], im.Scale(ImageReference(gal_item[1][0]), thumbnail_x, thumbnail_y))


screen cg_gallery():
    tag menu
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"))
    use game_menu(_(""), scroll="viewport5"):
        add "gui/save_load/gallery.png":
            xpos 0.47
            ypos 0.05
        fixed:
            xpos 150

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            vbox:
                ## The page name, which can be edited by clicking on a button.
                button:
                    style "page_label"

                    key_events True
                    xalign 0.5

                    input:
                        style "page_label_text"
                        value page_name_value

                ## The grid of file slots.
                grid gal_rows gal_cols:
                    style_prefix "slot"

                    xalign 0.5
                    ypos 4

                    spacing gui.slot_spacing
                    $ i = 0
                    for gal_item in gallery_cg_items:
                        $ i += 1
                        if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                            add g_cg.make_button(gal_item[0], gal_item[0], im.Scale("gui/save_load/gallocked.png", thumbnail_x, thumbnail_y), xsize=thumbnail_x, ysize=thumbnail_y, idle_border=None, background=None)
                    for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                        null

                hbox:
                    style_prefix "page"

                    xalign 0.5
                    ypos 100

                    spacing gui.page_spacing

                    ## range(1, 10) gives the numbers from 1 to 9.
                    if total_cg_items>gal_cells:
                        for page in range(1, int(total_cg_page) + 1):
                            imagebutton auto "gui/save_load/dot_%s.png" action [FilePage(page), SetVariable('cg_page', page - 1)]
                            null width 10


    imagebutton auto "gui/overlay/return_%s.png" hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg":
        style "return_button"
        ypos 1.02
        xpos 0.93
        xsize 63
        ysize 83
        action Return()


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "music/UI Click.ogg"
    hover_sound "music/UI Hover.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    imagebutton auto "gui/quick/log_%s.png" action ShowMenu('history') xpos 670 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) xpos 735 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/next choice_%s.png" action Skip(fast=True, confirm=True) xpos 800 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/auto_%s.png" action Preference("auto-forward", "toggle") xpos 865 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/save_%s.png" action ShowMenu('save') xpos 930 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/load_%s.png" action ShowMenu('load') xpos 995 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/settings_%s.png" action ShowMenu('preferences') xpos 1060 ypos 658 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
    imagebutton auto "gui/quick/home_%s.png" action MainMenu() xpos 1122 ypos 625 focus_mask True hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xalign 0.5
        ypos gui.navigation_new_ypos

        spacing gui.navigation_spacing

        imagebutton auto "gui/main_menu/new_game_%s.png" action Start() hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"



    vbox:
        style_prefix "navigation"

        xalign 0.5
        ypos gui.navigation_continue_ypos

        spacing gui.navigation_spacing

        imagebutton auto "gui/main_menu/continue_%s.png" action ShowMenu("load") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"


    vbox:
        style_prefix "navigation"

        xalign 0.5
        ypos gui.navigation_preference_ypos

        spacing gui.navigation_spacing

        imagebutton auto "gui/main_menu/preferences_%s.png" action ShowMenu("preferences") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"


    vbox:
        style_prefix "navigation"

        xalign 0.5
        ypos gui.navigation_gallery_ypos

        spacing gui.navigation_spacing

        imagebutton auto "gui/main_menu/gallery_%s.png" action ShowMenu("cg_gallery") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"


    if renpy.variant("pc"):

        ## The quit button is banned on iOS and unnecessary on Android.
        vbox:
            style_prefix "navigation"

            xalign 0.5
            ypos gui.navigation_quit_ypos

            spacing gui.navigation_spacing

            imagebutton auto "gui/main_menu/quit_%s.png" action Quit(confirm=not main_menu) hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "viewport2":

                    viewport:
                        side_xsize 1200
                        side_xpos -280
                        side_ysize 800
                        side_ypos 0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "viewport3":

                    viewport:
                        side_xsize 1200
                        side_xpos -265
                        side_ysize 1000
                        side_ypos -95

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "viewport4":

                    viewport:
                        side_xsize 1200
                        side_xpos -265
                        side_ysize 1000
                        side_ypos -95

                        scrollbars "vertical"
                        mousewheel False
                        draggable False

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "viewport5":

                    viewport:
                        xsize 1200
                        xpos -280
                        ysize 800
                        ypos -80

                        scrollbars None
                        mousewheel False
                        draggable False

                        side_yfill False

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    imagebutton auto "gui/overlay/return_%s.png" hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg":
        style "return_button"
        ypos 1.02
        xpos 0.93
        xsize 63
        ysize 83
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 10
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 1280
    ysize 1000

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_(""))

    add "gui/save_load/save_title.png":
        xpos 0.36
        ypos 0.05


screen load():

    tag menu

    use file_slots(_(""))

    add "gui/save_load/load_title.png":
        xpos 0.36
        ypos 0.05



screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            xpos -170
            ypos -40

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 18):
                    imagebutton auto "gui/save_load/dot_%s.png" action FilePage(page)
                    null width 10


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Character Select screen ##########################################################
#####################################################################################
#####################################################################################

init:

    $ jun_page = False
    $ shoichi_page = False
    $ keisuke_page = False

screen hearts_bar(hearts, max_hearts):
    default top_move = 95
    default left_move = 100
    for i in range(hearts):
        add "gui/heart_filled.png":
            ypos top_move
            xpos left_move + i * 32
    for i in range(max_hearts - hearts):
        add "gui/heart_empty.png":
            ypos top_move
            xpos left_move + (hearts - 1) * 32 + (i + 1) * 32

    if jun_page:
        for i in range(junhearts):
            add "gui/heart_filled.png":
                        ypos top_move
                        xpos left_move + i * 32
        for i in range(8 - junhearts):
            add "gui/heart_empty.png":
                        ypos top_move
                        xpos left_move + (junhearts - 1) * 32 + i * 32

    elif shoichi_page:
        for i in range(shoichihearts):
            add "gui/heart_filled.png":
                        ypos top_move
                        xpos left_move + i * 32
        for i in range(3 - shoichihearts):
            add "gui/heart_empty.png":
                        ypos top_move
                        xpos left_move + (shoichihearts - 1) * 32 + i * 32

    elif keisuke_page:
        for i in range(keisukehearts):
            add "gui/heart_filled.png":
                        ypos top_move
                        xpos left_move + i * 32
        for i in range(5 - keisukehearts):
            add "gui/heart_empty.png":
                        ypos top_move
                        xpos left_move + (keisukehearts - 1) * 32 + i * 32



screen characterselect_jun():

    $ jun_page = True
    $ shoichi_page = False
    $ keisuke_page = False

    tag menu

    imagemap:
        ground "gui/CS_Jun.png"
        alpha False

        if junhearts == 0:
            hotspot (330, 185, 300, 410) action Call("junstart_0") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 1:
            hotspot (330, 185, 300, 410) action Call("junstart_1") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 2:
            hotspot (330, 185, 300, 410) action Call("junstart_2") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 3:
            hotspot (330, 185, 300, 410) action Call("junstart_3") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 4:
            hotspot (330, 185, 300, 410) action Call("junstart_4") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 5:
            hotspot (330, 185, 300, 410) action Call("junstart_5") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 6:
            hotspot (330, 185, 300, 410) action Call("junstart_6") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif junhearts == 7:
            hotspot (330, 185, 300, 410) action Call("junstart_7") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        else:
            hotspot (330, 185, 300, 410) action Call("junstart_0") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

        hotspot (258, 290, 38, 52) action ShowMenu("characterselect_keisuke") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        hotspot (622, 290, 38, 52) action ShowMenu("characterselect_shoichi") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

        use hearts_bar(junhearts, 8)


screen characterselect_shoichi():

    $ jun_page = False
    $ shoichi_page = True
    $ keisuke_page = False

    tag menu

    imagemap:
        ground "gui/CS_Shoichi.png"
        alpha False

        if shoichihearts == 0:
            hotspot (330, 185, 300, 410) action Start("shoichistart_0") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif shoichihearts == 1:
            hotspot (330, 185, 300, 410) action Start("shoichistart_1") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif shoichihearts == 2:
            hotspot (330, 185, 300, 410) action Start("shoichistart_2") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        else:
            hotspot (330, 185, 300, 410) action Start("shoichistart_0") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

        hotspot (258, 290, 38, 52) action ShowMenu("characterselect_jun") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        hotspot (622, 290, 38, 52) action ShowMenu("characterselect_keisuke") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

        use hearts_bar(shoichihearts, 3)


screen characterselect_keisuke():

    $ jun_page = False
    $ shoichi_page = False
    $ keisuke_page = True

    tag menu

    imagemap:
        ground "gui/CS_Keisuke.png"
        alpha False

        if keisukehearts == 0:
            hotspot (330, 185, 300, 410) action Start("keisukestart_0") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif keisukehearts == 1:
            hotspot (330, 185, 300, 410) action Start("keisukestart_1") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif keisukehearts == 2:
            hotspot (330, 185, 300, 410) action Start("keisukestart_2") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif keisukehearts == 3:
            hotspot (330, 185, 300, 410) action Start("keisukestart_3") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        elif keisukehearts == 4:
            hotspot (330, 185, 300, 410) action Start("keisukestart_4") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        else:
            hotspot (330, 185, 300, 410) action Start("keisukestart_0") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

        hotspot (258, 290, 38, 52) action ShowMenu("characterselect_shoichi") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
        hotspot (622, 290, 38, 52) action ShowMenu("characterselect_jun") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

        use hearts_bar(keisukehearts, 5)



## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_(""), scroll="viewport2"):

        null height (4 * gui.pref_spacing)

        vbox:

            hbox:
                box_wrap True
                style_prefix "radio"

                null width 194

                vbox:
                    add "gui/settings/display.png":
                        xpos 38
                    imagebutton auto "gui/settings/options/window_%s.png" action Preference("display", "any window") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"
                    imagebutton auto "gui/settings/options/fullscreen_%s.png" action Preference("display", "fullscreen") hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg"

                null width (6 * gui.pref_spacing)

                vbox:
                    add "gui/settings/skip.png":
                        xpos 100
                    imagebutton auto "gui/settings/options/seen_%s.png" hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg" action Preference("skip", "seen"):
                        xpos 200
                    imagebutton auto "gui/settings/options/all_%s.png" hover_sound "music/UI Hover.ogg" activate_sound "music/UI Click.ogg" action Preference("skip", "all"):
                        xpos 200

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (8 * gui.pref_spacing)

            hbox:
                vbox:
                    style_prefix "slider"
                    box_wrap True

                    hbox:
                        add "gui/settings/text.png":
                            xpos 0
                        bar value Preference("text speed"):
                            xpos 20
                            ypos 10

                    hbox:
                        add "gui/settings/auto.png":
                            xpos 0
                        bar value Preference("auto-forward time"):
                            xpos 20
                            ypos 50

                    hbox:
                         if config.has_music:
                            add "gui/settings/music.png":
                                xpos 0
                            bar value MixerValue('m2'):
                                xpos 0
                                ypos 17

                null width (2 * gui.pref_spacing)

                vbox:
                    style_prefix "slider"
                    box_wrap True

                    hbox:
                        if config.has_sound:
                            add "gui/settings/sound.png":
                                xpos 10
                            bar value Preference("sound volume"):
                                xpos 10
                                ypos 17

                    hbox:
                        if config.has_music:
                            add "gui/settings/ambiance.png":
                                xpos 10
                                ypos 30
                            bar value Preference("music volume"):
                                xpos 10
                                ypos 47

                    hbox:
                         if config.has_music:
                            add "gui/settings/music2.png":
                                ypos 60
                                xpos 10
                            bar value MixerValue('m3'):
                                xpos 10
                                ypos 77




    add "gui/settings/title.png":
        xpos 0.36
        ypos 0.05


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 180
    left_bar Frame("gui/slider/left.png", 10, 0)
    right_bar Frame("gui/slider/right.png", 10, 0)
    thumb None

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 180


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    frame:
        add "gui/overlay/log.png"
        xpos -4
        ypos -4
        style_prefix "history"

        viewport:

            draggable True

            vbox:
                for h in _history_list:

                    window:
                        ypos 50
                        xpos 40

                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        if h.who:

                            vbox:
                                spacing 10
                                label h.who:
                                    style "history_name"
                                    text_size gui.text_size
                                    text_font gui.text_font

                                    ## Take the color of the who text from the Character, if
                                    ## set.
                                    if "color" in h.who_args:
                                        text_color h.who_args["color"]

                                    else:
                                        text_color gui.text_color

                            text _(":"):
                                ypos 0.025
                                xpos 0.12
                                color gui.selected_color
                                size gui.text_size
                                font gui.text_font

                        text h.what:
                            font gui.text_font
                            size gui.text_size

                if not _history_list:
                    label _("The dialogue history is empty."):
                        ypos 50
                        text_color gui.selected_color
                        text_size gui.notify_text_size
                        text_font gui.text_font


    add "gui/save_load/log_title.png":
        xpos 120
        ypos 10


    imagebutton auto "gui/save_load/log_back_%s.png":
        xpos 1200
        ypos 630
        action Return()



style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xsize 1280
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize 900
    ysize 100
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes"):
                    action yes_action
                    text_color gui.hover_color

                textbutton _("No"):
                    action no_action
                    text_color gui.hover_color

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################
