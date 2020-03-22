### For Windows Users 

For Windows Users, we recommend a Windows distribution with convenient graphical user interface:  
https://github.com/htczero/SeqDistK. It is C# based and much faster than this python distribution.

# SeqDistK-Pyhon

### Introduction 

Phylogenetic tools are fundamental to studies of evolution and taxonomy. In this paper, we present SeqDistK, a novel tool for alignment-free phylogenetic analysis. SeqDistK batch computes the pairwise distance matrix between biological sequences, using seven popular k-mer based dissimilari-ty measures. Based on the matrix, SeqDistK constructs a phylogenetic tree using the Unweighted Pair Group Method with Arithmetic Mean algorithm. Using a golden-standard dataset of 16S rRNA sequences and the associated phylogenetic tree, we benchmarked the accuracy and efficiency of SeqDistK. We found the measure d2S (k=5, M=2) was the best, which correctly clustered and classified all sequences. Compared to multiple aligners such as Muscle, Clustalw2 and Mafft, SeqDistK was tens to hundreds of times faster, which helps eliminating the computation limit encountered by large-scale phylogenetic analysis. 

### Overview  

SeqDistK, which can calculate the dissimilarity between sequences, a novel tool to efficiently compute seven widely accepted k-mer statistics: Chebyshev, Manhattan, Euclidian, Hao, d2, d2S and d2star, and perform alignment-free phylogenetic analysis. SeqDistK constructs a phylogenetic tree from a batch of input sequences in four steps: (1) it counts the k-mer frequency in each input sequence; (2) it merges the obtained k-mer frequencies into a 4N-by-N matrix, where N is the number of input sequences; (3) it uses the provided dissimilarity measure, and parameters k and M (if needed) to calculate the pairwise distance, obtaining a N-by-N distance matrix, where M is the order of background Markov model; (4) it applies the Unweighted Pair Group Method with Arithmetic Mean (UPGMA) algorithm to the distance matrix and constructs the phylogenetic tree.  
  
Fig. 1. The Strategy of SeqDistK. In (a), we illustrated the algorithm and associated data structure for k-mer searching, counting and storage as implemented in SeqDistK. In principle, we mathematically transformed k-mer to an index that can randomly address and operate an array-based memory storage efficiently. Phylogenetic trees from 16S rRNA sequences using 7 dissimilarity measures (b) the ground truth tree and (c) dissimilarity measures d2S(k=8, M=0)  

![Strategy](/doc/img/1.png)

### Requirments

numpy 1.16  
numba 0.43.1  
tqdm  
python 3.7  

MiniConda is recommended. 
Using Anaconda3 is also ok. 

### Example  
0. Start the program 
``` python
python main.py
```    
Suppose you have N input sequences file in a directory and the directory path is '/home/seqs'  

1. Input the directory path  
``` python
Input the directory path of sequences : /home/seq
```  

2. Input the k, the size of k-mer, you want to compute (k > 0).
See the reference paper for how to choose a measure for details.

For a single k, input a integer(>0), such as 4  
``` python  
Input the k : 4
```

For a range of k, input kmin-kmax-step. 
For example(without quotation marks), '2-10-2', which specifies k = [2, 4, 6, 8, 10]"  
``` python  
Input the k : 2-10-2
```

3. Choose the dissimilarity measure. 
See the reference paper for how to choose a measure for details.

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

4. If in the step 3, d2S or d2Star was chosen, 
one also needs to give M, the order of Markov background model. 
See the reference paper for how to choose M for details.

For a single M, input a interger(>=0)  
``` python
Input the possibility order : 2
```  

For a series of M, separation them with ','. 
For example(without quotation marks), '0, 1, 2, 3'  
```python
Input the possibility order : 0,1,2
```  

5. Input the path you want to save the results. 
For example, "/home/save"
``` python  
Input the path you want to save : /home/save
```  

6. Confirm the parameters are correct before submit the computaiton. 
``` python
Check the parameters : 'yes' or 'no'  
yes  # input yes and press enter if the parameters are correct.
```  

### Manuals  

### Structure of working directory  
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

### FAQ  
&nbsp;&nbsp;&nbsp;&nbsp;Q1:&nbsp;&nbsp;Can I pause if the program is running?  
&nbsp;&nbsp;&nbsp;&nbsp;A1:&nbsp;&nbsp;No

&nbsp;&nbsp;&nbsp;&nbsp;Q2:&nbsp;&nbsp;What is the range of k?    
&nbsp;&nbsp;&nbsp;&nbsp;A2:&nbsp;&nbsp;K should be no more than 15 (<=15). 

&nbsp;&nbsp;&nbsp;&nbsp;Q3:&nbsp;&nbsp;What is the difference between Windows version and this?   
&nbsp;&nbsp;&nbsp;&nbsp;A3:&nbsp;&nbsp;For windows version, it use C# and has UI. Further more, using multi-threading, Windows version  is mush faster than python version. 

&nbsp;&nbsp;&nbsp;&nbsp;Q4:&nbsp;&nbsp;Can I use it in MacOS?    
&nbsp;&nbsp;&nbsp;&nbsp;A4:&nbsp;&nbsp;Of course.
