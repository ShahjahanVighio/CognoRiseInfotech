import qrcode
import cv2
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Toplevel, Canvas, PhotoImage
from PIL import Image, ImageTk


def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    messagebox.showinfo("QR Code Generator", f"QR Code saved as {filename}")


def decode_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)

    if vertices_array is not None:
        # Show the decoded data
        messagebox.showinfo("QR Code Decoder", f"Decoded Data: {data}")
        # Show the QR code image
        show_image(image_path)
    else:
        messagebox.showerror("QR Code Decoder", "No QR code found in the image.")


def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filename:
        decode_qr(filename)


def generate_qr_gui():
    data = qr_entry.get()
    if data:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            generate_qr(data, save_path)
    else:
        messagebox.showerror("Input Error", "Please enter some data to encode.")


def show_image(image_path):
    # Create a new Tkinter window
    image_window = Toplevel(root)
    image_window.title("QR Code Image")

    # Load and display the image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    canvas = Canvas(image_window, width=image.width, height=image.height)
    canvas.pack()

    canvas.create_image(0, 0, anchor="nw", image=photo)

    # Keep a reference to the image to prevent garbage collection
    canvas.image = photo


# Set up the GUI window
root = Tk()
root.title("QR Code Encoder/Decoder")

# QR Code Generator section
Label(root, text="Enter Data to Encode:").grid(row=0, column=0, padx=10, pady=10)
qr_entry = Entry(root, width=40)
qr_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = Button(root, text="Generate QR Code", command=generate_qr_gui)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# QR Code Decoder section
decode_button = Button(root, text="Decode QR Code", command=browse_file)
decode_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()
