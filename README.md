# CS3012
CS3012 assignment submission in Python for both LCA and DAG.


 <i><b>Explanation of the LCA</b></i>

 The lowest common ancestor (LCA) of two nodes v and w in a tree is the lowest node that has both v and w as descendants.

 Some of the tests I look for include:

 <b>Tests</b>

 1. Check for the lowest common ancestory
 2. Test the constructor
 3. Test a null tree
 4. Test for duplicates
 5. Test when only one node
 6. Test 'get' 
 7. Test height of tree
 8. Test for non standard characters


<i><b>Explanation of a DAG</b></i>

The directed graph will have nodes pointing to one and other similar to the binary tree above except they will be joining other nodes from different branches at an early or later stage. Not all nodes have edges(connections) leading into them(known as indegree) and not all have edges leading out of them(known as outdegree). A directed acyclic graph will be the same except once a node/vertex is visited, there should be no ability to return to this node(ie there is no cycle within the graph). There must be atleast one vertex/node that has 0 indegrees.

<b>Tests</b>

1. Test the constructor
2. Test for adding nodes / connecting nodes together
3. Test for deleting nodes / disconnecting nodes from one another
4. Checking the LCA
