from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, products):
        old_date = cls.__old_fabrication_date(products)
        nearest_date = cls.__nearest_expiration_date(products)
        company_with_more_products = cls.__company_with_more_products(products)

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {nearest_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    def __old_fabrication_date(products):
        fabrication_dates = [date.fromisoformat(product["data_de_fabricacao"])
                             for product in products]

        return min(fabrication_dates)

    def __nearest_expiration_date(products):
        expiration_dates = [date.fromisoformat(product["data_de_validade"])
                            for product in products
                            if date.fromisoformat(product["data_de_validade"])
                            > date.today()]

        return min(expiration_dates)

    def __company_with_more_products(products):
        company_products = {}

        for product in products:
            if product["nome_da_empresa"] not in company_products:
                company_products[product["nome_da_empresa"]] = 1
            else:
                company_products[product["nome_da_empresa"]] += 1

        return max(company_products, key=company_products.get)
