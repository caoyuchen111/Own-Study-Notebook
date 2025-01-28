def settings():
    print("设置选项：1.修改密码；2.销毁数据")
    b=int(input("请输入选项（输入数字即可）"))
    if b==2:
        import os
        os.remove("password.json")
        os.remove("notes.json")
    if b==1:
        from pathlib import Path
        import json
        path=Path("password.json")
        contents=path.read_text()
        password=json.loads(contents)
        password1=input("请输入原密码:")
        if password!=password1:
            print("输入错误！")
        else:
            password2=input("请输入新密码：")
            password3=input("请再次输入新密码：")
            if password2 != password3:
                print("两次输入不匹配！")
            else:
                print("修改成功！")
                path=Path("password.json")
                contents=json.dumps(password2)
                path.write_text(contents)
