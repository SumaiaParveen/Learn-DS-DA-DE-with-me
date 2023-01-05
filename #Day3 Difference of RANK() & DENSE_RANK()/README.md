### Differences in the results of RANK() and DENSE_RANK() [MS SQL Server example]  

**RANK()** assigns a ranking to each row, with the highest ranked row being assigned a rank of 1. If multiple rows have the same value, they will receive the same rank and the next rank will be skipped. For instance, if two rows have a rank of 1, the following row will have a rank of 3.

**DENSE_RANK()** assigns a ranking to each row in a result set, with the highest ranked row being assigned a rank of 1. However, unlike RANK(), if multiple rows have the same value, there will not be a rank gap between them. For example, if two rows have a rank of 1, the next row will be assigned a rank of 2.

| name   | score | rank | dense_rank |
|--------|-------|------|------------|
| Bob    | 95    | 1    | 1          |
| Dave   | 95    | 1    | 1          |
| Alice  | 85    | 3    | 2          |
| Charlie| 75    | 4    | 3          |
| Eve    | 75    | 4    | 3          |

RANK() assigns a rank of 1 to both the rows with the highest score (95) and skips rank 2. DENSE_RANK(), on the other hand, assigns a rank of 1 to the rows with the highest score (95) and assigns a rank of 2 to the rows with the second highest score (85). The rows with the lowest score (75) are assigned a rank of 3 by both functions.
