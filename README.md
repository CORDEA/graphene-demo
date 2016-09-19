# Demonstration of Graphene

[Graphene](http://graphene-python.org/) is a Python library for building GraphQL.

## Query

```
query SampleQuery {
  stock {
    id
    count
    books {
      id
      title
      description
      price
      isRent
      isSold
    }
  }
}

mutation SampleMutations {
  arrival(price: 0, title: "", description: "") {
    reason
    success
    book {
      id
      # ...
    }
  }
  sold(id: 1) {
    reason
    success
    book {
      id
      # ...
    }
  }
  rent(id: 1) {
    reason
    success
    book {
      id
      # ...
    }
  }
}
```
