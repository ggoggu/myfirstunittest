def aabbcollision(a,b):
    return ((abs((a.xpos + a.width/2) - (b.xpos + b.width/2)) <= a.width/2 + b.width/2) and (abs((a.ypos + a.height/2) - (b.ypos + b.height/2)) <= a.height/2 + b.height/2))

def gameend2(player, boss):
    if(player.life <= 0):
        print("you are lose")
        return 0
    elif(boss.life <= 0):
        print("you are win")
        return 1
    else:
        return -1

def attack(player,mob):
    if(aabbcollision(player,mob)):
        player.life -= mob.attack