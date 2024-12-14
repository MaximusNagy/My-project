import tkinter as tk
import random

# إعدادات اللعبة
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14), bg="black", fg="white")
        self.score_label.pack()

        self.restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=self.restart_game)
        self.restart_button.pack()

        self.initialize_game()

    def initialize_game(self):
        self.snake = [[5, 5], [5, 4], [5, 3]]  # جسم الثعبان
        self.food = [random.randint(0, (HEIGHT // CELL_SIZE) - 1),
                     random.randint(0, (WIDTH // CELL_SIZE) - 1)]
        self.direction = "Right"
        self.running = True

        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")

        self.draw_elements()
        self.bind_keys()
        self.move_snake()

    def draw_elements(self):
        self.canvas.delete("all")

        # رسم الثعبان
        for segment in self.snake:
            x, y = segment[1] * CELL_SIZE, segment[0] * CELL_SIZE
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="green", outline="")

        # رسم الطعام
        food_x, food_y = self.food[1] * CELL_SIZE, self.food[0] * CELL_SIZE
        self.canvas.create_oval(food_x, food_y, food_x + CELL_SIZE, food_y + CELL_SIZE, fill="red", outline="")

    def move_snake(self):
        if not self.running:
            return

        # حساب الرأس الجديد
        head = self.snake[0]
        if self.direction == "Right":
            new_head = [head[0], head[1] + 1]
        elif self.direction == "Left":
            new_head = [head[0], head[1] - 1]
        elif self.direction == "Up":
            new_head = [head[0] - 1, head[1]]
        elif self.direction == "Down":
            new_head = [head[0] + 1, head[1]]

        # التحقق من الاصطدام بالجدار أو بالجسم
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= HEIGHT // CELL_SIZE or
            new_head[1] < 0 or new_head[1] >= WIDTH // CELL_SIZE):
            self.end_game()
            return

        # إذا أكل الطعام
        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.food = [random.randint(0, (HEIGHT // CELL_SIZE) - 1),
                         random.randint(0, (WIDTH // CELL_SIZE) - 1)]
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

        self.draw_elements()
        self.root.after(100, self.move_snake)

    def change_direction(self, new_direction):
        # منع العودة للخلف
        if (new_direction == "Left" and self.direction != "Right") or \
           (new_direction == "Right" and self.direction != "Left") or \
           (new_direction == "Up" and self.direction != "Down") or \
           (new_direction == "Down" and self.direction != "Up"):
            self.direction = new_direction

    def bind_keys(self):
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))

    def end_game(self):
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24, "bold"))

    def restart_game(self):
        self.initialize_game()

# تشغيل اللعبة
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
