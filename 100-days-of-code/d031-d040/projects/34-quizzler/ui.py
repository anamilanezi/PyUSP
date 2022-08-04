import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Consolas", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question will appear here!",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     justify="center",
                                                     font=("Consolas", 16, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_bt = tk.Button(image=false_img,
                                  highlightthickness=0,
                                  borderwidth=0,
                                  command=self.answer_false)
        self.false_bt.grid(column=0, row=2)

        true_img = tk.PhotoImage(file="images/true.png")
        self.true_bt = tk.Button(image=true_img,
                                 highlightthickness=0,
                                 borderwidth=0,
                                 command=self.answer_true)
        self.true_bt.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
            self.buttons_state("active")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\n"
                                                            f"Your final score is {self.quiz.score} ")

            self.buttons_state("disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.true_bt.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.false_bt.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#29b677")
            self.update_score()
        else:
            self.canvas.config(bg="#ee665d")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        score_text = self.quiz.score
        self.score_label.config(text=f"Score: {score_text}")

    def buttons_state(self, state):
        self.true_bt.config(state=state)
        self.false_bt.config(state=state)
