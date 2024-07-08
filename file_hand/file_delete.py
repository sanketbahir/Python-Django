import os

def delete_file(file_name):
    if(os.path.exists(file_name)):
      os.remove(file_name)
    else:
      print('file dose not exist')

def main():
    print('enter the name of file you want to delete')
    file_name = input('')
    delete_file(file_name)

if __name__=="__main__":
    main()
