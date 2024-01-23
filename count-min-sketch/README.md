# Count-min sketch

## Use case

- Counting the frequency of events in a stream

## Algorithm

- Initialize a two-dimensional array (table) of size `d` by `w` with all zeros.
- For each new element in the stream, hash it `d` times to get `d` different values.
- For each of the `d` values, increment the value in the table at the corresponding row and column by 1.

- To get the frequency of an element, hash it `d` times to get `d` different values.

## Time complexity

- Construction: O(dn) --> O(n)
  - n is the number of elements
  - d is the number of hash functions
- Query: O(d) --> O(1)

## Space complexity

- O(dw)
  - d is the number of hash functions
  - w is the width of the table

## Drawbacks

- Over-estimation is possible -- If the different values are hashed to the same `k` hash values, then the values in the table at the corresponding rows and columns will be incremented by 1, and the frequency of the element will be overestimated.
- Under-estimation is not possible.

- Theory: truth <= estimate, and estimate <= truth + epsilon \* n

  - truth: the actual frequency of the element
  - estimate: the frequency of the element estimated by the algorithm
  - epsilon(ε): the error factor
  - n: the number of elements

- Initially, the error probability was determined as `delta δ`, and the error factor was determined as `epsilon ε`. Then, we can have:

  - w: e / ε
    - w is the width of the table
  - d: max(1, ln(1 / δ))
    - d is the number of hash functions (depth)

## References

- [4 เทคนิคที่ควรรู้ในการทำงานกับ Streaming Data](https://medium.com/linedevth/4-เทคนิคที่ควรรู้ในการทำงานกับ-streaming-data-b98f20d75e2f)
- [Count-Min Sketching, Configuration & Point-Queries](https://crahen.github.io/algorithm/stream/count-min-sketch-point-query.html)
