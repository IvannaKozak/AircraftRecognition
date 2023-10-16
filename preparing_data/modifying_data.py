def modify_txt_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()  # Remove any trailing whitespace
            modified_line = f"../dataset/JPEGImages/{line}.jpg\n"
            outfile.write(modified_line)

if __name__ == "__main__":
    modify_txt_file("new_train.txt", "modified_train.txt")
    modify_txt_file("new_test.txt", "modified_test.txt")
