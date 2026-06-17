# Calculadora de Daño MH

Aplicación en Python con Flask para calcular el daño aproximado de una build de Monster Hunter a partir de un arma y un conjunto de habilidades.

## Archivos principales

- `app.py`: levanta la aplicación Flask y procesa el formulario.
- `mh_damage/calculator/`: contiene la lógica de armas, skills, builds y cálculo de daño.
- `mh_damage/static_data/`: define datos fijos como armas, skills y modificadores.
- `templates/`: vistas HTML del formulario y del resultado.
- `tests/`: pruebas de regresión del cálculo.

## Estructura de carpetas

```text
calculadora_daño_mh/
├── app.py
├── README.md
├── mh_damage/
│   ├── __init__.py
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── build.py
│   │   ├── build_factory.py
│   │   ├── damage.py
│   │   ├── skill.py
│   │   ├── skill_engine.py
│   │   ├── statistics.py
│   │   └── weapon.py
│   └── static_data/
│       ├── __init__.py
│       ├── modifiers.py
│       ├── skills.py
│       ├── stats.py
│       └── weapons.py
├── templates/
│   ├── build_form.html
│   └── build_result.html
└── tests/
	└── test_damage.py
```

## Clases principales

- `Statistics`: agrupa las estadísticas del arma.
- `Weapon`: representa el arma base y permite aplicar cambios.
- `Skill`: representa una habilidad y sus efectos.
- `SkillEngine`: combina efectos de varias skills.
- `BuildFactory`: crea una build a partir de un arma y skills.
- `Build`: genera la versión final del arma con las skills aplicadas.
- `Damage`: calcula el daño total de la build.

## Instalación

Requisitos:

- Python 3.9 o superior
- Flask

Instala la dependencia desde la raíz del proyecto:

```bash
pip install flask
```

## Ejecución

Desde la raíz del proyecto ejecuta:

```bash
python app.py
```

Después abre esta URL en el navegador:

```text
http://127.0.0.1:5000/build_calculator
```

## Cómo se usa

1. Selecciona el tipo de arma.
2. Introduce ataque, elemento y afinidad.
3. Marca las skills que quieras usar y elige su nivel.
4. Pulsa en `Calcular daño`.
5. La aplicación mostrará el daño calculado.

## Notas

- La interfaz web está pensada como una capa simple sobre la lógica de cálculo.
- Los efectos de skills y tipos de arma disponibles se editan en `mh_damage/static_data/`.
- El cálculo usa parámetros fijos definidos actualmente en `app.py`.