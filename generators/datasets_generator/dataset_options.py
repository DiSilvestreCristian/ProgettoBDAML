NUM_ROWS = 100000
FILENAME = 'datasets/amazon_completo.csv'
noise = 20
COLUMNS = [
    {
        "dimension" : "Geo.continent",
        "noise" : noise
    },
    {
        "dimension" : "Geo.country",
        "noise" : noise
    },
    {
        "dimension" : "Geo.country_iso2",
        "noise" : noise
    },
    {
        "dimension" : "Geo.country_iso3",
        "noise" : noise
    },
    {
        "dimension" : "Geo.region",
        "noise" : noise
    },
    {
        "dimension" : "Geo.region_iso",
        "noise" : noise
    },
    {
        "dimension" : "Payment.method",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_1",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_2",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_3",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_4",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_5",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_6",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_7",
        "noise" : noise
    },
    {
        "dimension" : "Product.category_8",
        "noise" : noise
    },
    {
        "dimension" : "Shipper.society",
        "noise" : noise
    },
    {
        "dimension" : "Time.day",
        "noise" : noise
    }
]