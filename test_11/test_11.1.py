def swap_case_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

        swapped_data = data.swapcase()

        with open(output_file, 'w') as file:
            file.write(swapped_data)

        print(f"Successfully converted case and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = 'input.txt'
output_file = 'output.txt'
swap_case_in_file(input_file, output_file)
