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
        "dimension" : "Product.category1",
        "noise" : noise
    },
    {
        "dimension" : "Product.category2",
        "noise" : noise
    },
    {
        "dimension" : "Product.category3",
        "noise" : noise
    },
    {
        "dimension" : "Product.category4",
        "noise" : noise
    },
    {
        "dimension" : "Product.category5",
        "noise" : noise
    },
    {
        "dimension" : "Product.category6",
        "noise" : noise
    },
    {
        "dimension" : "Product.category7",
        "noise" : noise
    },
    {
        "dimension" : "Product.category8",
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