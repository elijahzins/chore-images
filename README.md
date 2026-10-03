Hello, welcome to the chore completion/classifier data set. The goal of this project it to 
build a tool that can recognize a task and its completion status as well as giving some reasoning behind why that decision was made.

To get started with this data set can be found on a Github link attached to the doc. It has 102 images. These images were collected by personal imaging and free online stock photos from the websites Pexels and Unsplash. There are 102 images inside of this data set. These images are scenario images from the environments where the chores/tasks take place. Inside of this data set there are four distinct categories that can be seperated. 

The first thing is the chore type, in this dataset there are only two different chore types: washing dishes and taking out garbage. The washing dishes task can be found inside of kitchen/dining room setting. Taking out the garbage has a variety of scenes but contains trash/dumpsters/or loose garbage.

The second thing to be classified is the chore completion. For washing dishes to be complete dishes need to be drying, clean, or put away. An incompletely washing dishes will have them dirty, food covered, or haphazardely stacked inside of the sink. Garbage can be seen as completed if there is an empty trash can, bagged and stacked outside, or grabage that is in dumpsters. Incomplete would have full or partially full trash bags or loose gharbage laying about. 

The final field is a justification on why a task was classified as complete or incomplete. This should be a short sentence or statement based on the annotators thought process when making the decision. This should include reasoning and can reference the guidelines above but human thoughts/opinions could also be helpful (may adjust guidelines later)

Edge cases/ unclear status may appear. All of the images should be related to one of the tasks either washing the dishes or taking out the garbage. Completion can be more vague, partial completion is NOT complete all dishes should be washed and all garbage should be inside dumpster or bags. If a decision can truly not be made, incomplete should be marked a completed chore should rather get marked incomplete then an incomplete chore get marked complete. 

The estimated time to label each instance should take around 30-45 seconds. The entire dataset would take 60-75 minutes. But it can be done quicker. Every annotator should start at the beginning and label as much data as possible. Any data that is not covered will be covered by volunteer anotators and me. 

The license for this data set will be the CC0 1.0 Universal License. This means that anyone can run or use this dataset if they so choose. Currently the dataset is set to a public Github repo that anyone can use.

_________________________
HOW TO RUN
_________________________

The first step is unzipping the folder. Then open up the folder inside of an IDE I recommend VSCode. The interpreter for the IDE should be python. The files contained inside of the folder should be:

config.yaml
createJSON.py
data.json
README.md

Next install Potato using "pip install potato-annotation"

Inside of the terminal use the command "potato start config.yaml" wait a few seconds until the 
it says that the server it running. 

Make sure that internet is working properly. The dataset is hosted on a Github public repo, images will not appear if the internet is not working

Inside of the internet browser go to "http://localhost:8000"

Click register to create a new account, the username and password can be anything. For the sake of keeping track of annotators please keep the username identifiable. 

You can now annotate the dataset by choosing the chore type, completion status, and filling in the note. You will be able to navigate freely across all of the examples. I recommend starting at the beginning and traversing the dataset in order. This process should take around and hour.

When the annotation is finished go back to the terminal and kill the runtime.

Because the runtime was hosted on the annotators machine the annotations will have to be sent back to me. Please copy the annotation_output folder and send it through email or discord. 

I can be reached at ezinsli@umich.edu or ezinsli_84434 on Discord. Feel free to ask questions or give feedback, anything is appreciated. 




