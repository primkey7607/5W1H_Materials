import csv
import numpy as np
import tabulate

ratingmap = {"Very Easy" : 1, "Easy" : 2, "Moderate" : 3, "Difficult" : 4,
             "Very Difficult" : 5}

#create a dictionary where
#key: question number
#value: list of ratings people had for that question
def create_rating_dict(fname):
    with open(fname, 'r') as fh:
        csvreader = csv.reader(fh)
        outdict = {}
        for i,row in enumerate(csvreader):
            if i == 0: #then, these are the headers
                continue
            outdict[i] = []
            for j,e in enumerate(row):
                if j <= 1:
                    continue
                lst2Add = []
                if int(e) == 0:
                    lst2Add = []
                else:
                    lst2Add = [j-1]*int(e)
                outdict[i] = outdict[i] + lst2Add
    
    return outdict

def make_median_row(kr_name, krdict):
    new_row = []
    new_row.append(kr_name)
    for i in range(1, 28):
        vals = krdict[i]
        quartiles = np.percentile(vals, [25, 50, 75])
        #only use the median for now
        new_row.append(quartiles[1])
    
    return new_row

def genTable5Medians():
    ourname = 'our_mmq_ratings.csv'
    gcsname = 'gcs_mmq_ratings.csv'
    dhname = 'datahub_mmq_ratings.csv'
    ourdict = create_rating_dict(ourname)
    gcsdict = create_rating_dict(gcsname)
    dhdict = create_rating_dict(dhname)
    
    rows = []
    header = ['MM']
    for i in range(1, 28):
        header.append('Q' + str(i))
    
    rows.append(header)
    
    our_row = make_median_row('5W1H', ourdict)
    gcs_row = make_median_row('GCS', gcsdict)
    dh_row = make_median_row('Datahub', dhdict)
    
    rows.append(our_row)
    rows.append(gcs_row)
    rows.append(dh_row)
    
    restable = tabulate.tabulate(rows, headers='firstrow', tablefmt='latex')
    with open('table5medians.txt', 'w+') as fh:
        fh.write(restable)
        
#genTable5Medians()