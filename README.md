# Sentiment-Analyzer

Problem identified: 
In places such as cafes, shops, movie theatre, it's very difficult to collect review to know the performance quality by making them fill the form, it's very time consuming and sometimes confusing. According to recent research, 84% of people fill out at least one web form per week. Which supports our stance that most of the people prefer to review by saying it rather than filling any form. 

Solution: 
So to solve this problem and enhance communication, I have made this project that collects people’s review by asking them personally, and analyze whether the review is positive, negative or neutral and hence bridges the communication gap. So, in order to achieve this, I have used technologies such as speech-to-text and text-to-speech conversion. On starting the program, a page designed using Tkinter (pythons GUI), opens up. On the click of the button, the program starts talking to the user, which makes it easier for the user to understand what to do, using text to speech. 
The person can then speak and record its review. 
The speech and text conversion were achieved using the libraries namely speech_recognition, pyttsx3, and gTTS. Note: You need to have these packages on your computer in order to run the program. Execute the following lines of code in your command prompt to install the packages.
pip install speech_recognition pip install pyttsx3 (if this does not get installed, kindly install the .whl file for the corresponding library.) 
pip install gTTS speech_recognition: Recognizing speech requires audio input, and SpeechRecognition makes retrieving this input really easy. 
Instead of having to build scripts for accessing microphones and processing audio files from scratch, SpeechRecognition will have you up and running in just a few minutes. pyttsx3: is a text-to-speech conversion library in Python. gTTS (Google Text-to-Speech): a Python library and CLI tool to interface with Google Translates' text-to-speech API textblob- Textblob and its NLPTK libraries. After recording the review from a customer, it analyses whether the review given is positive or negative or neutral, and to do this we have used textblob and its NLPTK libraries. And all the reviews are stored in a database called db.txt file for future reference. Recommendation: Run the code using the Visual Studio Code. 

Project Done By: 
Gaurav Vinod Bhambhani
(18BCE072)

