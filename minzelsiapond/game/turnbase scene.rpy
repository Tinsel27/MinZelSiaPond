
label battle_start:
    default player_obj = Actor("Hero", 100, 25)
    default enemy_obj = Actor("Goblin", 80, 15)
    python:
        player_obj.hp = player_obj.max_hp
        player_obj.is_dead = False
        player_obj.is_defend = False
        enemy_obj.hp = enemy_obj.max_hp
        enemy_obj.is_dead = False

    show screen battle_ui
    jump battle_loop


label battle_loop:
    if player_obj.is_dead:
        jump battle_lose
    elif enemy_obj.is_dead:
        jump battle_win
    else:
        menu:
            "Attack":
                jump player_turn
            "Defend":
                jump player_defend
            "Heal":
                jump player_heal


label player_turn:
    python:
        damage_dealt = player_obj.atk
        result_text = enemy_obj.take_damage(damage_dealt)
    "[result_text]"
    "เลือดศัตรูเหลือ [enemy_obj.hp]"
    if enemy_obj.is_dead:
        jump battle_win
    jump enemy_turn

label player_heal:
    python:
        healing_text = player_obj.heal()
    "[healing_text]"
    jump enemy_turn

label player_defend:
    python:
        player_obj.is_defend = True
    "[player_obj.name] ตั้งท่าป้องกัน!"
    jump enemy_turn

label enemy_turn:
    python:
        damage_taken = enemy_obj.atk
        result_text = player_obj.take_damage(damage_taken)
    "[result_text]"
    "เลือดของคุณเหลือ [player_obj.hp]"
    if player_obj.is_dead:
        jump battle_lose
    jump battle_loop
