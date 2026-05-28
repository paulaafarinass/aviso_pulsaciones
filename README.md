 # Monitor de Frecuencia Cardíaca y Detección de Anomalías 🫀

Este proyecto es una simulación en Python de un sistema de monitorización cardíaca para dispositivos portables (wearables, como relojes inteligentes). Su objetivo es detectar eventos cardíacos anómalos (como paradas cardíacas o ritmos irregulares) y emitir alertas, filtrando posibles falsos positivos generados por la actividad física del usuario.

## ⚙️ Lógica y Simulación de Hardware

Dado que el código está diseñado para probar la lógica de evaluación médica sin necesidad de hardware físico, el sistema simula la integración de dos sensores principales:

1. **Sensor de Movimiento (Acelerómetro):** Un sensor que devuelve un valor digital (`1` o `0`) para indicar la existencia o ausencia de movimiento en el momento de la lectura. Si hay movimiento durante un ritmo cardíaco alterado, el sistema lo interpreta como un esfuerzo físico normal (falso positivo) y omite la alerta médica.

2. **Sensor de Pulso (Fotopletismografía - PPG):** Un sensor óptico que detecta las pulsaciones. En un entorno físico, el sistema guardaría cada latido en una variable contador que se estaría incrementando continuamente durante un intervalo exacto de 60 segundos. Al finalizar este intervalo de tiempo, el dato final se guarda en la variable `pulsaciones` (representando los Latidos Por Minuto o BPM) y el contador se reinicia a `0` para el siguiente ciclo.

## 🚀 Características del Código

- **Prevención de Falsos Positivos:** Implementación de lógica condicional que cruza los datos de frecuencia cardíaca con los datos de movimiento.
- **Manejo de Excepciones:** Uso de bloques `try-except` para garantizar que las entradas manuales durante la simulación sean estrictamente valores numéricos (enteros o booleanos).
- **Ejecución en Bucle:** El sistema se mantiene monitorizando "en tiempo real" hasta que el usuario (o el sistema médico) decida detener la simulación.

