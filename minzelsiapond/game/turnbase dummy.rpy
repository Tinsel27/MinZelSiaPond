image dummy_fight_bg="images/bg/Traning_Room.png"
image dummy="images/characters/dummy.png"
transform dummy_po:
    xalign 0.9       # position to the left
    yalign 1       # stick to the bottom
    zoom 10
label battle_dummy:
    $ player_obj = Actor("Luxure", 10, 4,6,4,4)
    $ enemy_obj = Actor("Dummy",99999999, 0,0,99999999,99999)
    python:
        player_obj.hp = player_obj.max_hp
        player_obj.is_dead = False
        enemy_obj.hp = enemy_obj.max_hp
        enemy_obj.is_dead = False

    show screen battle_ui
    jump loop_dummy


label loop_dummy:
    scene dummy_fight_bg
    show dummy at dummy_po
    show Lux_fight at player_po
    if player_obj.is_dead:
        jump battle_lose
    elif enemy_obj.is_dead:
        jump battle_win
    else:
        menu:
            "hex":
                jump hex
            "gun":
                jump gun
            "Heal":
                jump player_heal
            "Continue":
                hide dummy
                hide Lux_fight
                hide screen battle_ui
                return


label hex:
    python:
        damage_dealt = player_obj.sp_atk
        enemy_def=enemy_obj.sp_def
        result_text = enemy_obj.take_damage(max(1,((damage_dealt//enemy_def)//50+2)))
    "[ result_text]"
    jump enemy_turn

label player_heal:
    python:
        healing_text = player_obj.heal()
    jump enemy_turn

label gun:
    python:
        damage_dealt = player_obj.atk
        enemy_def=enemy_obj.defend
        result_text = enemy_obj.take_damage(max(1,((damage_dealt//enemy_def)//50+2)))
    "[ result_text]"
    jump enemy_turn

label enemy_turn:
    python:
        damage_dealt = enemy_obj.atk
        result_text = player_obj.take_damage(((damage_dealt//enemy_def)//50+0))
    "[ result_text]"
    jump loop_dummy
