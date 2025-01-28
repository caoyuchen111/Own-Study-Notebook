def log_in():
    from pathlib import Path
    import json
    path=Path("password.json")
    contents=path.read_text()
    password=json.loads(contents)
    if password=="None":
        print("为了信息安全，请设置一个密码！")
        while 1:
            password1=input("请输入：")
            password2=input("请再次输入：")
            if password1==password2:
                contents=json.dumps(password1)
                path.write_text(contents)
                print("登陆成功！")
                break
            else:
                print("两次输入不匹配！")
                continue
    else:
        print("请输入你的密码！")
        while 1:
            password1=input("请输入：")
            if password1==password:
                print("登陆成功！")
                break
            else:
                print("密码错误！")
                continue

