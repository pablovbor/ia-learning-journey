# In this project, Im going to operate with a sales dataset were rows are products and columns are months

import numpy as np

sales = [[120,90,100,80],
         [200,150,180,170],
         [90,100,110,120],
         [300,250,270,280]
        ]


def main():
    sales_array = np.array(sales) # Convert the sales list to a numpy array
    print(sales_array) 
    
    print(sales_array[0, :]) # Print the sales of the first product (first row)
    print(sales_array[:, 1]) # Print the sales of the second month (second column)
    print(sales_array[1, 2]) # Print the sales of the second product in the third month (second row, third column)

    
    #max_sales_product = 0
    #sales_product_index = 0
    #for i in range(sales_array.shape[0]): 
    #    sales_product = 0
    #    for j in range(sales_array.shape[1]): 
    #        sales_product += sales_array[i, j] 
    #    if sales_product > max_sales_product: 
    #        max_sales_product = sales_product
    #        max_sales_product_index = i
    #print(f"Product with highest sales: {max_sales_product_index}")
    #print(f"Highest sales: {max_sales_product}")

    total_sales = sales_array.sum(axis=1) # axis = 1 sums all values in each row (total sales per product) 
    best_product = np.argmax(total_sales) # takes the argument of the best product
    print(f"The best product is: {best_product} with {total_sales[best_product]} sales")
main()