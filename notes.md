# Useful commands for data processing

## Get data
* Use pandas

[pandas.read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)

    data = pandas.read_csv(file_path)

'data' will be a [pandas.DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).
Note that the first line in the file will turn into tags. Use'.keys()' to show all the tags.

* Use numpy

[numpy.loadtxt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)

    data = numpy.loadtxt(fname, dtype=float, usecols=(,2), delimiter=' ')
'data' will be a numpy.ndarray.

## Rearrange data
#### numpy array methods
* [numpy.concatenate](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html#numpy.concatenate)
: Concatenate a list of arrays. All the input arrays must have same number of dimensions.

        >>> a = np.array([[1, 2], [3, 4]])
        >>> b = np.array([[5, 6]])
        >>> np.concatenate((a, b), axis=0)
        array([[1, 2],
               [3, 4],
               [5, 6]])
           
* [numpy.block](https://docs.scipy.org/doc/numpy/reference/generated/numpy.block.html#numpy.block)
    : Assemble an nd-array from nested lists of blocks.
    
        A = np.ones((2, 2), int)
        >>> B = 2 * A
        >>> np.block([A, B])
        array([[1, 1, 2, 2],
               [1, 1, 2, 2]])    
               
* [numpy.reshape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)
    ：Gives a new shape to an array without changing its data.

        a = a.reshape((-1,1))
        
* [numpy.ndarray.astype](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html)
    : Copy of the array, cast to a specified type.
    
        x = x.astype(int)

* [numpy.delete(arr, obj, axis=None)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.delete.html)
    : Return a new array with sub-arrays along an axis deleted.
    
        >>> a
        array([1, 1])
        >>> np.delete(a, 0)
        array([1])
        >>> arr
        array([[ 1,  2,  3,  4],
               [ 5,  6,  7,  8],
               [ 9, 10, 11, 12]])
        >>> np.delete(arr, 1, 0)
        array([[ 1,  2,  3,  4],
               [ 9, 10, 11, 12]])



## Statistics
#### Counter
##### [.most_common(n)](https://docs.python.org/2/library/collections.html#collections.Counter.most_common)
return n most common items, as a list of tuples:(item, its counts).

    >>> Counter(label).most_common(1)[0][0]
    1

#### List or array
#####[cmp(a, b)](https://sjolzy.cn/Python-39-s-built-in-comparison-function-cmp-comparison-principle-analysis.html)
Built-in function in python2. 

Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y.

##Built-in KMeans
#### [sklearn.cluster.KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
Use K-means algorithm

    >>> from sklearn.cluster import KMeans
    >>> import numpy as np
    >>> X = np.array([[1, 2], [1, 4], [1, 0],
    ...               [4, 2], [4, 4], [4, 0]])
    >>> kmeans = KMeans(n_clusters=2, init=‘k-means++’, random_state=0).fit(X)
    >>> kmeans.labels_
    array([0, 0, 0, 1, 1, 1], dtype=int32)
    >>> kmeans.predict([[0, 0], [4, 4]])
    array([0, 1], dtype=int32)
    >>> kmeans.cluster_centers_
    array([[ 1.,  2.],
           [ 4.,  2.]])

