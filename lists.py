def print_data(txt):
    print(txt)


data = [1, 61, 32, 32, 12, 44]
data.sort()     # sort data in list
print_data(data)
data.reverse()  # revert data max to min
print_data(data)
print_data(data.pop())   # Print last element and remove from list
print_data(data)
print_data(data.count(32))   # Count object in list this will return 2 because this list has double 32
data.append(55)    # Append use for add data but we can add only one object will error data.append(1,2,3)
print_data(data)
data.extend([7, 8, 9])      # Add multiple data to list need to put value in []
print_data(data)
data.append("a")        # Python allow to store difference type in one list, just remember one thing
print_data(data)             # We cannot sort String. Will error when data.sort()
data.insert(1, 99)      # Insert object in specific index, this case will add 99 in to index 1
print_data(data)
print_data(data[1:])         # Return data start with index 1 until whatever, who care event Python not care.
print_data(data[:3])         # Return data start with first element until index 3
print_data(data[:])          # Print data start with whatever end with whatever ....
