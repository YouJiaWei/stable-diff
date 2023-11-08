import time
epoch = 25

print("\n\n\n")
print("　"*(epoch-10) + "彡ﾉﾉﾊミ ⌒ミ")
print("　"*(epoch-11) + " (´・ω・｀)ω･｀)　今だ！オラごと撃て！")
print("　"*(epoch-11) + "⊂∩　　　　∩つ  ）")
print("　"*(epoch-11) + " /　　　〈　 〈")
print("　"*(epoch-11) + " (／⌒｀ Ｊ⌒し'")
print("\033[5A", end="")
flag = False
for i in range(epoch):
    bar = "\033[33m弌"*i + "⊃\033[37m"
    print("\r\033[32mにｱ" + bar, end="")
    if i == int(epoch*0.25):
        print("\033[E", end="")
        print("　"*(epoch-11) + " (´・ω・｀)ω･｀)　離せっ！！オ…オレが悪かった！！", end="")
        print("\033[A", end="")
    elif i == int(epoch*0.5):
        flag = True
        print("\033[E", end="")
        print("　"*(epoch-11) + " (´；ω；｀)ω^｀)　ぐ…！！ち…ちくしょおおお！！！", end="")
        print("\033[A", end="")
    if flag:
        if i == int(epoch*0.5)+1:
            print("\033[F", end="")
            print("　"*(epoch-9)  + "ﾉ")
        elif i == int(epoch*0.5)+3:
            print("\033[2F", end="")
            print("　"*(epoch-8)  + "ﾉ")
            print("　"*(epoch-9)  + "彡　ノ")
        elif i == int(epoch*0.5)+5:
            print("\033[3F", end="")
            print("　"*(epoch-5)  + "ﾉ")
            print("　"*(epoch-8)  + "彡　ノ")
            print("　"*(epoch-9)  + "ノ")
        elif i == int(epoch*0.5)+7:
            print("\033[4F", end="")
            print("　"*(epoch-3)  + "ﾉ")
            print("　"*(epoch-6)  + "彡　ノ")
            print("　"*(epoch-8)  + "ノ")
            print("　"*(epoch-9)  + "ﾉノ　　　ミ　ﾉノ")
    time.sleep(0.25)
print()
print("\033[5B", end="")
