# -*- coding: utf-8 -*-
"""
Created on Sat Feb  17 13:31:11 2024

@author: Jimmy
"""

import speech_recognition as sr

def recognize_from_mic(recognizer, microphone,phrase_time_limit=None):
    """speech from recorded from `mic`.

    Returns a dictionary with three keys:

    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "achieve": `None` if speech could not be achieved,
               otherwise a string containing the recognized text
    """

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`please us the `speech_recognition.Recognizer` as your recognizer")


    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,phrase_time_limit=phrase_time_limit)

    # set up the output object
    output = {
        "error": None,
        "achieve": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        output["achieve"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        output["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unrecognizable
        output["error"] = "Sorry, I cannot hear your voice. Please try again"

    return output


def user_input(i=3,phrase_time_limit=3):
    tries=i
    if tries==3:
        print("Please tell me your name")
    if tries>0:
        response = recognize_from_mic(recognizer, microphone,phrase_time_limit=3)
        name=response["achieve"]
        tries-=1
        if name:
            return name
        if response["error"]:
            # print error message
            print("ERROR: {}".format(response["error"]))
            user_input(tries)
    else:
        print("Please check your mic")
        return None


if __name__ == "__main__":
    # set up the recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    name=user_input()

    if name:
    # show instructions to the user
        print(f"Hi,{name}! Let's have a great conversation")

        # recognize speech and print the transcription
        response = recognize_from_mic(recognizer, microphone)
        if response["achieve"]:
            # print successful transcription
            #print("You said: {}".format(response["transcription"]))
            print(name,":",response["achieve"])

        if response["error"]:
            # print error message
            print("ERROR: {}".format(response["error"]))


