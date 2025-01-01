# Laptop API Guide {Lappy API}

Welcome to the **Laptop Data API {Lappy APi}**! This API provides laptop data, including categories, sources, prices, ratings, and more. You can filter the data using various parameters.

## API Base URL

https://lappyapi.vercel.app/laptops


## API Parameters

### 1. Get All Laptops
**Endpoint**: `GET /laptops`  
**Description**: Fetch all laptops data from the API.

GET https://lappyapi.vercel.app/laptops


### 2. Filter by Category
**Endpoint**: `GET /laptops?category={category}`  
**Description**: Filter laptops by category. Example: `gaming laptop`, `office laptop`, etc.

GET https://lappyapi.vercel.app/laptops?category=gaming


### 3. Filter by Source
**Endpoint**: `GET /laptops?source={source}`  
**Description**: Filter laptops by source (e.g., `amazon`, `flipkart`).

GET https://lappyapi.vercel.app/laptops?source=amazon


### 4. Filter by Price
**Endpoint**: `GET /laptops?price_less_than={price}` or `GET /laptops?price_greater_than={price}`  
**Description**: Filter laptops by price. You can use `price_less_than` or `price_greater_than`.

GET https://lappyapi.vercel.app/laptops?price_less_than=60000 GET https://lappyapi.vercel.app/laptops?price_greater_than=50000


### 5. Filter by Rating
**Endpoint**: `GET /laptops?rating_greater_than={rating}` or `GET /laptops?rating_less_than={rating}`  
**Description**: Filter laptops by rating. You can use `rating_greater_than` or `rating_less_than`.

GET https://lappyapi.vercel.app/laptops?rating_greater_than=4 GET https://lappyapi.vercel.app/laptops?rating_less_than=3


### 6. Filter by Deals
**Endpoint**: `GET /laptops?deal={deal}`  
**Description**: Filter laptops by deal availability.

GET https://lappyapi.vercel.app/laptops?deal=yes


### 7. Limit Results
**Endpoint**: `GET /laptops?limit={limit}`  
**Description**: Limit the number of results returned.

GET https://lappyapi.vercel.app/laptops?limit=10


### 8. Get a Random Laptop
**Endpoint**: `GET /laptop/random`  
**Description**: Get a random laptop from the database.

GET https://lappyapi.vercel.app/laptop/random


## Parameter Combinations

### 1. Category + Price
**Endpoint**: `GET /laptops?category={category}&price_less_than={price}`  
**Description**: Filter laptops by both category and price.

GET https://lappyapi.vercel.app/laptops?category=gaming&price_less_than=100000


### 2. Source + Rating
**Endpoint**: `GET /laptops?source={source}&rating_greater_than={rating}`  
**Description**: Filter laptops by source and rating.

GET https://lappyapi.vercel.app/laptops?source=flipkart&rating_greater_than=4


### 3. Deals + Limit
**Endpoint**: `GET /laptops?deal={deal}&limit={limit}`  
**Description**: Filter laptops by deal availability and limit the number of results.

GET https://lappyapi.vercel.app/laptops?deal=yes&limit=5


### 4. Rating + Price + Category
**Endpoint**: `GET /laptops?rating_greater_than={rating}&price_less_than={price}&category={category}`  
**Description**: Filter laptops by rating, price, and category.

GET https://lappyapi.vercel.app/laptops?rating_greater_than=4&price_less_than=80000&category=office


## Footer

Made with ❤️ by Saket Kesar
