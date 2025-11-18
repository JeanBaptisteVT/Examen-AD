#   https://dodona.be/nl/activities/1780297260/

class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
    def __str__(self):

        return f'Batch(quantity =[{self.quantity}], cost_per_unit=[{self.cost_per_unit}])'



class Product:
    def __init__(self, product_name, holding_cost, stockout_penalty):
        self.product_name = product_name
        # We gebruiken een list als stack: laatste element is de "bovenste" batch
        self.batches = []
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty

    def add_batch(self, quantity, cost_per_unit):
        """Voegt een nieuwe batch bovenop de stack toe (LIFO)."""
        new_batch = Batch(quantity, cost_per_unit)
        self.batches.append(new_batch)

    def fulfill_demand(self, demand):
        """
        Probeert de vraag te vervullen volgens LIFO.
        Retourneert 0 als alles geleverd kan worden.
        Indien niet, return stockout_penalty * (niet geleverde hoeveelheid).
        """
        remaining_demand = demand

        # Zolang er vraag is én batches zijn, gebruiken we de bovenste batch (LIFO)
        while remaining_demand > 0 and self.batches:
            top_batch = self.batches[-1]  # bovenste batch

            if top_batch.quantity > remaining_demand:
                # Batch heeft genoeg om de vraag te dekken
                top_batch.quantity -= remaining_demand
                remaining_demand = 0
            else:
                # Batch is niet genoeg: gebruik alles en verwijder batch
                remaining_demand -= top_batch.quantity
                top_batch.quantity = 0
                self.batches.pop()

        # Als er niets meer overblijft van de vraag, geen penalty
        if remaining_demand <= 0:
            return 0

        # Niet alles kon geleverd worden → stockout penalty
        return remaining_demand * self.stockout_penalty

    def calculate_holding_cost(self):
        """
        Totale aanhoudingskost = holding_cost * aantal eenheden in voorraad
        (opgeteld over alle batches).
        """
        total_units = sum(batch.quantity for batch in self.batches)
        return total_units * self.holding_cost

    def __str__(self):
        # Startstring
        result = f"Product [{self.product_name}]:\n"

        # Voor elke batch lijnen toevoegen
        for batch in self.batches:
            result += f"Batch(quantity=[{batch.quantity}], cost_per_unit=[{batch.cost_per_unit}])\n"

        return result
