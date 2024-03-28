import time
import csv

start_timer=time.time()



with open("16.csv","r") as file:
    print(file.read())

    timer1=time.time()-start_timer
    print(f"\nЗатрачено времени на чтение: {timer1} секунд.")

    start_timer=time.time()
    reader=csv.reader(file)

    for row in reader:
        print(row)

    timer3=time.time()-start_timer

    print(f"\nЗатрачено времени на чтение: {timer3} секунд.")

    timer2=time.time()-start_timer
  

    start_timer=time.time()

    data=map(str.split, file)
    data=list(data)

    timer2=time.time()-start_timer

    print(f"\nЗатрачено времени на чтение: {timer1} секунд.")
    print(f"\nЗатрачено времени на чтение: {timer2} секунд.")
    print(f"\nЗатрачено времени на чтение: {timer3} секунд.")


    print(data)