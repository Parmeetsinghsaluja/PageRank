This is the implementation of given Page Rank Algorithm


The given algorithm was implementes in python.


Citations:
To develop this program I have used following libraries of python:
1)collections -to use Counter class and its functionality
2)math -to use its function like log and power
3)itemgetter - to use functions which apply on objects

How to run:
1. Install Pythonv2.7.4
2. The implementation is in Parmeetsingh_Saluja_TuTh_HW2 folder so change your directory to Parmeetsingh_Saluja_TuTh_HW2 folder.
3. Run the implementation by entering command on your command line python by command -
   python filename
   For Example- python Page_Rank_Implementation.py
4. The program takes input a file which contains the graph as mentioned in problem statement and outputs the pagerank.
5. On executing the program:
     1. Program asks user to Enter the Graph File Name with extension (.txt)-
     2. You can enter the your own file name with extension (only .txt is acceptable) and remember to keep in same directory as the program file and do see Note(below).
     3. Otherwise, to select default graph file :
              Enter 1 for G1(Graph by BFS Crawling)                 or
              Enter 2 for G2(Graph by DFS Crawling)
    4.Then,program asks user to Enter the File Name in which you want to store Perplexities with extension-
    5. You can enter the your own file name with extension (only .txt is acceptable)
    6. Otherwise, to select default output file :
              Enter 1 for G1(Graph by BFS Crawling) and you will get output in Perplexity_G1.txt              or
              Enter 2 for G2(Graph by DFS Crawling) and you will get output in Perplexity_G2.txt

Note:
The Graph is space seperated and the last value in each line also ends with space. So,if you use anytime your own graph file remember to follow this guidline of Graph file.


