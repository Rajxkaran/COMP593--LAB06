import requests
import hashlib
import subprocess
import os

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    # expected_sha256 = get_expected_sha256()
    # Send GET message to download the file
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        
        # Extract binary file content from response message body
        file_content = resp_msg.text
        
        x = file_content.split()
        # Print the hash value
        print(x[0])
               
    # Download (but don't save) the VLC installer from the VLC website
    
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe'
    resp_msg = requests.get(file_url)
    
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        
        # Extract text file content from response message
        file_content = resp_msg.content
        
        # Calculate SHA-256 hash value
        image_hash = hashlib.sha256(file_content).hexdigest()
            
        # Print the hash value
        print(image_hash)
        
    # Verify the integrity of the downloaded VLC installer by comparing the expected and computed SHA-256 hash values
    if x[0] == image_hash:
        print("Hash value's have matched")
    else:
        print("Files are different")
    
    # Save the downloaded VLC installer to disk
    with open(r'C:\temp\vlcinstaller.exe', 'wb') as file:
        file.write(file_content)
        print("file has been saved")

def installing_vlc():

    # Silently run the VLC installer
    installer_path = r'C:\temp\vlcinstaller.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])

    print("File was ran silently in the background ")
    return installer_path

def removing_vlc(installer_path):

    #Delete the VLC installer from disk
    os.remove(installer_path)
    print("File has been deleted")
            

if __name__ == '__main__':
    main()