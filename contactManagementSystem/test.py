# Write initial content to the file if it doesn't exist
with open('contacts.csv', 'a') as f:
    f.write("a,b,c,d\n")

# Temporary storage for new content
updated_lines = []

# Read all lines and update only the required one
with open('contacts.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        fields = line.strip().split(',')
        name, email, phone, address = fields

        # Update the specific line where the condition is met
        if name == 'a':
            name = 'samad'  # Update the name
            updated_line = f"{name},{email},{phone},{address}\n"
        else:
            updated_line = line  # Keep other lines as they are
        updated_lines.append(updated_line)

# Overwrite the file only with the modified data
with open('contacts.csv', 'w') as f:
    for line in updated_lines:
        f.write(line)
