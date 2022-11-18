# Computer Networks
## Assignment 2
### Tanmay Garg CS20BTECH11063

Please extract the zip file present in the directory. 2 Folders will be present in this extracted directory which are
- A2_SW
- A2_GBN

### A2_SW
- This contains the file for running Stop and Wait Protocol
- It contains all the python files and image file to be used, please execute the following code (as mentioned in the assignment doc)
```bash
$ sudo mn
```
- The 5 important files in this directory are
    - CS20BTECH11063_senderStopWait.py
    - CS20BTECH11063_receiverStopWait.py
    - testFile.jpg
    - script_h1.sh
    - script_h2.sh
- To run both the files please follow this procedure
    - After doing ```sudo mn```, in the mininet prompt, run ```xterm h1``` and ```xterm h2```
    - In H2 run the command
    ```bash
    $ bash script_h2.sh
    $ python3 CS20BTECH11063_receiverStopWait.py
    ```
    - In H1 run the command
    ```bash
    $ bash script_h1.sh
    $ python3 CS20BTECH11063_senderStopWait.py
    ```

- The program will automatically send the image chunks to the reciever and the reciever will automatically save the image in the directory

### A2_GBN
- This contains the file for running Go Back N Protocol
- It contains all the python files and image file to be used, please execute the following code (as mentioned in the assignment doc)
```bash
$ sudo mn
```
- The 5 important files in this directory are
    - CS20BTECH11063_senderGBN.py
    - CS20BTECH11063_receiverGBN.py
    - testFile.jpg
    - script_h1.sh
    - script_h2.sh
- To run both the files please follow this procedure
    - After doing ```sudo mn```, in the mininet prompt, run ```xterm h1``` and ```xterm h2```
    - In H2 run the command
    ```bash
    $ bash script_h2.sh
    $ python3 CS20BTECH11063_receiverGBN.py
    ```
    - In H1 run the command
    ```bash
    $ bash script_h1.sh
    $ python3 CS20BTECH11063_senderGBN.py
    ```

- The program will automatically send the image chunks to the reciever and the reciever will automatically save the image in the directory


NOTE:
The code is written in python3 and the image is in jpg format. Please make sure that the image is in the same directory as the python files. Also, the image name is testFile.jpg. If you want to change the image name, please change the name in the python files as well.

Also, the scripts ```scripts_h1.sh``` and ```scripts_h2.sh``` are different linux commands than the one given in the pdf as instructed by the Teaching Assistants. Please use the scripts given in the directory.