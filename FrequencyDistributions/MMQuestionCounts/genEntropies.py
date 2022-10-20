import csv
import numpy as np
import tabulate
import math
import matplotlib.pyplot as plt

def create_entropy_dict(fname):
    resdict = {}
    with open(fname, 'r') as fh:
        csvreader = csv.reader(fh)
        for i,row in enumerate(csvreader):
            if i == 0:
                continue
            row_len = len(row)
            #compute max entropy
            max_entropy = 0
            for k in range(row_len - 1):
                frac = float(1) / float(row_len - 1)
                max_entropy += frac * math.log(frac, 2)
            max_entropy = -max_entropy
            vals = []
            for j,e in enumerate(row):
                #exclude question no, question text, and None column
                #from entropy calculation
                if j <= 1 or j == len(row)-1:
                    continue
                else:
                    vals.append(int(e))
            
            entropy = 0
            total_vals = sum(vals)
            termlst = []
            for v in vals:
                t = float(v) / float(total_vals)
                if t > 0:
                    termlst.append(t)
            
            for t in termlst:
                entropy += t * math.log(t, 2)
            entropy = -entropy
            #print(i)
            resdict[row[0]] = (max_entropy, entropy)
    
    return resdict
            

def make_ent_row(kr_name, krdict):
    new_row = []
    new_row.append(kr_name)
    for i in range(1, 28):
        entropy = krdict['Q' + str(i)][1]
        ent_str = '%.2f' % entropy
        #only use the median for now
        new_row.append(ent_str)
    
    return new_row

#Generate the MM Entropies shown in Table 3 of our paper
def genTable3Entropies():
    ourname = 'our_mmq_counts.csv'
    gcsname = 'gcs_mmq_counts.csv'
    dhname = 'datahub_mmq_counts.csv'
    
    ourdict = create_entropy_dict(ourname)
    print(ourdict)
    print(len(ourdict.values()))
    gcsdict = create_entropy_dict(gcsname)
    print(gcsdict)
    print(len(gcsdict.values()))
    dhdict = create_entropy_dict(dhname)
    print(dhdict)
    print(len(dhdict.values()))
    
    rows = []
    header = ['MM']
    for i in range(1, 28):
        header.append('Q' + str(i))
    
    rows.append(header)
    
    our_row = make_ent_row('5W1H', ourdict)
    gcs_row = make_ent_row('GCS', gcsdict)
    dh_row = make_ent_row('Datahub', dhdict)
    
    rows.append(our_row)
    rows.append(gcs_row)
    rows.append(dh_row)
    
    restable = tabulate.tabulate(rows, headers='firstrow', tablefmt='latex')
    with open('table3entropies.txt', 'w+') as fh:
        fh.write(restable)

#genTable3Entropies()

def create_norm_ent_dict(fname):
    resdict = {}
    with open(fname, 'r') as fh:
        csvreader = csv.reader(fh)
        for i,row in enumerate(csvreader):
            if i == 0:
                continue
            row_len = len(row)
            #compute max entropy
            max_entropy = 0
            for k in range(row_len - 2):
                frac = float(1) / float(row_len - 1)
                max_entropy += frac * math.log(frac, 2)
            max_entropy = -max_entropy
            vals = []
            for j,e in enumerate(row):
                if j <= 1 or j == len(row)-1:
                    continue
                else:
                    vals.append(int(e))
            
            entropy = 0
            total_vals = sum(vals)
            termlst = []
            for v in vals:
                t = float(v) / float(total_vals)
                if t > 0:
                    termlst.append(t)
            
            for t in termlst:
                entropy += t * math.log(t, 2)
            entropy = -entropy
            efficiency = entropy / max_entropy
            #print(i)
            resdict[row[0]] = efficiency
            
    return resdict

def make_norm_ent_row(kr_name, krdict):
    new_row = []
    new_row.append(kr_name)
    for i in range(1, 28):
        efficiency = krdict['Q' + str(i)]
        ent_str = '%.2f' % efficiency
        #only use the median for now
        new_row.append(ent_str)
    return new_row
        
        
#Generate the Normalized Entropies shown in Table 6
def genTable4NormalizedEntropies():
    ourname = 'our_mmq_counts.csv'
    gcsname = 'gcs_mmq_counts.csv'
    dhname = 'datahub_mmq_counts.csv'
    
    ourdict = create_norm_ent_dict(ourname)
    print(ourdict)
    print(len(ourdict.values()))
    gcsdict = create_norm_ent_dict(gcsname)
    print(gcsdict)
    print(len(gcsdict.values()))
    dhdict = create_norm_ent_dict(dhname)
    print(dhdict)
    print(len(dhdict.values()))
    
    rows = []
    header = ['MM']
    for i in range(1, 28):
        header.append('Q' + str(i))
    
    rows.append(header)
    
    our_row = make_norm_ent_row('5W1H', ourdict)
    gcs_row = make_norm_ent_row('GCS', gcsdict)
    dh_row = make_norm_ent_row('Datahub', dhdict)
    
    rows.append(our_row)
    rows.append(gcs_row)
    rows.append(dh_row)
    
    print(rows)
    
    restable = tabulate.tabulate(rows, headers='firstrow', tablefmt='latex')
    with open('table4normentropies.txt', 'w+') as fh:
        fh.write(restable)

#genTable6NormalizedEntropies()

def create_none_dict(fname):
    resdict = {}
    with open(fname, 'r') as fh:
        csvreader = csv.reader(fh)
        for i,row in enumerate(csvreader):
            if i == 0:
                continue
            row_len = len(row)
            num_nones = int(row[row_len - 1])
            total_users = sum([int(x) for x in row[2:]])
            max_resp = max([int(x) for x in row[2:]])
            is_max_resp = False
            if max_resp == num_nones:
                is_max_resp = True

            resdict[row[0]] = [num_nones, total_users, is_max_resp]
    
    return resdict

def make_noneprop_row(kr_name, krdict):
    new_row = []
    new_row.append(kr_name)
    total = 0
    for i in range(1, 28):
        num_nones = krdict['Q' + str(i)][0]
        total_resps = krdict['Q' + str(i)][1]
        is_max_resp = krdict['Q' + str(i)][2]
        total += num_nones
        none_prop = float(num_nones) / float(total_resps)
        ent_str = '%.2f' % none_prop
        if is_max_resp:
            ent_str += '*'
        #only use the median for now
        new_row.append(ent_str)
    new_row.append(str(total))
    
    return new_row

def genTable5NonePropsTable():
    ourname = 'our_mmq_counts.csv'
    gcsname = 'gcs_mmq_counts.csv'
    dhname = 'datahub_mmq_counts.csv'
    
    ourdict = create_none_dict(ourname)
    print(ourdict)
    gcsdict = create_none_dict(gcsname)
    print(gcsdict)
    dhdict = create_none_dict(dhname)
    print(dhdict)
    
    rows = []
    
    header = ['MM']
    for i in range(1, 28):
        header.append('Q' + str(i))
    
    header.append('Total')
    
    our_row = make_noneprop_row('5W1H', ourdict)
    gcs_row = make_noneprop_row('GCS', gcsdict)
    dh_row = make_noneprop_row('Datahub', dhdict)
    
    rows.append(header)
    rows.append(our_row)
    rows.append(gcs_row)
    rows.append(dh_row)
    
    restable = tabulate.tabulate(rows, headers='firstrow', tablefmt='latex')
    with open('table5noneproptable.txt', 'w+') as fh:
        fh.write(restable)

#genTable4NonePropsTable()

