# SeqDistK-Pyhon
Calculate the dissimilarity between sequence

### Requirments
numpy 1.16  
numba 0.43.1  
tqdm  
python 3.7 


### Usage  
python main.py  

### Structure of directory  
Single directory  
|--dir  
&nbsp;&nbsp;&nbsp;&nbsp;|--seq_1.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;|--seq_2.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;|--seq_3.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;|--seq_4.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;:  
&nbsp;&nbsp;&nbsp;&nbsp;|--seq_n.fasta  
For one directory with n sequences, you will obtain a csv file with n by n matrix for difference conditions.  


Multiple directory  
|--root  
&nbsp;&nbsp;&nbsp;&nbsp;|--dir_1   
&nbsp;&nbsp;&nbsp;&nbsp;|--dir_2   
&nbsp;&nbsp;&nbsp;&nbsp;|--dir_3   
&nbsp;&nbsp;&nbsp;&nbsp;|--dir_4   
&nbsp;&nbsp;&nbsp;&nbsp;:  
&nbsp;&nbsp;&nbsp;&nbsp;|--dir_n  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--seq_1.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--seq_2.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--seq_3.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--seq_4.fasta  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--seq_n.fasta  
For each dir_x, it can be seen as a case of single directory. 