from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from street_clip import predict, hiyoshi_maps

root = Tk()
root.title('Image Viewer')

# resize window to 500x300px
root.geometry("500x300")


# open image
def open_img():
	global my_img
	root.filename = filedialog.askopenfilename(initialdir="~", title="Select your picture", filetypes=(("image file", ("*.png", "*.jpg", "*.jpeg")), ("all files", "*.*")))
	my_label = Label(root, text=root.filename).pack()
	my_img = ImageTk.PhotoImage(Image.open(root.filename))
	my_img_label = Label(image=my_img).pack()
	return my_img


# display the result of prediction
def display_result():
	res = predict(Image.open(root.filename), list(hiyoshi_maps.keys()))
	result_label = Label(root, text=res).pack()
	return res


# create an open image button
my_btn = Button(root, text="Open Image", command=open_img).pack(anchor=CENTER)

# create a predict button
predict_btn = Button(root, text="Predict", command=display_result).pack(anchor=CENTER)

#TODO: display a map with the predicted result

if __name__ == '__main__':
	root.mainloop()