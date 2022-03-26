from vbspython import makefile

file = makefile()

file.input(text="What is the message you want to send?", getvar=True)
strtosend = file.run()

file.input(text="How much times do you want to send the message", getvar=True)
amount = file.run()

file.msgbox(text="Press enter to start sending the messages")
file.sleep(2)
file.run()

file2 = makefile()
file2.presskeys(strtosend.rstrip("\n"))
file2.presskey("ENTER")
for i in range(int(amount)):
    file2.run(deletefile=False)
