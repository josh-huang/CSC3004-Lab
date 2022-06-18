current_check_in_location = []
with open(f"client_file/123_Josh_info.txt", "r+") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)
        if "Check Out" not in line:
            current_check_in_location.append(line.split("  ",1)[0])
print(current_check_in_location)