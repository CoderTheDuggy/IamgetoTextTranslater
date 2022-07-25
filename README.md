# ImgToChars
ImgToChars is a small python-script, whith which you can display an image as text!

![Normal image](/assets/pythonLogo.png) -----> ![Chars screenshot](/assets/charsScreenshot.png)


### Configuration
- By default, ImgToChars creates a file with the result. You can diable it with the argument`--no-file`
- The default ouput-location of the output-file is the location of the script. If you want you can change the with the argument   
`--custom-output-file` followed by the costum ouput-dir!

### Dependencies
ImgToChars requeries the following dependencies:

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
git clone https://github.com/CoderTheDuggy/ImageToChars.git
```
Install all requirements like shown.

Execute the script:
```
python imgToChars.py
```
First, you must enter the path to the image
Than you can enter the width to resize to or nothing to calculate it from the height.
After that you can enter the height to resize to or nothing to calculate it from the width.
If you leave both width and height empty, it uses the original width and height.  
If it hasn't been disabled, there appears a output file in the dir of the script or, if set, in the custom-location!
