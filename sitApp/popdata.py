import csv
from models import Product

def populate_products_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Product.objects.create(
                product_id=row['product_id'],
                merchant_id=row['merchant_id'],
                product_name=row['name'],
                preferred=row['Preferred'],
                mall=row['Mall'],
                avg_rating=row['avg_rating'],
                total_rating=row['total_rating'],
                total_sold=row['total_sold'],
                price=row['price'],
                fav_count=row['fav_count'],
                qty_avail=row['qty_avail'],
                description=row['description'],
                img_src=row['img_source'],
            )

if __name__ == '__main__':
    csv_file_path = 'C:/Users/limji/gitlocal/SitShop/sitApp/etlProduct.csv'  # Provide the correct path to your CSV file
    populate_products_from_csv(csv_file_path)