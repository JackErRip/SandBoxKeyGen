import tkinter as tk
import uuid
import clipboard

class UUIDGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UUID Generator")

        # Set the background color to white
        self.root.configure(bg="white")

        self.uuid_label = tk.Label(root, text="Generated UUID:", bg="white", fg="black")
        self.uuid_label.pack()

        self.uuid_var = tk.StringVar()

        # Adjust the width of the Entry widget to fit the UUID key
        self.uuid_entry = tk.Entry(root, textvariable=self.uuid_var, state="readonly", bg="white", fg="black", width=50)
        self.uuid_entry.pack()

        self.regenerate_button = tk.Button(root, text="Regenerate", command=self.generate_uuid, bg="white", fg="black")
        self.regenerate_button.pack()

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="white", fg="black")
        self.copy_button.pack()

        self.generate_uuid()

        # Add label with creator's name at the bottom
        self.creator_label = tk.Label(root, text="Software was made by: Aldrien Velasco", bg="white", fg="black")
        self.creator_label.pack(side="bottom")  # Position at the bottom

    def generate_uuid(self):
        new_uuid = str(uuid.uuid4()).upper()
        self.uuid_var.set(new_uuid)

    def copy_to_clipboard(self):
        uuid_to_copy = self.uuid_var.get()
        clipboard.copy(uuid_to_copy)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x200")  # Set the window resolution
    app = UUIDGeneratorApp(root)
    root.mainloop()
