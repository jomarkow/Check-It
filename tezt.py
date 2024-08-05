import easygui
# importing easygui module
from easygui import *
 
text = "Enter the following details"
title = "Window Title GfG"
input_list = ["Geek Name", "Geek ID", "Experience"]
output = multenterbox(text, title, input_list)
title = "Message Box"
message = "Entered details are in form of list : " + str(output)
msg = msgbox(message, title)