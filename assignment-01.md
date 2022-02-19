

# CMPS 2200 Assignment 1

**Name:**_________________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
        This function, when given a value, will first check if the value is 1 or less, if it is, that value will simply be returned.
        If the value is greater than 1 it will assign a variable aVar as the function called on the previous value, and assign another
        variable bVar as the function called on the value from 2 iterations previous. It will then return the sum of aVar and bVar.
        The function could have included a for loop inside the "else: " statement but since it was not, the function could be called 
        within a for loop to print each value of the sequence. I assigned 2 variables instead of just calling the funtion 
        like: return(recrFib(n-1) + recrFib(n-2)) because it seemed more accurate to the SPARC function to assign variables. The function will
        return the fibonacci sequence one term at a time up to the value given to recrFib(), assuming the function is called in a for loop.
.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
        The work of this implimentation is just O(n) because the algorithm iterates through n items in a list, so it has a linear runtime.
        Thus, the span is also O(n).
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
      The work of the recursive form of this algorithm is: W(n) = 2W(n/2) + k. We get 2 * W(n/2) because we split the list into 2 parts, so now each one takes only       1/2 of the work. So, we have W(n/2) work for each of 2 smaller lists and constant k represents merging the lists back together, beacuse it takes some additional work each time we combine. The merging work is constant because we do not use any for loops to combine the list back together and it will only happen the amount of times the function is called. 
      
      The span is also: S(n) = 2W(n/2) + k because there is no parallelism involved and the computer must still do 1 task at a time. So the Span will be the same as the work for creating 2 smaller lists and merging them back together to find the longest streak.
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?
  The work required for this algorithm will not change with paralellism, because we still have the same amount of work to do, we can just do it in a shorter amount of time. So, work would be: W(n) = 2W(n/2) + k.
  
  We can reduce the span by the amount of tasks the computer is asked to do at once, in this case it would be to evaluate each of 2 smaller lists at once, so we can divide the span by the new amount of tasks it can do at once: 2, to get S(n) = S(n/2) + k, because we can now evaluate each list simultaneously. We could think about it like: now span is the time it takes the algorithm to analyze only 1 of the smaller lists, because it is analyzing them both at the same time.

.  
.  
.  
.  
.  
.  
.  
.  

