def main():
    import log_in
    import sys
    import settings
    import notes
    log_in.log_in()
    while 1:
        print("请输入选项（输入数字即可）")
        a=int(input("1.退出 2.设置 3.有关笔记/l"))
        if a==1:
            sys.exit()
        if a==2:
            settings.settings()
        if a==3:
            notes.notes()