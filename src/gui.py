import subprocess
import tkinter as tk
from tkinter import scrolledtext

def run_script():
    prompt = prompt_entry.get()
    
    if not prompt:
        output_text.insert(tk.END, "❌ Please enter a prompt.\n")
        output_text.tag_add("error", "end-2l", "end-1l")
        output_text.tag_config("error", foreground="red", font=("Arial", 10, "bold"))
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
    
    try:
        stdout, stderr = process.communicate(input=prompt, timeout=120)
        
        if stdout:
            output_text.insert(tk.END, f"{stdout}\n", "output")
        if stderr:
            output_text.insert(tk.END, f"⚠️ Error: {stderr}\n", "error")
            
    except subprocess.TimeoutExpired:
        process.kill()
        output_text.insert(tk.END, "⏳ Script execution timed out\n", "timeout")
        output_text.tag_add("timeout", "end-2l", "end-1l")
        output_text.tag_config("timeout", foreground="orange", font=("Courier", 10, "italic"))
    
    output_text.insert(tk.END, "✅ Execution completed.\n", "info")
    output_text.see(tk.END)

def close_app():
    root.destroy()

root = tk.Tk()
root.title("FRUGAL SOT GUI")
root.geometry("700x500")
root.config(bg="#f0f8ff")

prompt_label = tk.Label(
    root, text="Enter Prompt:", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="black"
)
prompt_label.pack(pady=10)

prompt_entry = tk.Entry(root, width=60, font=("Arial", 10))
prompt_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

run_button = tk.Button(
    button_frame,
    text="Run Script",
    command=run_script,
    font=("Arial", 12, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#45a049",
    width=15
)
run_button.pack(side=tk.LEFT, padx=5)

end_button = tk.Button(
    button_frame,
    text="End",
    command=close_app,
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    activebackground="#e53935",
    width=15
)
end_button.pack(side=tk.LEFT, padx=5)

output_text = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=80, height=20, font=("Courier", 10), bg="#f9f9f9", fg="black"
)
output_text.pack(pady=10)

output_text.tag_config("prompt", foreground="blue", font=("Arial", 10, "italic"))
output_text.tag_config("info", foreground="green", font=("Arial", 10, "bold"))
output_text.tag_config("output", foreground="black", font=("Courier", 10))
output_text.tag_config("error", foreground="red", font=("Arial", 10, "bold"))

root.mainloop()
