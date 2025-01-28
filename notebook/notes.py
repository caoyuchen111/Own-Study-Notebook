import json
from pathlib import Path
def notes():
    path = Path("notes.json")
    
    # Read the content of the file if it exists
    if path.exists():
        contents = path.read_text()
        notes = json.loads(contents)
    else:
        notes = {}

    # Check if the notes are empty, and create a default topic
    if not notes:
        print("你还没有任何主题，请创建一个！")
        subject = input("请输入主题名：")
        notes[subject] = "None"
        print("创建成功！")

    while True:
        print("请输入你要操作的选项（填数字即可）：1.查看所有主题；2.退出")
        op = int(input(" "))
        
        if op == 2:
            # Save the notes to the file before exiting
            contents = json.dumps(notes, ensure_ascii=False, indent=4)
            path.write_text(contents)
            break
        
        # List all topics
        k = []
        for i in notes.keys():
            print(i)
            k.append(i)  # Corrected append method
        
        print("请输入下一步操作：1.退出 2.删除主题 3.添加主题 4.浏览主题")
        op = int(input(" "))

        if op == 1:
            # Save the notes to the file before exiting
            contents = json.dumps(notes, ensure_ascii=False, indent=4)
            path.write_text(contents)
            break
        
        elif op == 2:
            # Delete a theme
            o = input("请输入主题名：")
            if o not in k:
                print("此主题不存在！")
            else:
                del notes[o]
                print(f"主题 {o} 已删除！")
        
        elif op == 3:
            # Add a new theme
            o = input("请输入主题名：")
            if o in k:
                print("该主题已存在！")
            else:
                l = input("请输入内容：")
                notes[o] = l
                print("主题添加成功！")
        
        elif op == 4:
            # Browse a specific theme
            o = input("请输入主题编号：")
            if o not in k:
                print("此主题不存在！")
            else:
                print(f"主题内容：{notes[o]}")

