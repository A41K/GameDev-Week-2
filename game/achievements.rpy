screen achievements():

    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):

        vbox:
            spacing 20

            frame:
                padding (20, 20)
                xfill True
                
                hbox:
                    spacing 20
                    vbox:
                        if achievement.has("First Theft"):
                            text "First Theft" color "#00ff00" size 30
                            text "You successfully stole a necklace!" size 22
                        else:
                            text "First Theft (Locked)" color "#808080" size 30
                            text "???" size 22

            frame:
                padding (20, 20)
                xfill True
                
                hbox:
                    spacing 20
                    vbox:
                        if achievement.has("Independent"):
                            text "Independent" color "#00ff00" size 30
                            text "You chose your own path." size 22
                        else:
                            text "Independent (Locked)" color "#808080" size 30
                            text "???" size 22

## Achievement Notification Screen

transform achievement_transform:
    on show:
        xalign 0.98 yalign 0.0
        yoffset -100 alpha 0.0
        easein 0.5 yoffset 20 alpha 1.0
    on hide:
        easeout 0.5 yoffset -100 alpha 0.0

screen achievement_popup(title):
    zorder 100
    frame at achievement_transform:
        background "#212121"
        padding (20, 15)
        
        hbox:
            spacing 10
            vbox:
                text "Advancement Made!" size 18 color "#FFFF55" 
                text title size 22 color "#FFFFFF"

    timer 4.0 action Hide("achievement_popup")
