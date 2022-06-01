from mouse import move, click
from random import randrange
from time import sleep, time, strftime
from datetime import datetime, timedelta

def afk_start(min: int) -> None:

    try:
        start = time()
        target_hour = (datetime.now() + timedelta(minutes= min)).strftime("%Y-%m-%d %H:%M")

        print(f"AFK iniciado: {datetime.now().strftime('%Y-%m-%d %H:%M')} com término definido às {target_hour}")
        while datetime.now().strftime("%Y-%m-%d %H:%M") != target_hour:
            pos = []
            for i in range(2):
                pos.append(randrange(0, 1000))
            sleep(2)

            move(x=pos[0],y=pos[1])
            sleep(5)

            move(x=21, y=1055)
            click()

        else:
            print("AFK foi finalizado")
            exit(0)

    except(KeyboardInterrupt):
        end = time()
        print(f"AFK Interrompido após: {('%.2f' % (end - start))} segundos")
            
afk_start(min= 40)