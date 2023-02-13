text_to_add = "index.html"
target_text = "swagger/"

file_list = [
    "sites.txt"
]

for file_name in file_list:
    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "w") as f:
        for line in lines:
            if line.strip().endswith(target_text):
                f.write(line.strip() + text_to_add + "\n")
            else:
                f.write(line)

print("Text added successfully to all files.")
