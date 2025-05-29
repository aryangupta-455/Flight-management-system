import os
def create_file(filename):
    try:
        with open (filename, 'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(F'File Name {filename} already exists!')
        
    except Exception as E:
        print('An Error Occured!')
        
def view_all_files():
    files = os.listdir()
    if not files:
        print("No Files found!")
    else:
        print("Files in Directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been removed successfully!")
    except FileNotFoundError:
        print('File not Found!')
    except Exception as e:
        print('An Error Occured!')
        
def read_file(filename):
    try:
        with open ('sample.txt', 'r') as f:
            content =f.read()
            print(f"Content of '{filename}' :\n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print('An Error Occured!')
        
def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input ("Enter data to add = ")
            f.write(content +"\n")
            print("Content added to {filename} Successfully!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print('An Error Occured!')
        
def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1: Create File")
        print("2: View All Files")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit")
        
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            filename = input("Enter the file name to create: ")
            create_file (filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the file name to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file name to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file name to edit: ")
            edit_file(filename)
        elif choice == '6':
            print("Thank you for using the File Management App!")
            print("Closing the app....")
            break
        else:
            print("Invalid Choice! Try again.")

if __name__ == "__main__":
    main()