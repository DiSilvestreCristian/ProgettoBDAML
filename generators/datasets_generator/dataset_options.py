NUM_ROWS = 1000000
noise_randomity = 1000
noise = 20
FILENAME = 'datasets/amazon_completo_'+str(NUM_ROWS)+'_'+str(noise)+'_'+str(noise_randomity)+'.csv'
COLUMNS = [
    "Geo.continent",
    "Geo.country",
    "Geo.country_iso2",
    "Geo.country_iso3",
    "Geo.region",
    "Geo.region_iso",
    "Payment.method",
    "Product.category_1",
    "Product.category_2",
    "Product.category_3",
    "Product.category_4",
    "Product.category_5",
    "Product.category_6",
    "Product.category_7",
    "Product.category_8",
    "Shipper.society",
    "Time.day"
]