# rosalind-python
My solutions to the problems in [Rosalind's Python Village](http://rosalind.info)


## Python Village

This track is mainly to get you comfortable using the rosalind platform. For each problem you code the
solution, and then download the dataset from the [website](http://rosalind.info). Run your program with
this dataset as the input, and upload the output on the website.

- [Installing Python](http://rosalind.info/problems/ini1/)
- [Variables and some Arithmetic](http://rosalind.info/problems/ini2/)
- [Strings and Lists](http://rosalind.info/problems/ini3/)
- [Conditionals and Loops](http://rosalind.info/problems/ini4/)
- [Working with Files](http://rosalind.info/problems/ini5/) For this problem, open your output file and copy the contents. Paste that into the answer box on the rosalind website.
- [Dictionaries](http://rosalind.info/problems/ini6/)


## Algorithmic Heights
This track has classic algorithm problems.
- [rosalind_in.txt] This file is where I put the sample inputs.
- [rosalind_out.txt] The program writes the output to this file.
- [Majority Element](http://rosalind.info/problems/list-view/?location=algorithmic-heights) The question asks which element occurs more than half the number of times in the array. After sorting, check the count of middle element. If it is more than half, that is the answer, else -1.
- [Degree Array](http://rosalind.info/problems/deg/) Just make a linear scan through the input and increase the count of every vertex you find.
- [Insertion Sort](http://rosalind.info/problems/ins/) Modified the insertion sort function to return the count of number of swaps, instead of a sorted array.
- [Merge Arrays](http://rosalind.info/problems/mer/) Just scan through both the arrays and add the element that is small er to the final array. The merge function from this problem can be used to solve the merge sort question.
- [Merge Sort](http://rosalind.info/problems/ms/) Added the merge_sort function to the code from Merge array problem.
- [Double Degree array](http://rosalind.info/problems/ddeg/) Simply make a dictionary containing nodes as keys, and add the neighbors to it's value (a list).
## Bioinformatics Textbook Track


## Bioinformatics Armory


## Bioinformatics Stronghold
- [Counting Nucleotides](http://rosalind.info/problems/dna/) Used a dictionary with each nucleotide as a key
- [Transcribing DNA to RNA](http://rosalind.info/problems/rna/) Simple character replacement of 'T' by 'U'
- [Complementing a strand of DNA](http://rosalind.info/problems/revc/) String manipulation with dictionary.
- [Mendel's first law](http://rosalind.info/problems/iprb/) First find the formula for the probability using the various combinations of the alleles. Then just substitute the values.
- [Translating RNA into protein](http://rosalind.info/problems/prot/) Used a dictionary of rna codons to translate rna into protein.
- [Finding a motif in DNA](http://rosalind.info/problems/subs/) Simple O(mn) algorithm that matches the string at each index of the original dna string.
- [Calculating Expected Offspring](http://rosalind.info/problems/iev/) First built a formula based on information provided in the problem.  
 
