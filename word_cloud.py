"""
Create a "word cloud" from a text by writing a script. 
This script needs to process the text, remove punctuation, 
ignore case and words that do not contain all alphabets, 
count the frequencies, and ignore uninteresting or irrelevant words. 
A dictionary is the output of the calculate_frequencies function. 
The wordcloud module will then generate the image from your dictionary.
"""
##################################
# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

##################################
# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

##################################

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "in", "on", "not", "thus", "for", "thy", "then", "yet", "so", "while", "thou", "now", "shall", "there", "through", \
    "those", "one", "day", "like", "may"]
    
    # LEARNER CODE START HERE
    text = file_contents.lower()
    for char in punctuations:
        text = text.replace(char, '')
    
    words_all = text.split()
    
    words_frequencies = {}
    for word in words_all:
        if word in uninteresting_words:
            continue
        if word not in words_frequencies:
            words_frequencies[word] = 0
        words_frequencies[word] += 1
    
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_frequencies)
    return cloud.to_array()
  
###############################################

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
