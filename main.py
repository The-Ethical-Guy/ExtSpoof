import readline
import os
import shutil
import requests
from zipfile import ZipFile
from io import BytesIO
import tempfile
from extspoof import *

wow = Secrets


#file to jpg func
def file_to_jpg(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}gpj{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


#file to pdf func
def file_to_pdf(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}fdp{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


#file to txt func
def file_to_txt(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}txt{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


#file to docx func
def file_to_docx(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}xcod{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


#file to mp4 func
def file_to_mp4(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}4pm{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")

#file to gif func
def file_to_gif(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}fig{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


#file to mp3 func
def file_to_mp3(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}3pm{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")

#special extension spoofing
def special_spoofing(input_path, ext):
    rev_ext = ext[::-1]
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}{rev_ext}{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file safed \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


#update the tool
def update():
    tool_path = "../ExtSpoof"

    if os.path.exists(tool_path):
        shutil.rmtree(tool_path)


    with tempfile.TemporaryDirectory() as temp_path:

        github_url = "https://github.com/The-Ethical-Guy/ExtSpoof/archive/main.zip"
        response = requests.get(github_url)

        if response.status_code == 200:
            with ZipFile(BytesIO(response.content), 'r') as zip_file:
                zip_file.extractall(temp_path)

            source_folder = os.path.join(temp_path, "ExtSpoof-main")
            shutil.move(source_folder, tool_path)

            print("ExtSpoof updated \033[1;32msuccessfully!\033[1;97m")
        else:
            print(f"\033[1;31mFailed\033[1;97m to download ExtSpoof from GitHub. Status code: {response.status_code}")






def main():
    Baner()
    print("\n\033[1;35m-:\033[1;97mChose an option\033[1;35m:-\033[1;97m")
    print(choices)
    while True:
        try:
            user_choice = input("\033[1;35m>>\033[1;97m ")
            if user_choice == '1':
                file_path = input("enter the file path: ")
                file_to_jpg(file_path)
                break

            elif user_choice == '2':
                file_path = input("enter the file path: ")
                file_to_pdf(file_path)
                break

            elif user_choice == '3':
                file_path = input("enter the file path: ")
                file_to_txt(file_path)
                break

            elif user_choice == '4':
                file_path = input("enter the file path: ")
                file_to_docx(file_path)
                break

            elif user_choice == '5':
                file_path = input("enter the file path: ")
                file_to_mp4(file_path)
                break

            elif user_choice == '6':
                file_path = input("enter the file path: ")
                file_to_gif(file_path)
                break
            
            elif user_choice == '7':
                file_path = input("enter the file path: ")
                file_to_mp3(file_path)
                break
            
            elif user_choice == '8':
                file_path = input("enter the file path: ")
                ext = input("enter the extension name to spoof: ")
                special_spoofing(file_path, ext)
                break

            elif user_choice == '9':
                print("start updating the tool")
                update()
                break

            elif user_choice == '0':
                exit()


            else:
                print("please enter a valid choice")
        except KeyboardInterrupt:
            print("\nEnter '0' to exit")
            pass


if __name__ == '__main__':
    main()
