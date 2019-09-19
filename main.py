from unit1.project.game_gobang.gameview import GameView

if __name__ == "__main__":
    view = GameView()
    view.start()
    view.update()


# 改进：
# 游戏结束后应该提示是否再来一局
# 当一个格有棋子了，玩家还想在此格放棋子，应弹出提示此格已有棋子请选择其他格