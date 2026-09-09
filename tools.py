def create_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)

        return f"File '{filename}' created successfully."

    except Exception as e:
        return f"Error creating file: {e}"