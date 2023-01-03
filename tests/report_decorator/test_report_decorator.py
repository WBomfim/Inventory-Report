from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport


def mock_product_list():
    return [
        {
            "id": 1,
            "nome_do_produto": "Produto 1",
            "nome_da_empresa": "Empresa 1",
            "data_de_fabricacao": "2021-01-01",
            "data_de_validade": "2024-01-01",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "Armazenar em local seco",
        }
    ]


def expected_report():
    product_fake = mock_product_list()[0]
    return (
        f"\033[32m{'Data de fabricação mais antiga:'}\033[0m"
        + f" \033[36m{product_fake['data_de_fabricacao']}\033[0m\n"

        f"\033[32m{'Data de validade mais próxima:'}\033[0m"
        + f" \033[36m{product_fake['data_de_validade']}\033[0m\n"

        f"\033[32m{'Empresa com mais produtos:'}\033[0m"
        + f" \033[31m{product_fake['nome_da_empresa']}\033[0m\n"

        "Produtos estocados por empresa:\n"
        F"- {product_fake['nome_da_empresa']}: 1\n"
    )


def test_decorar_relatorio():
    report = ColoredReport(CompleteReport)
    assert report.generate(mock_product_list()) == expected_report()
