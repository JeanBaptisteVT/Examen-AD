import random
import csv
from Code_lectures_2526.examens.examenvorigjaar import Product


class Inventory_Manager:
    def __init__(self):
        # product_name -> Product object
        self.products = {}

    def add_product(self, product_name, holding_cost, stockout_penalty):
        """Voegt een nieuw product toe als het nog niet bestaat."""
        if product_name in self.products:
            print(f"Product {product_name} already exists.")
        else:
            self.products[product_name] = Product(
                product_name, holding_cost, stockout_penalty
            )

    def restock_product(self, product_name, quantity, cost_per_unit):
        """Voegt een batch toe aan een bestaand product."""
        product = self.products.get(product_name)
        if product is None:
            print(f"Product {product_name} not found")
        else:
            product.add_batch(quantity, cost_per_unit)

    def simulate_demand(self, min_demand=0, max_demand=20):
        """
        Genereert een willekeurige vraag voor elk product.
        Returnt een dict: {product_name: vraag}
        """
        demand = {}
        for name in self.products:
            demand[name] = random.randint(min_demand, max_demand)
        return demand

    def simulate_day(self, demand):
        """
        Simuleert een dag.
        demand: dict {product_name: gevraagde hoeveelheid}
        Returnt (totale_holding_cost, totale_stockout_cost).
        """
        total_stockout_cost = 0

        # Eerst vraag proberen te leveren
        for name, qty in demand.items():
            product = self.products.get(name)
            if product is not None:
                total_stockout_cost += product.fulfill_demand(qty)

        # Daarna holding cost op nieuwe voorraad
        total_holding_cost = sum(
            product.calculate_holding_cost()
            for product in self.products.values()
        )

        return total_holding_cost, total_stockout_cost

    def save_to_csv(self, filename):
        """
        Slaat voorraad op als:
        product_name,batch_quantity,batch_cost_per_unit
        """
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            for name, product in self.products.items():
                for batch in product.batches:
                    writer.writerow([name, batch.quantity, batch.cost_per_unit])

    def load_from_csv(self, filename):
        """
        Laadt voorraad terug in.
        Als een product nog niet bestaat, maken we het aan met
        holding_cost=0 en stockout_penalty=0 (aannames).
        """
        with open(filename, mode="r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                product_name, quantity, cost_per_unit = row
                quantity = int(quantity)
                cost_per_unit = float(cost_per_unit)

                if product_name not in self.products:
                    self.products[product_name] = Product(
                        product_name, holding_cost=0, stockout_penalty=0
                    )

                self.products[product_name].add_batch(quantity, cost_per_unit)

    def print_inventory(self):
        print("Current Inventory:")
        for product in self.products.values():
            print(product)
            print()  # lege lijn tussen producten
