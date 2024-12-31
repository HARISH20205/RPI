import subprocess
import tkinter as tk
from tkinter import scrolledtext

def run_script():
    prompt = prompt_entry.get().strip()
    
    if not prompt:
        output_text.insert(tk.END, "❌ Please enter a prompt.\n", "error")
        output_text.see(tk.END)
        return
    
    output_text.insert(tk.END, f"📝 Prompt: {prompt}\n", "prompt")
    output_text.insert(tk.END, "🚀 Starting script execution...\n", "info")
    output_text.see(tk.END)
    
    process = subprocess.Popen(
        ["bash", "../scripts/frugalSot.sh"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=prompt)
    
    if stdout:
        output_text.insert(tk.END, f"{stdout}\n", "output")
    #if stderr:
        #output_text.insert(tk.END, f"⚠️ Error: {stderr}\n", "error")
    
    output_text.insert(tk.END, "✅ Execution completed.\n", "info")
    output_text.see(tk.END)

def close_app():
    root.destroy()

root = tk.Tk()
root.title("FRUGAL SOT GUI")
root.geometry("750x550")
root.resizable(False, False)
root.config(bg="#eaf2f8")

header_label = tk.Label(
    root, 
    text="FRUGAL SOT GUI", 
    font=("Helvetica", 16, "bold"), 
    bg="#5dade2", 
    fg="white",
    padx=20, 
    pady=10
)
header_label.pack(fill=tk.X)

prompt_label = tk.Label(
    root, 
    text="Enter Prompt:", 
    font=("Arial", 12, "bold"), 
    bg="#eaf2f8", 
    fg="#34495e"
)
prompt_label.pack(pady=(20, 5))

prompt_entry = tk.Entry(
    root, 
    width=60, 
    font=("Arial", 12), 
    relief="solid", 
    borderwidth=2
)
prompt_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=20)

run_button = tk.Button(
    button_frame,
    text="Run Script",
    command=run_script,
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    width=15,
    relief="raised",
    borderwidth=3
)
run_button.pack(side=tk.LEFT, padx=10)

end_button = tk.Button(
    button_frame,
    text="End",
    command=close_app,
    font=("Arial", 12, "bold"),
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    width=15,
    relief="raised",
    borderwidth=3
)
end_button.pack(side=tk.LEFT, padx=10)

output_text = scrolledtext.ScrolledText(
    root, 
    wrap=tk.WORD, 
    width=80, 
    height=20, 
    font=("Courier", 10), 
    bg="#f9f9f9", 
    fg="#2c3e50", 
    relief="solid", 
    borderwidth=2
)
output_text.pack(pady=10)

output_text.tag_config("prompt", foreground="#2980b9", font=("Arial", 10, "italic"))
output_text.tag_config("info", foreground="#27ae60", font=("Arial", 10, "bold"))
output_text.tag_config("output", foreground="#2c3e50", font=("Courier", 10))
output_text.tag_config("error", foreground="#e74c3c", font=("Arial", 10, "bold"))

root.mainloop()
