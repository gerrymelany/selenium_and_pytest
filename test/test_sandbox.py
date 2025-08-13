import pytest


@pytest.mark.sandbox
def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_dynamic_button()

    elemento_texto_oculto = sandbox_page.wait_for_element(sandbox_page.hidden_text_label)

    texto_experado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"

    assert texto_experado in elemento_texto_oculto.text, f"El texto esperado '{texto_experado}' no se encontró en el elemento oculto."

def test_boton_id_dinamico_cambia_color_al_hacer_hover(sandbox_page):
    sandbox_page.navigate_sandbox()
    boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.dynamic_id_button_locator)
    color_before_hover = boton_id_dinamico.value_of_css_property("background-color")
    sandbox_page.hover_over_element(sandbox_page.dynamic_id_button_locator)
    color_after_hover = boton_id_dinamico.value_of_css_property("background-color")
    assert color_before_hover != color_after_hover, "El color del botón no cambió al hacer hover."
