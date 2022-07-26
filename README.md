# ImgToAscii
ImgToAscii is a small python-script, with which you can display an image as text!

### Configuration
- By default, ImgToAscii creates a file with the result. You can disable it with the argument`--no-file`
- The default output-location of the output-file is the location of the script. If you want you can change the with the argument   
`--custom-output-file` followed by the custom output-dir!

### Dependencies
ImgToAscii requires the following dependencies:

- colorama
- numpy
- Pillow
You can just install all required dependencies from the requirements.txt file with the following command:
```
pip install -r requirements.txt
```

### Run it
Clone the repository with the following command:
```
git clone https://github.com/CoderTheDuggy/ImgToAscii.git
```
Install all requirements like shown.

Execute the script:
```
python ImgToAscii.py
```
- First, you must enter the path to the image. 
- Then you can enter the width to resize to or nothing to calculate it from the height.
- After that you can enter the height to resize to or nothing to calculate it from the width.
- If you leave both width and height empty, it uses the original width and height.
- Now you are requested to enter the offset. By leaving it blank, the default offset is calculated.  
You can also enter a number to use a custom offset or enter `disabled`, so the offset is disabled!
- If it hasn't been disabled, there appears an output file in the dir of the script or, if set, in the custom-location!
