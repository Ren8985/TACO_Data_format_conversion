The JSON annotation file of the original TACO dataset can be converted into a dataset format that conforms to YOLO training

**main train of thought**

Requirements for annotation information:
● Category number for each target object
The center position (x, y) of the target object in the image
The width and height of the target object (w, h)

**The idea of dataset conversion**
1. Traverse the position and ID of the JSON image and move it to the train folder, then use a counter to rename it using the image ID
2. Traverse all location information to determine if there is a txt named after the image ID,
Do not exist -->Use the image ID to create a txt file, write the bbox position of the category and box on one line
Existence ->Open this txt file and write line breaks to the bbox of the category and box
