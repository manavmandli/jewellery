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

4. Supplier Payment Tracker

- Supplier(link - supplier)
- created on(date time)
- last updated on(data time)
- Pending amount (currency)
- pending fine(float)

5. Supplier Bill Payment

basic details(section)

- Supplier(link - supplier)
- payment date(datetime)
  payment type(section)
- amount(currency)
- purity(select)
- weight(float)
- metal rate(10 gram)
