def play():
    print("正在玩魂斗罗......")


def gameover():
    # from mypack.menu import show_menu()
    from ..menu import show_menu
    show_menu()
    #from .tanks import play
    from ..games.tanks import play
    #from ...mypack.games.tanks import play #超过 顶层了 因为... 三个点


# 想在游戏调用借宿之后调用菜单 show_menu

print("魂斗罗模块被加载")
