screen team_battle_ui(current_actor):
    modal True
    hbox:
        xalign 0.5 yalign 0.1
        spacing 20
        for enemy in enemies:
            if not enemy.is_dead:
                vbox:
                    text enemy.name
                    bar value enemy.hp range enemy.max_hp xsize 200
                    text f"{enemy.hp}/{enemy.max_hp}"
    hbox:
        xalign 0.5 yalign 0.8
        spacing 20
        for member in party:
            $ style = "battle_member_box"
            if member == current_actor:
                $ style = "battle_member_box_active"

            vbox style style:
                text member.name
                bar value member.hp range member.max_hp xsize 200
                text f"{member.hp}/{member.max_hp}"

    if current_actor.is_player:
        vbox:
            xalign 0.1 yalign 0.5
            textbutton "โจมตี" action Return("attack")
            textbutton "ป้องกัน" action Return("defend")