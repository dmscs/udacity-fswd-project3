# Project 3 Log Analysis
Internal reporting tool. Python file parses through sql database with specific queries and outputs results in text file.

## Getting Started
Install vagrant machine. Detailed instructions can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).

Once vagrant is installed, go to directory with vagrant file. Then:

```
vagrant up
vagrant ssh
cd /vagrant
```

Next, download the data. Detailed instructions can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91). 

Now move **log_analysis.py** to **/vagrant** directory. Then launch program:

```
python log_analysis.py
```
The program will output **sql_query_results.txt** file upon completion.

## Special Note:
Output text file **sql_query_results.txt** should not be opened on Windows Text Editor.
Because the file was made in a Linux editor, Windows Text Editor cannot read line breaks due to [compatability issues](https://askubuntu.com/questions/13224/when-creating-a-new-text-file-should-i-add-a-txt-extension-to-its-name).
However, other text editors, such as atom or sublime, work fine.