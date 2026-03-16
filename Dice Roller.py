import flet as ft
import random

def main(page: ft.Page):

    page.title = "Dice Roller"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50

    def rollDice(e):
        diceRow.controls.clear()

        howMany = int(diceDropdown.value)
        results = []

        for i in range(howMany):
            number = random.randint(1, 6)
            results.append(number)

            diceRow.controls.append(
                ft.Image(
                    src=f"dice/dice_{number}.png",
                    width=80,
                    height=80
                )
            )

        resultText.value = "Result: " + str(results)
        historyColumn.controls.append(ft.Text(str(results)))

        page.update()

    def resetDice(e):
        diceRow.controls.clear()
        resultText.value = "Result: -"
        historyColumn.controls.clear()
        page.update()

    diceDropdown = ft.Dropdown(
        label="How many dice?",
        value="2",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
        ],
        width=200
    )

    rollButton = ft.Button(content="Roll Dice", on_click=rollDice)
    resetButton = ft.Button(content="Reset", on_click=resetDice)

    diceRow = ft.Row(spacing=10)

    resultText = ft.Text("Result: -", size=18)
    historyTitle = ft.Text("History:", size=16)
    historyColumn = ft.Column()

    page.add(
        diceDropdown,
        rollButton,
        resetButton,
        diceRow,
        resultText,
        historyTitle,
        historyColumn
    )

ft.run(main=main, assets_dir="assets")