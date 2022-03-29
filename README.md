# Phylogeny
Contructs bifurcating phylogenetic trees from data that has an associated distance function

## Example

For the input sequence of integers `625, 390, 400, 410, 605` and distance function 'distance(x,y)=|x-y|', the following tree is outputted:

```
Node
 |_ Node
     |_ 605
     |_ 400
 |_ Node
     |_ 410
     |_ Node
         |_ 625
         |_ 390
```

## Todo

- Better commenting
- Distance function for genetic sequences
