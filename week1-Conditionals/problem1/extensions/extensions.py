


def main():

    fileName = input("Enter file name with its extension --> ").lower().strip()

    # LeaveOneExtension(fileName) is a recursive function, which will remove all extensions except the last one !
    # And returns extension Point Index of the last on, and the file name excluding every letter/word before the last extension point
    extensionPointIndex, fileNameWithOneExtension = LeaveOneExtension(fileName)

    if extensionPointIndex >= 0:

        extension = fileNameWithOneExtension[extensionPointIndex+1:]

        match extension:
            case "gif" | "png":
                print(f"image/{extension}")
            case "jpeg" | "jpg":
                print(f"image/jpeg")
            case "pdf" | "zip" :
                print(f"application/{extension}")
            case "txt":
                print(f"text/plain")
            case _ :
                print("application/octet-stream")
    else :
        print("application/octet-stream")



# A recurcive function
def LeaveOneExtension(fileName):

    # This will return the index of the extension point, if found, and if the fileName doesn't have an extension than it will return "-1"
    extensionPointIndex =  fileName.find(".")

    # This the base of the recurcive function
    # If extensionPointIndex == -1, so that means that we don't have an extension in the fileName, so please return extensionPointIndex (which is "-1 "in this case) and also return fileName, and exit this function and move to the next one in stack if found !
    if extensionPointIndex == -1:
        return extensionPointIndex, fileName

    # WordsAfterTheExtPoint will be the rest of letters after the extension point
    WordsAfterTheExtPoint = fileName[extensionPointIndex+1:]

    # LeaveOneExtension(WordsAfterTheExtPoint) will return
    extensionPointIndex_2, WordsAfterTheExtPoint = LeaveOneExtension(WordsAfterTheExtPoint)

    if extensionPointIndex_2 == -1:
        # If extensionPointIndex_2 == -1, so that means that WordsAfterTheExtPoint doesn't have any extensions, so don't return WordsAfterTheExtPoint, and return the original fileName instead
        # Notice that this will only be triggered at the fucntion that is next one after the last one of recursion stack
        return extensionPointIndex, fileName
    else:
        # If extensionPointIndex_2 != -1, so that means that we have an extension point, so please return its index, and the words/letters that follow it !
        # WordsAfterTheExtPoint will be the new file name, so it will overwrite the previous name
        # extensionPointIndex_2 will be the new extensionPointIndex, so it will overwrite the previous one
        return extensionPointIndex_2, WordsAfterTheExtPoint



    # This is another solution that is much simpler

    # file = input('what is the file name? ').lower().strip()

    # if file.endswith('gif'):
    #     print('image/gif')
    # elif file.endswith('jpeg') or file.endswith('jpg'):
    #     print('image/jpeg')
    # elif file.endswith('png'):
    #     print('image/png')
    # elif file.endswith('pdf'):
    #     print('application/pdf')
    # elif file.endswith('txt'):
    #     print('text/plain')
    # elif file.endswith('zip'):
    #     print('application/zip')
    # else:
    #     print('application/octet-stream')

main()



