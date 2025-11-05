image Unknow_figth="images/characters/unknown_fight.png"
image Lux_fight="images/characters/Lux_fight.png"
image void_bg="images/bg/The_Void.png"
transform enemy_po:
    xalign 0.9       # position to the left
    yalign 1       # stick to the bottom
    zoom 5
transform player_po:
    xalign 0.1       # position to the left
    yalign 0.9      # stick to the bottom
    zoom 0.5
screen battle_ui_1():
    tag battle
    vbox:
        xalign 0.5
        yalign 0.3
        text "[enemy_1.name]" size 24
        bar value enemy_1.hp range enemy_1.max_hp xsize 300 ysize 20
        text "[enemy_1.hp] / [enemy_1.max_hp]" color "#f66"
    vbox:
        xalign 0.5
        yalign 0.7
        text "[Lux_1.name]" size 24
        bar value Lux_1.hp range Lux_1.max_hp xsize 300 ysize 20
        text "[Lux_1.hp] / [Lux_1.max_hp]" color "#6f6"

label battle_1:
    scene void_bg
    show unknown_fight at enemy_po
    show Lux_fight at player_po
    default Lux_1 = Actor("Luxure", 10, 4,6,4,4)
    default enemy_1 = Actor("Unknow",1000, 1000,1000,1000,1000)
    python:
        Lux_1.hp = Lux_1.max_hp
        Lux_1.is_dead = False
        enemy_1.hp = enemy_1.max_hp
        enemy_1.is_dead = False

    show screen battle_ui_1
    jump battle_1_loop


label battle_1_loop:
    if Lux_1.is_dead:
        jump battle_lose
    elif enemy_1.is_dead:
        jump battle_win
    else:
        menu:
            "hex":
                jump hex_1
            "gun":
                jump gun_1
            "Heal":
                jump player_heal_1


label hex_1:
    python:
        damage_dealt = Lux_1.sp_atk
        enemy_def=enemy_1.sp_def
        result_text = enemy_1.take_damage(max(1,((damage_dealt//enemy_def)//50+2)))
    "[result_text]"
    if enemy_1.is_dead:
        jump battle_win
    jump dimensional

label player_heal_1:
    python:
        healing_text = Lux_1.heal()
    "[healing_text]"
    jump dimensional

label gun_1:
    python:
        damage_dealt = Lux_1.atk
        enemy_def=enemy_1.defend
        result_text = enemy_1.take_damage(max(1,((damage_dealt//enemy_def)//50+2)))
    "[result_text]"
    if enemy_1.is_dead:
        jump battle_win
    jump dimensional

label dimensional:
    python:
        Lux_1.hp=1
    "Luxure take 9 damage"
    hide Unknow_figth
    hide Lux_fight
    hide screen battle_ui_1
    return
