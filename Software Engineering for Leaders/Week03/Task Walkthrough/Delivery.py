'''
We are running a small business. We have a list of 
regions where our customers are ('North', 'South', 'East',
'West'), a dictionary containing how many packages need 
to be sent to each region (50, 30, 20, 40 respectively), 
and another list containing the profit made on each 
successful delivery in that region (5.00, 4.50, 6.00, 5.50 
respectively). The goal is to calculate our expected 
profit.
'''

regions = ['North', 'South', 'East','West']

packages = {
    'North': 50,
    'South' : 30,
    'East' : 20,
    'West' : 40
}

profit_per_delivery = [5.00, 4.50, 6.00, 5.50]

expected_profit = 0

# 50 x 5.00
# packages['North'] * profit_per_delivery[0]
# packages['South'] * profit_per_delivery[1]

for i, region in enumerate(regions):
    # first iteration: i = 0 and region = 'North'
    # second iteration: i = 1 and region = 'South'
    region_profit = packages[region] * profit_per_delivery[i]

    expected_profit += region_profit

print(expected_profit)

