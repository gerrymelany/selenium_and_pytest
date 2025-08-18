import pytest



def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_dynamic_button()
    elemento_texto_oculto = sandbox_page.wait_for_element(sandbox_page.hidden_text_label)
    texto_esperado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"

    assert texto_esperado in elemento_texto_oculto.text, f"El texto esperado '{texto_esperado}' no se encontró en el elemento oculto."


def test_boton_id_dinamico_cambia_color_al_hacer_hover(sandbox_page):
    sandbox_page.navigate_sandbox()
    boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.dynamic_id_button_locator)
    color_before_hover = boton_id_dinamico.value_of_css_property("background-color")
    sandbox_page.hover_over_element(sandbox_page.dynamic_id_button_locator)
    color_after_hover = boton_id_dinamico.value_of_css_property("background-color")

    assert color_before_hover != color_after_hover, "El color del botón no cambió al hacer hover."

@pytest.mark.sandbox
def test_checkbox_seleccionable_pizza(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox("Pizza")

@pytest.mark.sandbox
def test_checkbox_seleccionable_pizza(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox("Helado")

@pytest.mark.sandbox
def test_elegir_radio_buttion_si(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_radio_button("Si")

@pytest.mark.sandbox
def test_elegir_deporte_del_dropdown(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_deporte("Fútbol")

@pytest.mark.sandbox
def test_deporte_dropdown_options(sandbox_page):
    sandbox_page.navigate_sandbox()
    options = sandbox_page.get_deporte_dropdown_options()
    expected_options = ["Seleccioná un deporte", "Fútbol","Tennis", "Basketball"]

    assert all(
        option in options for option in expected_options
    ), "No todas las opciones esperadas están presentes en el dropdown de deportes."

@pytest.mark.sandbox
def test_popup_title(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_button_popup()
    popup_title = sandbox_page.get_popup_title_text()
    expected_title = "Popup de ejemplo"

    assert popup_title == expected_title, f"El título del popup esperado '{expected_title}' no coincide con '{popup_title}'."

@pytest.mark.sandbox
def test_valor_celda_cambia_post_recarga(sandbox_page):
    sandbox_page.navigate_sandbox()
    valor_inicial = sandbox_page.get_cell_value(2, 3)  # Asumiendo que fila=2 y columna=3
    sandbox_page.reload_page()
    valor_post_recarga = sandbox_page.get_cell_value(2, 3)  # Asumiendo que fila=2 y columna=3

    assert valor_inicial != valor_post_recarga, f"El valor de la celda no cambió después de recargar la página aún es: {valor_inicial}"

@pytest.mark.sandbox
def test_valor_celda_estatica(sandbox_page):
    sandbox_page.navigate_sandbox()
    valor_inicial = sandbox_page.get_valor_celda_estatica(2, 3)  # Asumiendo que fila=2 y columna=3
    sandbox_page.reload_page()
    valor_post_recarga = sandbox_page.get_valor_celda_estatica(2, 3)  # Asumiendo que fila=2 y columna=3

    assert valor_inicial == valor_post_recarga, f"El valor de la celda no es estático, el valor inicial es: {valor_inicial} y el valor post recarga es: {valor_post_recarga}"
