import pandas as pd
import os.path
from datetime import datetime


#Create a .csv of a DF dict, such that no other gets deleted or overwritten
def create_dict(filname, heads):
    filname = correct_ext(filname, '.csv')
    if os.path.exists("./" + filname):
        print(filname + " already exists")
        return False
    else:
        tmp_dict = {}
        for head in heads:
            tmp_dict[head] = []
        d = pd.DataFrame(tmp_dict)
        save_prog(d, filname)
        return True

def save_prog(df, filname):
    filname = correct_ext(filname, '.csv')
    df.to_csv(filname, index=False, na_rep="Unknown", float_format='%.2f')
    print(filname+" saved")

def correct_ext(filname, correct):
    root, ext = os.path.splitext(filname)
    if not ext or ext != correct:
        ext = correct
    filname = root + ext
    return filname


def new_head(frame, head, pos=0):
    global file
    if pos == 0:
        frame[head] = []
    else:
        frame.insert(pos, head, [])
    print(head + " added to " + frame)
    save_prog(frame, file)
    return frame

def target_f(filname):
    filname = correct_ext(filname, '.csv')
    if not os.path.exists("./" + filname):
        create_dict(filname, ['tmp'])
    f = pd.read_csv(filname)
    return f.set_index(f.columns[0])

def add_data(frame, col, row, data):
    global file
    frame.loc[row, col] = data
    print(str(data) + " added")
    save_prog(frame, file)
    return frame

    
def add_row(frame, data=[]):
    c = frame.columns
    tmp = {}
    for i in range (0, len(c)):
        tmp[c[i]] = data[i+1]
    tmp = pd.Series(tmp)
    tmp = tmp.rename(data[0])
    print(tmp)
    frame = frame.append(tmp)
    save_prog(frame, file)
    return frame
    
file = 'subs.csv'
DF = target_f(file)

#ERROR RIGHT NOW:
#setting index means we're not saving properly.
