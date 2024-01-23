# Bloom filter

## Use case

- Check if an element is in a very large set of elements.

## Algorithm

- Initialize a bit array of size m with all bits set to 0.
- For each element, hash it k times to get k different hash values. (or use k different hash functions)
  - Set the bits at the k hash values to 1.
- After all elements are hashed, to check if an element is in the set, hash it k times and check if all the bits at the k hash values are 1.

## Time complexity

- Construction: O(kn) --> O(n)
  - n is the number of elements
  - k is the number of hash functions
- Query: O(k) --> O(1)

## Space complexity

- O(m) (m is the size of the bit array)
  - m = -n\*ln(p) / (ln(2))^2

## Drawbacks

- False positive is possible -- If the different values are hashed to the same k hash values, then the bits at the k hash values will be set to 1, and the element will be considered as in the set when it's not.
- The probability of false positive can be calculated by the formula below.
  - p = (1 - e^(-k/(m/n)))^k
  - k is the number of hash functions
  - n is the number of elements
  - m is the size of the bit array

## References

- [4 เทคนิคที่ควรรู้ในการทำงานกับ Streaming Data](https://medium.com/linedevth/4-เทคนิคที่ควรรู้ในการทำงานกับ-streaming-data-b98f20d75e2f)
- [Bloom Filter Calculator](https://hur.st/bloomfilter/)
