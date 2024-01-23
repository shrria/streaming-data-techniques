# Reservoir sampling

## Use case

- Randomly select k samples from a set of n elements, where n is either a very large or unknown number (streaming data).

## Algorithm

- Initialize an array of size k with the first k elements of the stream.
- For each new element in the stream (starting at (k+1)th item), randomly replace an element in the array with the new element with probability k/n.
  - To implement the probability, generate a random number from 0 to current index. If the generated number is smaller than k, then replace the element at the random index with new element.

## Time complexity

- O(n)

## Space complexity

- O(k)

## References

- [4 เทคนิคที่ควรรู้ในการทำงานกับ Streaming Data](https://medium.com/linedevth/4-เทคนิคที่ควรรู้ในการทำงานกับ-streaming-data-b98f20d75e2f)
- [Reservoir sampling](https://www.geeksforgeeks.org/reservoir-sampling/)
