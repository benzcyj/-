import os

from unit1.project.game_gobang.gamecontroller import GameController


class GameView:
    def __init__(self):
        self.__controller = GameController()

    def start(self):
        # self.__controller.start_build_chess()
        self.__controller.random_build_chess()
        self.__print_map()

    def __print_map(self):
        os.system("clear")

        for line in self.__controller.board:
            for item in line:
                print(item,end=" ")
            print()

    def update(self):
        while True:
            row = int(input("请输入要放棋子的行:"))
            line = int(input("请输入要放棋子的列:"))
            self.__controller.input_chess(row,line)
            # if self.__controller.input_chess() == 1:
            #     continue
            self.__controller.random_build_chess()
            self.__print_map()
            if self.__controller.player_row_win() == 1 or\
                    self.__controller.player_line_win() == 1 or\
                    self.__controller.player_oblique_win() == 1:
                print("你赢了！")
                break
            if self.__controller.system_row_win() == 2 or\
                self.__controller.system_line_win() == 2 or\
                self.__controller.player_oblique_win() == 2:
                print("你输了！")
                break
            if self.__controller.draw() == 3:
                print("平局！")

