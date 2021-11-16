from tkinter import *

game_width = 500 #ширина оуна игры
game_height = 500 #длина окна игры
shake_item = 10 #размер 1 элемента змейки
snake_coloor1 = "red"
snake_coloor2 = "black"

tk = Tk()
tk.title("Змейка Питон") #заголовок окна
tk.resizable(0, 0) #нельзя масштабировать окно
tk.attributes("-topmost", 1) # поверх всех окон
canvas = Canvas(tk, width = game_width, height = game_height, bd = 0, highlightthickness = 0) #параметры канваса, стороны и границы
canvas.pack() #запаковка канваса
tk.update()

def snake_paint_item(canvas, x, y):
    canvas.create_rectangle(x * shake_item, y * shake_item, x * shake_item + shake_item, y * shake_item + shake_item, fill = snake_coloor1)
    canvas.create_rectangle(x * shake_item + 2, y * shake_item + 2, x * shake_item + shake_item - 2, y * shake_item + shake_item - 2, fill = snake_coloor2)

snake_paint_item(canvas, 1, 1)
snake_paint_item(canvas, 49, 49)
