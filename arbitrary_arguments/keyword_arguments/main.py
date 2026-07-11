def filter_products_by_budget(budget, **kwargs):
    affordable_products = {} 
    product_in_budget = 0
    for product, price in kwargs.items():
        if price <= budget:
            affordable_products[product] = price
            product_in_budget += 1
    
    if product_in_budget == 0:
        return 'No products available within the budget.'
    
    return f'Available products within budget: {affordable_products}'

# Testing the result
print(filter_products_by_budget(100, laptop=1200, smartphone=800, mouse=50, keyboard=90, headphones=150))