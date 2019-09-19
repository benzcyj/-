import random

class GameController:

    def __init__(self):
        # self.__list_0_location = []
        self.__board = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]

        ]

    @property
    def board(self):
        return self.__board

    def start_build_chess(self):
        __list_0_location = []
        for r in range(len(self.__board)):
            for c in range(len(self.__board[r])):
                if self.__board[r][c] == 0:
                    __list_0_location.append((r, c))
        location = random.choice(__list_0_location)
        self.__board[location[0]][location[1]] = 2
        return 4

    def row_build_chess(self):
        for r in range(len(self.__board)):
            __list_0_location = []
            i = 0
            j = 0
            for c in range(len(self.__board[r])):
                if self.__board[r][c] == 0:
                    __list_0_location.append((r,c))
                    j += 1
                if self.__board[r][c] == 1:
                    i += 1
            if j <= 1:
                return
            # if i == 3:
            #     location = random.choice(__list_0_location)
            #     self.__board[location[0]][location[1]] = 2
            #     return 1
            if i == 2:
                location = random.choice(__list_0_location)
                self.__board[location[0]][location[1]] = 2
                return 1

    def line_build_chess(self):
        for a in range(len(self.__board)):
            c = 0
            y = 0
            list01 = []
            zero_location = []
            for b in self.__board:
                list01.append(b[a])
            for item in range(len(list01)):
                if list01[item] == 1:
                    c += 1
                if list01[item] == 0:
                    zero_location.append(item)
                    y += 1
            if y <= 1:
                return
            # if c == 3:
            #     d = random.choice(zero_location)
            #     self.__board[d][a] = 2
            #     return 2
            if c == 2:
                d = random.choice(zero_location)
                self.__board[d][a] = 2
                return 2

    def oblique_build_chess(self):
        a = 0
        b = 0
        h = 0
        g = 0
        __list_0_01 = []
        __list_0_02 = []
        for i in range(len(self.__board)):
            if self.__board[i][i] == 1:
                a += 1
            if self.__board[i][i] == 0:
                __list_0_01.append((i,i))
                h += 1
            if self.__board[i][-(i+1)] == 1:
                b += 1
            if self.__board[i][-(i+1)] == 0:
                __list_0_02.append((i,-(i+1)))
                g += 1
        if h <= 1:
            return
        # if a == 3:
        #     d = random.choice(__list_0_01)
        #     self.__board[d[0]][d[1]] = 2
        #     return 3
        if a == 2:
            d = random.choice(__list_0_01)
            self.__board[d[0]][d[1]] = 2
            return 3
        if g <= 1:
            return
        # if b == 3:
        #     d = random.choice(__list_0_02)
        #     self.__board[d[0]][d[1]] = 2
        #     return 3
        if b == 2:
            d = random.choice(__list_0_02)
            self.__board[d[0]][d[1]] = 2
            return 3

    def random_build_chess(self):
        """
        # 逻辑生成棋子：当任意一行，一列或对角线有两个或以上的１，应优先在此行/列/对角线随机生成２
        :return:
        """
        if self.row_build_chess():
            return
        elif self.line_build_chess():
            return
        elif self.oblique_build_chess():
            return
        # if self.row_build_chess() or \
        #         self.line_build_chess() or \
        #         self.oblique_build_chess():
        #     return
        elif self.start_build_chess():
            return

    def input_chess(self,row=0,line=0):
        """
        当一个格有棋子了，玩家还想在此格放棋子，应弹出提示此格已有棋子请选择其他格
        :param row:
        :param line:
        :return:
        """
        # if self.__board[row-1][line-1] == 2:
        #     print("请重新输入棋子位置")
        #     return 1
        if self.__board[row-1][line-1] != 1 and self.__board[row-1][line-1] != 2:
            self.__board[row-1][line-1] = 1

    def player_row_win(self):
        for a in range(len(self.__board)):
            for b in range(len(self.__board[a])-1):
                i = 0
                for c in range(b+1,len(self.__board[a])):
                    if self.__board[a][b] == self.__board[a][c] == 1:
                        i += 1
                        continue
                    else:
                        break
                if i == 4:
                    return 1
                else:
                    break

    def player_line_win(self):
        for c in range(len(self.__board)):
            for a in range(len(self.__board)-1):
                i = 0
                for b in range(a+1,len(self.__board)):
                    if self.__board[a][c] == self.__board[b][c] == 1:
                        i += 1
                        continue
                    else:
                        break
                if i == 4:
                    return 1
                else:
                    break

    def player_oblique_win(self):
        a = 0
        b = 0
        for i in range(len(self.__board)-1):
            if self.__board[i][i] == self.__board[i+1][i+1] == 1:
                a += 1
            if self.__board[i][-(i+1)] == self.__board[i+1][-(i+2)] == 1:
                b += 1
        if a == 4 or b == 4:
            return 1

    def system_row_win(self):
        for a in range(len(self.__board)):
            for b in range(len(self.__board[a])-1):
                i = 0
                for c in range(b+1,len(self.__board[a])):
                    if self.__board[a][b] == self.__board[a][c] == 2:
                        i += 1
                        continue
                    else:
                        break
                if i == 4:
                    return 2
                else:
                    break

    def system_line_win(self):
        for c in range(len(self.__board)):
            for a in range(len(self.__board)-1):
                i = 0
                for b in range(a+1,len(self.__board)):
                    if self.__board[a][c] == self.__board[b][c] == 2:
                        i += 1
                        continue
                    else:
                        break
                if i == 4:
                    return 2
                else:
                    break

    def system_oblique_win(self):
        a = 0
        b = 0
        for i in range(len(self.__board)-1):
            if self.__board[i][i] == self.__board[i+1][i+1] == 2:
                a += 1
            if self.__board[i][-(i+1)] == self.__board[i+1][-(i+2)] == 2:
                b += 1
        if a == 4 or b == 4:
            return 2

    def draw(self):
        """
        # 平局算法应该为任意一行，一列或对角线都有至少有一个１和２才算平局
        :return: 3
        """
        s = 0
        for a in self.__board:
            if 1 and 2 in a:
                s += 1

        for b in range(len(self.__board)):
            list01 = []
            for c in self.__board:
                list01.append(c[b])
            if 1 and 2 in list01:
                s += 1

        list02 = []
        list03 = []
        for z in range(len(self.__board)):
            list02.append(self.__board[z][z])
            list03.append(self.__board[z][-(z+1)])
        if 1 and 2 in list02:
            s += 1
        if 1 and 2 in list03:
            s += 1

        if s == 12:
            return 3



if __name__ == "__main__":
    controller = GameController()






