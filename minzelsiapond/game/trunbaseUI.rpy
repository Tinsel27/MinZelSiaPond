screen battle_ui:
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