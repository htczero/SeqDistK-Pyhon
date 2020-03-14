# SeqDistK-Pyhon
### Home 

Calculate the dissimilarity between sequence

### Requirments
numpy 1.16  
numba 0.43.1  
tqdm  
python 3.7  

MiniConda is recommended. Also Anaconda3 is ok. 




### Example  
0. Start the program 
``` python
python main.py
```    
If you have N sequences file in a directory and the directory path is '/home/seqs'  

1. Input the directory path  
``` python
Input the directory path of sequences : /home/seq
```  

2. Input the k you want to calculate(k > 0)  
For single k, input a integer(>0), such as 4  
``` python  
Input the k : 4
```

For a series of k, input kmin-kmax-step. For example(without quotation marks), '2-10-2', it means, [2, 4, 6, 8, 10]"  
``` python  
Input the k : 2-10-2
```

3. Select the dissimilarities  
``` python  
0. Ma  
1. Ch  
2. Eu  
3. d2  
4. Hao  
5. d2S  
6. d2Star  
For example(without quotation marks), '1,2,3,4'  
Input the dissimilarities : 0,1,2,4,5
```  

4. If in the step 3, d2S or d2Star is selected. You need to input "Markov possibility order"  
For single order, input a interger(>=0)  
``` python
Input the possibility order : 2
```  

For a series of order, separation with ','. For example(without quotation marks), '0, 1, 2, 3'  
```python
Input the possibility order : 0,1,2
```  

5. Input the path you want to save. For example, "/home/save"
``` python  
Input the path you want to save : /home/save
```  

6. Check the parameters. 
``` python
Check the parameters : 'yes' or 'no'  
yes  # input yes and press enter if the parameters are correct.
```  

### Manuals  


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

 
### For Windows  
For Windows, we recommend a Windows version.  
https://github.com/htczero/SeqDistK  
It is more faster than and more convenient python version.


### FAQ  
&nbsp;&nbsp;&nbsp;&nbsp;Q1:&nbsp;&nbsp;Can I pause if the program is running?  
&nbsp;&nbsp;&nbsp;&nbsp;A1:&nbsp;&nbsp;No

&nbsp;&nbsp;&nbsp;&nbsp;Q2:&nbsp;&nbsp;What is the range of k?    
&nbsp;&nbsp;&nbsp;&nbsp;A2:&nbsp;&nbsp;K should be no more than 15 (<=15). 

&nbsp;&nbsp;&nbsp;&nbsp;Q3:&nbsp;&nbsp;What is the difference between Windows version and this?   
&nbsp;&nbsp;&nbsp;&nbsp;A3:&nbsp;&nbsp;For windows version, it use C# and has UI. Further more, using multi-threading, Windows version  is more faster than python version. 

&nbsp;&nbsp;&nbsp;&nbsp;Q4:&nbsp;&nbsp;Can I use it in MacOS?    
&nbsp;&nbsp;&nbsp;&nbsp;A4:&nbsp;&nbsp;Of course.
