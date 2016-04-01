import chapter3.section1
import chapter3.section3
import chapter3.section4
import chapter3.section5
import chapter3.section7

def load_chapter(tree, frame):
  tree.insert("", "end", "ch3", text="Chapter 3")
  chapter3.section1.load_section(tree, frame)
  chapter3.section3.load_section(tree, frame)
  chapter3.section4.load_section(tree, frame)
  chapter3.section5.load_section(tree, frame)
  chapter3.section7.load_section(tree, frame)
