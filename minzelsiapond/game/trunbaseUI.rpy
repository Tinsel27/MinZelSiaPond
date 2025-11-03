screen battle_ui():
    tag battle
    vbox:
        xalign 0.5
        yalign 0.3
        text "[enemy_obj.name]" size 24
        bar value enemy_obj.hp range enemy_obj.max_hp xsize 300 ysize 20
        text "[enemy_obj.hp] / [enemy_obj.max_hp]" color "#f66"
    vbox:
        xalign 0.5
        yalign 0.7
        text "[player_obj.name]" size 24
        bar value player_obj.hp range player_obj.max_hp xsize 300 ysize 20
        text "[player_obj.hp] / [player_obj.max_hp]" color "#6f6"
    # hbox:
    #     xalign 0.5
    #     yalign 0.9
    #     spacing 20
    #     textbutton "Attack":
    #         action Jump("player_turn")
    #     textbutton "Defend":
    #         action Jump("player_defend")
    #     textbutton "Heal":
    #         action Jump("player_heal")
