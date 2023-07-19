from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from street_clip import predict, hiyoshi_maps

root = Tk()
root.title('Image Viewer')

# open image
def open_img():
	global input_img
	global img
	input_frame.filename = filedialog.askopenfilename(initialdir="~", title="Select your picture", filetypes=(("image file", ("*.png", "*.jpg", "*.jpeg")), ("all files", "*.*")))
	if input_frame.filename:
		img = Image.open(input_frame.filename)
		img = img.resize((500, int(img.size[1]*500/img.size[0])))
		img = ImageTk.PhotoImage(img)
		input_img.config(image=img, width=img.width(), height=img.height())

# display the result of prediction
def display_result():
	res = predict(Image.open(input_frame.filename), list(hiyoshi_maps.keys()))
	output_img.config(text=res)
	return 0

# create two frames in the window
left_frame = Frame(root, width=300, height=300, background="light green")
left_frame.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)

right_frame = Frame(root, width=300, height=300, background="green")
right_frame.pack(side=RIGHT, anchor=E, fill=BOTH, expand=True)

# create an open image button
load_btn = Button(master=left_frame, height=2, text="Open Image", command=open_img)
load_btn.pack(anchor=N, pady=10)

# create a predict button
predict_btn = Button(master=right_frame, height=2, text="Predict", command=display_result)
predict_btn.pack(anchor=N, pady=10)

# create the frame for the input image
input_frame = Frame(master=left_frame, border=3, relief=RIDGE)
input_frame.pack(anchor=N, fill=BOTH, padx=10, pady=10, expand=True)
input_img = Label(input_frame, width=50, height=20, text="No image selected")
input_img.pack(anchor=CENTER, fill=BOTH)

# create the frame for the result
output_frame = Frame(master=right_frame, border=3, relief=RIDGE)
output_frame.pack(anchor=N, fill=BOTH, padx=10, pady=10, expand=True)
output_img = Label(output_frame, width=50, height=20, text="Awaiting input")
output_img.pack(anchor=CENTER, fill=BOTH)


#TODO: display a map with the predicted result

if __name__ == '__main__':
	root.mainloop()