### For Windows Users 

For Windows Users, we recommend a Windows distribution with convenient graphical user interface:  
https://github.com/htczero/SeqDistK. It is C# based and much faster than this python distribution.

# **SeqDistK**-Pyhon

## Introduction 

Phylogenetic tools are fundamental to studies of evolution and taxonomy. We present **SeqDistK**, a novel tool for alignment-free phylogenetic analysis. **SeqDistK**, batch computes the pairwise distance matrix between biological sequences, using seven popular k-mer based dissimilarity measures. Based on the matrix, **SeqDistK**, constructs a phylogenetic tree using the Unweighted Pair Group Method with Arithmetic Mean algorithm. We illustrated the steps of **SeqDistK**, constructing a phylogenetic tree: (1) it counts k-mer occurrence in each input sequence; (2) it gathers k-mer occurrence vectors from all input sequences; (3) it computes the distance matrix of the input sequences using specifiable dissimilarity measures; (4) it draws the phylogenetic tree using the Unweighted Pair Group Method with Arithmetic Mean (UPGMA) algorithm via Phylip. Using a golden-standard dataset of 16S rRNA sequences and the associated phylogenetic tree, we benchmarked the accuracy and efficiency of **SeqDistK**.

**SeqDistK** was implemented with several advanced programming techniques: (1) It makes full use of multi-thread programming to improve CPU use through multi-core optimization. It is highly responsive even on personal computers. (2) It has a graphical interface that is simple, intuitive, and easy to interact with. (3) It is fully compatible with all current versions of a major operation system – MS Windows, Linux and MAC platforms.

## Strategy  

**SeqDistK**, which can calculate the dissimilarity between sequences, a novel tool to efficiently compute seven widely accepted k-mer statistics: Chebyshev, Manhattan, Euclidian, Hao, d2, d2S and d2star, and perform alignment-free phylogenetic analysis. In Fig. 1., we illustrated the algorithm and associated data structure for k-mer searching, counting and storage as implemented in **SeqDistK**. In principle, we mathematically transformed k-mer to an index that can randomly address and operate an array-based memory storage efficiently. Given the fact that k-mer based statistics were mostly useful for phylogenetic analysis when k is relatively small (<16), we implemented in **SeqDistK** a mature and simple algorithm to count k-mers frequency. (1) we record the k-mer frequency into a 4^k vector for each input sequence. If N input sequences were to be compared, their merged vectors are stored in a 4^k N matrix. (2) A user specifies the desired dissimilarity measure(s), which **SeqDisK** will use to calculate the distance matrix, which is a N-by-N matrix. (3) Finally, with this distance/dissimilarity matrix, **SeqDisK** employs the Unweighted Pair Group Method with Arithmetic Mean (UPGMA) to construct the phylogenetic tree. At the last step, SeqDisK can also perform clustering analysis of the sequences based on the distance matrix.

![Strategy](/doc/img/Fig1.png)
**Fig. 1.** The Strategy of **SeqDistK**  
  
  

## Example1    

In the example illustrated in **Fig. 2**., we analyzed four input sequences with 5-mer statistics and constructed their phylogenetic tree. When k=5, there are 4^5 combinations of k-mer. Taking GCCGT as our example, in the first step, we counted the frequency of GCCGT. In the next step, the frequency vectors of GCCGT and all other 5-mers from each sequence were combined to form a matrix. In the third step, we computed the dissimilarity matrix by pairwise comparison of all k-mer vectors using the dissimilarity measures. And in the last step, we used UPGMA to draw the inferred phylogenetic tree using the open source software Phylip.

![Strategy](/doc/img/Fig2.png)  
**Fig. 2.** The Workflow of **SeqDistK**  
  
  

## Example2   
 We can use 7 steps to complete the program of **SeqDistK**
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


## Example3

While alignment-free phylogenetic analysis is unrestricted to specific genes, we used a golden standard 16S rRNA dataset as benchmark for its wide acceptance. We downloaded a golden standard dataset of 100 16S rRNA sequences and the associated and expert-curated phylogenetic tree from the All-species Living Tree Project (LTP) by Yilmaz and Beccati et al (2014). All sequenced strains of archaea and bacterial species were classified and preserved in LTP. There are 7 dissimilarity measures Eu, Ma, Ch, d2, d2star, d2S and Hao in **SeqDistK**. We draw the phylogenetic tree using dissimilarity measure d2S (k=8, M=0) as in **Figs. 3. (a) and (b)**.

![Strategy](/doc/img/Fig3.png)  
**Fig.3.** **(a)** the ground truth tree and **(b)** dissimilarity measures d2S (k=8, M=0)  
  
  

## Requirments

numpy 1.16  
numba 0.43.1  
tqdm  
python 3.7  

MiniConda is recommended. 
Using Anaconda3 is also ok. 


## Manuals  

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

## FAQ  
&nbsp;&nbsp;&nbsp;&nbsp;Q1:&nbsp;&nbsp;Can I pause if the program is running?  
&nbsp;&nbsp;&nbsp;&nbsp;A1:&nbsp;&nbsp;No

&nbsp;&nbsp;&nbsp;&nbsp;Q2:&nbsp;&nbsp;What is the range of k?    
&nbsp;&nbsp;&nbsp;&nbsp;A2:&nbsp;&nbsp;K should be no more than 15 (<=15). 

&nbsp;&nbsp;&nbsp;&nbsp;Q3:&nbsp;&nbsp;What is the difference between Windows version and this?   
&nbsp;&nbsp;&nbsp;&nbsp;A3:&nbsp;&nbsp;For windows version, it use C# and has UI. Further more, using multi-threading, Windows version  is mush faster than python version. 

&nbsp;&nbsp;&nbsp;&nbsp;Q4:&nbsp;&nbsp;Can I use it in MacOS?    
&nbsp;&nbsp;&nbsp;&nbsp;A4:&nbsp;&nbsp;Of course.

### CONTACTS  
Questions and comments shall be writted in issue.
