from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section1.problem1.problem1

def load_problem_one(tree, frame):
  tree.insert("ch1.1", "end", "ch1.1.1", text="Problem 1", tags=["ch1.1.1"])
  tree.tag_bind("ch1.1.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = u"Given a number \u03B1, find rational number p/q such that "
  problemText += u"|\u03B1 - p/q| \u2264 1/q^2"
  promptText = u"Enter an integer \u03B1:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_one_display_answer
    )

def problem_one_display_answer(frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section1.problem1.problem1.problem(int(alpha.get()))

    answerText = Label(frame, text=u"With an \u03B1 of " +
      unicode(int(alpha.get())) + u" we have the inequality " +
      unicode(answer[0][2]) + u" \u2264 " + unicode(answer[0][3]) +
      u" when p=" + unicode(answer[0][0]) + u" and q=" +
      unicode(answer[0][1]))
    
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = u"An error has occurred. Please ensure that \u03B1 is an"
    errorText += u" integer"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)
