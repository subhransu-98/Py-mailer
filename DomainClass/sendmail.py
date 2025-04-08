import smtplib
import ssl
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender = sender_entry.get()
    receiver = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    password = password_entry.get()

    if not sender or not receiver or not subject or not message or not password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        # Set up the email
        email = EmailMessage()
        email["From"] = sender
        email["To"] = receiver
        email["Subject"] = subject
        email.set_content(message)

        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            server.send_message(email)

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email.\n\n{str(e)}")

# GUI setup
window = tk.Tk()
window.title("Python Email Sender")
window.geometry("400x450")
window.resizable(False, False)

# Widgets
tk.Label(window, text="Sender Email:").pack()
sender_entry = tk.Entry(window, width=40)
sender_entry.pack()

tk.Label(window, text="Password:").pack()
password_entry = tk.Entry(window, show="*", width=40)
password_entry.pack()

tk.Label(window, text="Receiver Email:").pack()
receiver_entry = tk.Entry(window, width=40)
receiver_entry.pack()

tk.Label(window, text="Subject:").pack()
subject_entry = tk.Entry(window, width=40)
subject_entry.pack()

tk.Label(window, text="Message:").pack()
message_text = tk.Text(window, height=10, width=40)
message_text.pack()

tk.Button(window, text="Send Email", command=send_email).pack(pady=10)

window.mainloop()
