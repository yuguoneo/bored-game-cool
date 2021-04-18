import time, random

name = str(input('你叫什么名字？  '))
print(' ')
print('队长%s,欢迎您！'%name)
print(' ')
time.sleep(1)

class Role():
    def __init__(self,name = '|角色|'):
        self.name = name
        self.life = random.randint(2400,3000)
        self.attack = random.randint(400,625)

class Sains_knight(Role):
    def __init__(self,name = '|圣光骑士·不灭神剑|'):
        Role.__init__(self,name)
        self.life = 5 * self.life
        self.attack = 3 * self.attack

    def fight_buff(self,enemy):
        if enemy == '|暗影刺客·黑暗之刃|':
            self.attack *= 1.5
            print('\n--圣光骑士对暗影刺客有克制效果！（下面这一局）--')
        else:
            self.attack = self.attack * 1.0

class Shadow_Assassin(Role):
    def __init__(self,name = '|暗影刺客·黑暗之刃|'):
        Role.__init__(self, name)
        self.life = 3 * self.life
        self.attack = 5 * self.attack

    def fight_buff(self,enemy):
        if enemy == '|精灵弩手·远古之弓|':
            self.attack *= 1.5
            print('\n--暗影刺客对精灵弩手有克制效果！（下面这一局）--')
        else:
            self.attack = self.attack * 1.0

class Faerie_Bowman(Role):
    def __init__(self,name = '|精灵弩手·远古之弓|'):
        Role.__init__(self, name)
        self.life = 4 * self.life
        self.attack = 4 * self.attack

    def fight_buff(self,enemy):
        if enemy == '|圣光骑士·不灭神剑|':
            self.attack *= 1.5
            print('\n--精灵弩手对圣光骑士有克制效果！（下面这一局）--')
        else:
            self.attack = self.attack * 1.0

class GAME():
    def __init__(self):
        self.players = []
        self.enemies = []
        self.show_title()
        self.show_role()
        self.order_role()
        self.pk_role()

    # 随机生成角色的属性
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Sains_knight(),Shadow_Assassin(),Faerie_Bowman()]))
            self.enemies.append(random.choice([Sains_knight(),Shadow_Assassin(),Faerie_Bowman()]))

    # 生成和展示角色信息
    def show_role(self):
        self.born_role()
        # 展示我方的3个角色
        print('-------------- 正在生成你的队伍 --------------')
        time.sleep(1)
        print('----------------- 角色信息 -----------------')
        print('%s的队伍：'%name)
        for i in range(3):
            print('%s %s  血量：%s  攻击：%s'
                  % (name,self.players[i].name,self.players[i].life,self.players[i].attack))
        print('--------------------------------------------')
        

        # 展示敌方的3个角色
        print('敌人队伍：')
        for i in range(3):
            print('敌方 %s  血量：%s  攻击：%s'
                  % (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')
        input('请按回车键继续...')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。
        print(' ')
        
    # 角色排序，选择出场顺序。
    def order_role(self):
        order_dict = {}
        for i in range(3):
            while True:
                ordersss = input('你想让{}第几个上场？（输入数字1~3）'.format(self.players[i].name))
                if ordersss == '1' or ordersss == '3' or ordersss == '2':
                    order = int(ordersss)
                    order_dict[order] = self.players[i]
                    break
                else:
                    print('-{选择失败！请重输}-')
                    
        self.players = []
        for i in range(1,4):
            self.players.append(order_dict[i])

        print('\n%s方的出场顺序是：%s、%s、%s' % (name,self.players[0].name, self.players[1].name, self.players[2].name))
        print('敌方的出场顺序是：%s、%s、%s' % (self.enemies[0].name, self.enemies[1].name, self.enemies[2].name))
        print('\n----------------- 角斗开始！----------------- ')
        

    # 角色PK
    def pk_role(self):
        round = 1
        score = 0
        for i in range(3):  # 一共要打三局
            player_name = self.players[i].name
            enemy_name = self.enemies[i].name
            #判断敌人是否对其有克制效果，有则进行攻击加成
            self.players[i].fight_buff(enemy_name)
            self.enemies[i].fight_buff(player_name)
            player_life = self.players[i].life
            player_attack = self.players[i].attack
            enemy_life = self.enemies[i].life
            enemy_attack = self.enemies[i].attack

            # 每一局开战前展示战斗信息
            print('\n----------------- 【第%s局】 -----------------' % round)
            print('%s角色：%s vs 敌方角色：%s ' % (name, player_name, enemy_name))
            print('%s %s 血量：%s  攻击：%s' % (name,player_name, player_life, player_attack))
            print('敌方 %s 血量：%s  攻击：%s' % (enemy_name, enemy_life, enemy_attack))
            print('--------------------------------------------')
            input('请按回车键继续...')
            print(' ')

            # 开始判断血量是否都大于零，然后互扣血量。
            while player_life > 0 and enemy_life > 0:
                if enemy_life > player_attack:
                    enemy_life = enemy_life - player_attack
                elif enemy_life <= player_attack:
                    enemy_life = int(0)
                if player_life > enemy_attack:
                    player_life = player_life - enemy_attack
                elif player_life <= enemy_attack:
                    player_life = int(0)
                print('%s %s发起攻击-敌方%s剩余血量%s' % (name, player_name, enemy_name, enemy_life))
                time.sleep(0.625)
                print('敌方 %s发起攻击-%s 方%s剩余血量%s' % (enemy_name, name, player_name, player_life))
                time.sleep(0.625)
                print('--------------------------------------------')
            else:  # 每局的战果展示，以及分数score和局数的变化。
                # 调用show_result()函数，打印返回元组中的result。
                print(self.show_result(player_life,enemy_life)[1])
                # 调用show_result()函数，完成计分变动。
                score += int(self.show_result(player_life,enemy_life)[0])
                round += 1
        input('\n--{[点击回车查看比赛结果]}--\n')

        if score > 0:
            print('---【VICTORY！】---\n')
        elif score < 0:
            print('---【DEFEAT！】---\n')
        else:
            print('---【NOUN！】---\n')

    # 返回单局战果和计分法所加分数。
    def show_result(self,player_life, enemy_life):  # 注意：该函数要设定参数，才能判断单局战果。
        if player_life > 0 and enemy_life <= 0:
            result = '\n胜利永远属于我们！'
            return 1, result
        elif player_life <= 0 and enemy_life > 0:
            result = '\n生当作人杰，死亦为鬼雄......'
            return -1, result
        else:
            result = '\n虽然我们失败了，但敌人也没赢！'
            return 0, result
    #展示标题
    def show_title(self):
        print('''--------------欢迎来到炼狱角斗场-----------------
在昔日的黄昏山脉，陆奥帝国的北境边界上，有传说中的‘炼狱角斗场'!
鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！
今日，只要【%s的队伍】能取得胜利，你将获得一笔够花500年的财富!
将随机生成【%s的队伍】和【敌人队伍】！'''% (name, name))
        print('''\n角色简介：
圣光骑士:一位西方来的圣骑士，平日里最看不起暗影刺客，但
有时会被精灵弩手的暗箭终结
---------------------------------------------
暗影刺客：东方的刺客，可以偷偷刺杀精灵弩手，但在圣光骑士
面前无计可施
---------------------------------------------
精灵弩手：丛林中玛雅部落的第十五代传人，射出的箭圣光骑士
无法防备，但常常被暗影刺客刺伤\n''')
        input('\n狭路相逢勇者胜，话不投机半句多(按回车键继续...)')
        print(' ')

while True:
    try:
        GAME_START = GAME()
    except:
        print('')
        print('发生了不知名的错误！！！')
        print('')
        print('该游戏将在5秒后重置！')
        print('')
        time.sleep(5)
        continue
    bbb = input('再玩一次？（按回车键继续或输入exit...）')
    if bbb == 'exit':
        print(' ')
        print('--我不玩了...--')
        break
    else:
        print(' ')

exec('exit()')
    
    
