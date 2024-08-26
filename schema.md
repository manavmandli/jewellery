Doctype
Masters:

1. City

- city name(data)

2. Item UOM

- uom(data)

3. Payment Mode

- payment mode (data)

Child Table:

1. Item Tax

- tax name(date)
- valid from(date)
- tax percentage(percentage)

2. Purchese Item Details

- Item(link-item)
- UOM(link-item uom)
- purity(float)
- quantity(int)
- amount

3. sales Item Details

- Item(link-item)
- UOM(link-item uom)
- purity(float)
- quantity(int)
- amount

4. Purchase Taxes and Charges

- type(select)(Actual,On Net Total,On Previous Row Amount,On Previous Row Total,On Item Quantity)
- Tax Rate(float)
- amount(currency)

5. Sales Taxes and Charges

- type(select)(Actual,On Net Total,On Previous Row Amount,On Previous Row Total,On Item Quantity)
- Tax Rate(float)
- amount(currency)

  Stock:

1. Item

item basic details(section)

- item name (data)
- disable(check)
- item image(attch)
- item group(link-itemgroup)
  item balance(section)
- item uom(link - item uom)
- item weight(float)(depends on uom)
- item quantity(int)(depends on uom)
  purity(section)
- Purity(select)
- Certificate number(data)
- Hall mark certificate(attach)
  (section)
  -Description

2. Item Group:

- Item Group name(data)
- disabled(check)
  Item Tax(section)
- Taxes(table-Item Tax)
  (section)
- description

3. Stock Ledger

- supplier(link-supplier)
- item (link- item)
- uom (link - uom)
- weight(float)
- quantity(int)
- amount
- Transaction Type(select - debit or credit)

Buying:

1. Supplier

supplier details(section)

- Supplier Name(data)
- shop name(data)
- City(link-city)
- Supplier group(link-supplier group)
- image(attach)
  address & contact(section)
- website (url)
- mobile no.(data)
- secondary/whatsapp no.(data)
- email id (data)
- shop address(data)
  account details(section)
- account holder name(data)
- account number(data)
- bank name(data)
- irfc code(data)
- upi id(data)

2. Supplier Group

- Supplier group name(data)
- disbaled(check)

3. Purchase Invoice

- Date(datetime)
- city(link-city)
- is paid(check)
- is return(check)
- supplier(link-supplier)
- supplier name(fetch from supplier-data)
- purchase item details(link-purchase item details)
- Metal Rate(float)(your business metal rate it shoould be accoding to pure metal rate and per 10 gram)
- Total Item(int)
- Total quantity(int)
- Total net weight(float)(\*\*it is also known as pure weight)
- Total Amount(currency)
- Net Total(currency)
- purchase taxes and charges(link-purchase taxes and charges)
- total taxes and charge(currency)
- grand total(currency)
  payments(section)
- mode of payment(link-payment mode)
- paid amount(currency)
- paid metal(float)
- Outstanding Amount(currency)
- Outstanding weight(float)
  address(section)
- supplier address(fetch from selected supplier- data)
- mobile no.(data-fetch from supplier)
- remark(small text)

4. Supplier Payment Tracker

- Supplier(link - supplier)
- supplier name(data-fetch from supplier)
- created on(date time)
- last updated on(data time)
- Pending amount (currency)
- pending fine(float)

5. Supplier Bill Payment

basic details(section)

- Supplier(link - supplier)
- supplier name (data - fetch from supplier)
- payment date(datetime)
  payment type(section)
- amount(currency)
- purity(select)
- weight(float)
- metal rate(10 gram)

Selling:

1. Customer

customer details(section)

- customer Name(data)
- shop name(data)
- City(link-city)
- customer group(link-supplier group)
- image(attach)
  address & contact(section)
- website (url)
- mobile no.(data)
- secondary/whatsapp no.(data)
- email id (data)
- shop address(data)
  account details(section)
- account holder name(data)
- account number(data)
- bank name(data)
- irfc code(data)
- upi id(data)

2. customer Group

- customer group name(data)
- disbaled(check)

3. Sales Invoice

- Date(datetime)
- city(link-city)
- is paid(check)
- is return(check)
- customer(link-customer)
- customer name(fetch from customer-data)
- sales item details(link-sales item details)
- Metal Rate(float)(your business metal rate it shoould be accoding to pure metal rate and per 10 gram)
- Total Item(int)
- Total quantity(int)
- Total net weight(float)(\*\*it is also known as pure weight)
- Total Amount(currency)
- Net Total(currency)
- sales taxes and charges(link-sales taxes and charges)
- total taxes and charge(currency)
- grand total(currency)
  payments(section)
- mode of payment(link-payment mode)
- paid amount(currency)
- paid metal(float)
- Outstanding Amount(currency)
- Outstanding weight(float)
  address(section)
- customer address(fetch from selected customer- data)
- mobile no.(data-fetch from supplier)
- remark(small text)

4. Customer Payment Tracker

- Customer(link - customer)
- customer name(data-fetch from customer)
- created on(date time)
- last updated on(data time)
- Pending amount (currency)
- pending fine(float)

5. customer Bill Payment

basic details(section)

- customer(link - customer)
- customer name (data - fetch from customer)
- payment date(datetime)
  payment type(section)
- amount(currency)
- purity(select)
- weight(float)
- metal rate(10 gram)
