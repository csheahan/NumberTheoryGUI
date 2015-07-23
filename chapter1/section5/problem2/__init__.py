from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section5.problem2.problem2

def load_problem_two(tree, frame):
  tree.insert("ch1.5", "end", "ch1.5.2", text="Problem 2", tags=["ch1.5.2"])
  tree.tag_bind("ch1.5.2", '<1>',
    functools.partial(problem_two_view, tree, frame))

def problem_two_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = "Enter an a and b in the division algorithm to find the "
  problemText += "quotient and remainder: a = b * q + r"
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    tree,
    frame,
    problemText,
    promptaText,
    promptbText,
    problem_two_display_answer
  )

def problem_two_display_answer(tree, frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section5.problem2.problem2.problem(
      int(a.get()),
      int(b.get())
    )

    answerLabelText = "The quotient is " + str(answer[0]) + " and the "
    answerLabelText += "remainder is " + str(answer[1]) + ", or in other "
    answerLabelText += "words, " + a.get() + " = " + b.get() + " * "
    answerLabelText += str(answer[0]) + " + " + str(answer[1])

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=5)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that a and b are "
    errorText += "integers"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=5)
