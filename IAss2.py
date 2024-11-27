#Name: Ben Leigh
#Student ID: 20074149
#Version: 2202401

#Import required libraries
import hashlib
import json

# Function to produce hash as required
def produce_hash(string_to_hash):
    hashed_object = hashlib.sha256(string_to_hash.encode('utf-8'))
    return hashed_object.hexdigest()

#Open rockyou text file and define variables
passFile = open("rockyou.txt", 'r', encoding='latin-1')
continueLooping = True
data = []

#Begin while loop
while continueLooping == True:
    #Ask user for the file path to the JSON file they wish to check for password hashs or to exit
    hashFilePath = input("Enter the file path for the JSON file or type 'e' to exit: ")
    if hashFilePath.lower() == 'e' or hashFilePath.lower() == 'exit':
        print("Bye :)")
        userToContinue = False
    else:
        #Try to open the file from the path and read it otherwise print an error message
        try:
            hashFile = open(hashFilePath, 'r')
            hashContent = json.load(hashFile)
        except:
            print("Incorrect file path or file does not exist, try again.")
            continue

    #Create a list out of the rockyou passwords, then create a dictionary out of the hashs that are generated
    passFileList = passFile.read().splitlines()
    passDict = {}
    for password in passFileList:
        passDict[produce_hash(password)] = password
    
    for username in hashContent:
        passFound = False
        #Check if the users passwords are in the dictionary by matching them with the hashs from rockyou
        if username['user_password'] in passDict:
            passFound = True
            updates = {'username':username['user_name'],'password':passDict[username['user_password']],'password_found':True}
            print(f"{username['user_name']}'s password was found.")
        else:
            updates = {'username':username['user_name'],'password':"",'password_found':False}
            print(f"{username['user_name']}'s password was not found.")
        data.append(updates)
    continueLooping = False
#open a results json file and record the results
resultsFile = open('results.json', 'w')
json.dump(data, resultsFile, indent=1)
resultsFile.close()
print("The results have been saved to a JSON file named 'results'.")
#Close all relevant files
hashFile.close()
passFile.close()
        
        
    