from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        old_date = super()._old_fabrication_date(products)
        nearest_date = super()._nearest_expiration_date(products)
        company_more_products = super()._company_with_more_products(products)
        stock_by_company = cls.stock_by_company(products)

        formated_stock_by_company = ""
        for product in stock_by_company:
            for company, quantity in product.items():
                formated_stock_by_company += f"- {company}: {quantity}\n"

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {nearest_date}\n"
            f"Empresa com mais produtos: {company_more_products}\n"
            f"Produtos estocados por empresa:\n {formated_stock_by_company}"
        )

    @classmethod
    def stock_by_company(cls, products):
        company_products = super()._company_by_product(products)
        return [company_products]
