from time import *
import random as r

set_of_string = ["I want to install SoundRecongnition package but I'm getting the following error when I type: pip3 install SoundRecognition",
                 "I tried upgrading the pip. Also tried using the --user tag but still facing the problem. I'm using pip 19.0.3 version, python 3.7.0 version, and Pycharm as IDE.",
                 "Could not find a version that satisfies the requirement SoundRecognition (from versions: ) No matching distribution found for SoundRecognition"]

def get_string(set_of_string):
    choice_num = [x for x in range(0,len(set_of_string))]
    id = r.choice(choice_num)
    print(set_of_string[id])
    return set_of_string[id]

def get_input():
    get_input = input( "Enter the line displayed \n")
    return get_input
    

def check(input_str, ref_str):
    err = 0
    for i in range(0,len(ref_str)):
        try:
            if ref_str[i]!=input_str[i]:
                err+=1
        except:
            err+=1
    return err

def get_accuracy(err_num, length_of_str):
    acc = round((length_of_str - err_num)*100/length_of_str,2)
    return acc
    
if __name__ == "__main__":

    print("Hello, Are you ready for typing test")
    ref_str = get_string(set_of_string)
    start_time = time()
    input = get_input()
    err_num = check(input,ref_str)
    end_time = time()
    accuracy = get_accuracy(err_num,len(ref_str))
    print(f'You typing has {err_num} error')
    print(f'You took {round((end_time-start_time),2)} sec with {accuracy} % accuracy.')
