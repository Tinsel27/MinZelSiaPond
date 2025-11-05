image fisser_battle="images/characters/monster.png"
screen battle_ui_2():
    tag battle
    vbox:
        xalign 0.5
        yalign 0.3
        text "[fisser_2.name]" size 24
        bar value fisser_2.hp range fisser_2.max_hp xsize 300 ysize 20
        text "[fisser_2.hp] / [fisser_2.max_hp]" color "#f66"
    vbox:
        xalign 0.5
        yalign 0.7
        text "[Lux_2.name]" size 24
        bar value Lux_2.hp range Lux_2.max_hp xsize 300 ysize 20
        text "[Lux_2.hp] / [Lux_2.max_hp]" color "#6f6"

label battle_2:
    scene void_bg
    show Lux_fight at player_po
    show fisser_battle at dummy_po
    default Lux_2 = Actor("Luxure", 10, 4,6,4,4)
    default fisser_2 = Actor("Fisser",8, 5,4,5,5)
    python:
        Lux_2.hp = Lux_2.max_hp
        Lux_2.is_dead = False
        fisser_2.hp = fisser_2.max_hp
        fisser_2.is_dead = False

    show screen battle_ui_2
    jump battle_2_loop


label battle_2_loop:
    if Lux_2.is_dead:
        "You Loss reset fight"
        jump battle_2
    elif fisser_2.is_dead:
        hide Lux_fight
        hide fisser_battle
        hide screen battle_ui_2
        return
    else:
        menu:
            "hex":
                jump hex_2
            "gun":
                jump gun_2
            "Heal":
                jump player_heal_2


label hex_2:
    python:
        damage_dealt = Lux_2.sp_atk
        enemy_def=fisser_2.sp_def
        result_text = fisser_2.take_damage(max(1,((damage_dealt//enemy_def)//50+2)))
    "[ result_text]"
    jump enemy_turn_2

label player_heal_2:
    python:
        healing_text = Lux_2.heal()
    jump enemy_turn_2

label gun_2:
    python:
        damage_dealt = Lux_2.atk
        enemy_def=fisser_2.defend
        result_text = fisser_2.take_damage(max(1,((damage_dealt//enemy_def)//50+2)))
    "[ result_text]"
    jump enemy_turn_2

label enemy_turn_2:
    python:
        damage_dealt = fisser_2.atk
        enemy_def=Lux_2.defend
        result_text = Lux_2.take_damage(((damage_dealt//enemy_def)//50+2))
    "[ result_text]"
    jump battle_2_loop
