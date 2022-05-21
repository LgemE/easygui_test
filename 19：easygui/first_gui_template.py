import easygui as gui
import sys
#最初欢迎界面
gui.msgbox("Let's start the interview !!",title = "Your favorite team in NBA", ok_button = "All right!", image = "开始1.gif")
while 1:
    
    msg1 = "What's your favorite team?"
    title = "Your favorite team in NBA"
    choices = ["Golden State Warriors", "The Lakers", "Heat", "Spurs"]      #四个球队
    players = ["Curry", "God Tang", "KD", "Kobe", "Magic", "Shark", "Wade", "Bosh", "Butler", "Duncan", "Parker", "Ginobili"]
    choice = gui.choicebox(msg1, title, choices)
    print(choice)

    #分别添加四个球队的球员
    msg2 = "Why do you like " + str(choice) + " ?" + " Pick one player you like best below!"
    button1_choices = ["Curry", "God Tang", "KD"]
    button2_choices = ["Kobe", "Magic", "Shark"]
    button3_choices = ["Wade", "Bosh", "Butler"]
    button4_choices = ["Duncan", "Parker", "Ginobili"]

    if choice == choices[0]:
        button_choice = gui.buttonbox(msg2, title, button1_choices, image = "勇士1.gif")
    if choice == choices[1]:
        button_choice = gui.buttonbox(msg2, title, button2_choices, image = "湖人1.gif")
    if choice == choices[2]:
        button_choice = gui.buttonbox(msg2, title, button3_choices, image = "热火1.gif")
    if choice == choices[3]:
        button_choice = gui.buttonbox(msg2, title, button4_choices, image = "马刺1.gif")
     
    print(button_choice)

    gui.enterbox("Why you worship him in that crazy way??", title = "? Favorite player ?", image = "崇拜1.gif")
    #12球员
    if button_choice == players[0]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "库里1.gif")
    if button_choice == players[1]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "汤普森1.gif")
    if button_choice == players[2]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "杜兰特1.gif")
    if button_choice == players[3]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "科比1.gif")
    if button_choice == players[4]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "魔术师1.gif")
    if button_choice == players[5]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "奥尼尔1.gif")
    if button_choice == players[6]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "韦德1.gif")
    if button_choice == players[7]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "波什1.gif")
    if button_choice == players[8]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "巴特勒1.gif")
    if button_choice == players[9]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "邓肯1.gif")
    if button_choice == players[10]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "帕克1.gif")
    if button_choice == players[11]:
        gui.enterbox("Say something to your favorite player", title = "! Favorite player !", image = "吉诺比利1.gif")

    msg = "It's the end of this interview. You wanna do it again?"
    if gui.ccbox(msg, title, image = "结束1.gif"):
        pass
    else:
        sys.exit(0)



