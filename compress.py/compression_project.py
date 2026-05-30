

import tkinter as tk
from tkinter import ttk

# ================= RLE =================
def rle_compress(data):
    compressed = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        compressed += data[i] + str(count)
        i += 1
    return compressed

def rle_decompress(data):
    decompressed = ""
    i = 0
    while i < len(data):
        char = data[i]
        i += 1
        num = ""
        while i < len(data) and data[i].isdigit():
            num += data[i]
            i += 1
        decompressed += char * int(num)
    return decompressed

# ================= Huffman (Simplified) =================
huff_codes = {}

def huffman_compress(data):
    global huff_codes
    huff_codes = {}
    unique = list(set(data))
    
    for i, ch in enumerate(unique):
        huff_codes[ch] = format(i, 'b')  # binary code
    
    compressed = ''.join(huff_codes[c] for c in data)
    return compressed

def huffman_decompress(data):
    reverse = {v: k for k, v in huff_codes.items()}
    temp = ""
    result = ""
    
    for bit in data:
        temp += bit
        if temp in reverse:
            result += reverse[temp]
            temp = ""
    
    return result

# ================= Functions =================
def compress():
    text = input_text.get("1.0", tk.END).strip()
    algo = algo_choice.get()

    if text == "":
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Enter text first!")
        return

    if algo == "RLE":
        result = rle_compress(text)
    else:
        result = huffman_compress(text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

    if len(result) > 0:
        ratio = len(text) / len(result)
        ratio_label.config(text=f"Compression Ratio: {ratio:.2f}")

def decompress():
    text = input_text.get("1.0", tk.END).strip()
    algo = algo_choice.get()

    if algo == "RLE":
        result = rle_decompress(text)
    else:
        result = huffman_decompress(text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    ratio_label.config(text="Compression Ratio: ")

# ================= GUI =================
root = tk.Tk()
root.title("Compression Project")
root.geometry("500x400")

tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

algo_choice = ttk.Combobox(root, values=["RLE", "Huffman"])
algo_choice.set("RLE")
algo_choice.pack(pady=5)

tk.Button(root, text="Compress", command=compress, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Decompress", command=decompress, bg="lightblue").pack(pady=5)
tk.Button(root, text="Clear", command=clear_all, bg="lightgray").pack(pady=5)

tk.Label(root, text="Output:", font=("Arial", 12)).pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

ratio_label = tk.Label(root, text="Compression Ratio: ")
ratio_label.pack(pady=5)

root.mainloop()