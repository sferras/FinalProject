from tkinter import*
from PIL import Image, ImageTk

window = Tk()
window.title("Welcome")
window.resizable(0, 0)

name = StringVar()
result_list = []

def ole():
    nombre = entry1.get()
    country = var.get()
    welcoming = "Hello "+nombre+" from "+country+", welcome to this game"
    label_resumen["text"] = welcoming


def game():
    nombre = entry1.get()
    country = var.get()
    import pygame
    import random
    from matplotlib import pylab as plt

    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("Arial", 20, "bold")
    score_font = pygame.font.SysFont("Bauhaus 93", 35)

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, black)
        dis.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 50, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = int(1)

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(red)
                message("You Lost! Press: C-play again, Q-exit, R-check results", yellow)
                Your_score(Length_of_snake - 1)
                result_list.append(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
                        if event.key == pygame.K_r:
                            plt.figure("First")
                            plt.title("Here is your progress " + nombre + " from " + country)
                            plt.plot(result_list)
                            plt.show()
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(green)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()

imge = Image.open("C:/Users/sergi/Desktop/snakelogo2.jpg")
photo = ImageTk.PhotoImage(imge)

lab0 = Label(image=photo, width=800, bg="light green")
lab0.grid()

labsnake = Label(master=window, text="SNAKE", width=47, font=("Calibri",25, "bold"), fg="green", bg="light green")
labsnake.grid(row=1, column=0)

lab1 = Label(master=window, text="Name > > >", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab1.grid(row=2, column=0, sticky="w")

entry1 = Entry(window, textvar=name, bg="light green")
entry1.grid(row=2, column=0)

lab2 = Label(master=window, text=" < < < Name", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab2.grid(row=2, column=0, sticky="e")

lab3 = Label(master=window, text="Country > > >", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab3.grid(row=3, column=0, sticky="w")

var = StringVar()
list1 = ["Argentina", "Spain", "Venezuela", "Italy", "Portugal", "USA", "France", "Morocco", "Egypt", "Kazakhstan", "Lebanon", "Romania", "Belgium"]
droplist = OptionMenu(window, var, *list1)
var.set("Select BIS nationality")
droplist.config(width=20, bg="light green")
droplist.grid(row=3, column=0)

lab4 = Label(master=window, text=" < < < Country", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab4.grid(row=3, column=0, sticky="e")

lab5 = Label(master=window, text="What do you want to do?", width=47, font=("Calibri", 25, "bold"), fg="green", bg="light green")
lab5.grid(row=4, column=0)

label_resumen = Label(master=window, width=47, font=("Calibri", 25, "bold"), fg="green", bg="light green")
label_resumen.grid(row=6, column=0)

bt1 = Button(master=window, text="Play", width=24, font=("Arial", 15, "bold"), fg="green", bg="light green", command=game)
bt1.grid(row=5, column=0, sticky="w")

bt3 = Button(master=window, text="Welcome", width=24, font=("Arial", 15, "bold"), fg="green", bg="light green", command=ole)
bt3.grid(row=5, column=0)

bt2 = Button(master=window, text="Exit", width=24, font=("Arial", 15, "bold"), fg="green", bg="light green", command=sys.exit)
bt2.grid(row=5, column=0, sticky="e")

window.mainloop()