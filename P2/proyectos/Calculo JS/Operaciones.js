function calcular() {
    var numero1 = document.getElementById("numero1").value;
    var numero2 = document.getElementById("numero2").value;
    var operacion = document.getElementById("operacion").value;

    // Verifica si los números son válidos
    if (isNaN(numero1) || isNaN(numero2) || numero1 === "" || numero2 === "") {
        alert("Por favor, ingresa números válidos en ambos campos.");
        return; // Sale de la función si los valores no son válidos
    }

    // Convierte las entradas a números
    var n1 = parseFloat(numero1);
    var n2 = parseFloat(numero2);
    var resultado;
    var simbolo;

    // Realiza la operación seleccionada
    switch (operacion) {
        case "sumar":
            resultado = n1 + n2;
            simbolo = "+";
            break;
        case "restar":
            resultado = n1 - n2;
            simbolo = "-";
            break;
        case "multiplicar":
            resultado = n1 * n2;
            simbolo = "*";
            break;
        case "dividir":
            if (n2 === 0) {
                alert("Error: No se puede dividir entre cero.");
                return; // Sale de la función si hay intento de dividir entre cero
            }
            resultado = n1 / n2;
            simbolo = "/";
            break;
        default:
            alert("Operación no válida.");
            return; // Sale de la función si la operación no es válida
    }

    // Muestra el resultado
    document.getElementById("resultado").innerHTML = "<strong>" + n1 + " " + simbolo + " " + n2 + " = " + resultado + "</strong>";
}
