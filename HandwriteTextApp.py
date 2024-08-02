import pywhatkit as pw


pw.start_server()
txt="""Hello this is a handrwiting app who can help you to make normal text to handwrite text and it's very cool this feature with python"""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" END   ")
