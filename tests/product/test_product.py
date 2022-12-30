from inventory_report.inventory.product import Product
from tests.product.mocks import MockProduct


def test_cria_produto():
    mock_product = MockProduct()
    new_product = Product(
        mock_product.id,
        mock_product.nome_do_produto,
        mock_product.nome_da_empresa,
        mock_product.data_de_fabricacao,
        mock_product.data_de_validade,
        mock_product.numero_de_serie,
        mock_product.instrucoes_de_armazenamento,
    )

    assert new_product.id == mock_product.id
    assert new_product.nome_do_produto == mock_product.nome_do_produto
    assert new_product.nome_da_empresa == mock_product.nome_da_empresa
    assert new_product.data_de_fabricacao == mock_product.data_de_fabricacao
    assert new_product.data_de_validade == mock_product.data_de_validade
    assert new_product.numero_de_serie == mock_product.numero_de_serie
    assert new_product.instrucoes_de_armazenamento == (
        mock_product.instrucoes_de_armazenamento
    )
