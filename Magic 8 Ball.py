import flet as ft
import random

def main(page: ft.Page):
    
    def askClick(e):
        question = questionInput.value.strip()

        if question == "":
            questionShow.value = "Your question: "
            resultText.value = "Type a yes or no question first :)"
            resultText.color = ft.Colors.GREY
            imagen.src = "images.magic8ball/question.png"
            page.update()
            return

        answers = [
            ("Yes", ft.Colors.GREEN, "images.magic8ball/yes.png"),
            ("Very likely", ft.Colors.GREEN, "images.magic8ball/yes.png"),
            ("Chances are good", ft.Colors.GREEN, "images.magic8ball/yes.png"),

            ("No", ft.Colors.RED, "images.magic8ball/no.png"),
            ("Very unlikely", ft.Colors.RED, "images.magic8ball/no.png"),
            ("Do not count on it", ft.Colors.RED, "images.magic8ball/no.png"),

            ("Maybe", ft.Colors.PINK, "images.magic8ball/maybe.png"),
            ("It is possible", ft.Colors.PINK, "images.magic8ball/maybe.png"),
            ("I am not sure", ft.Colors.PINK, "images.magic8ball/maybe.png"),

            ("Ask again later", ft.Colors.BLUE, "images.magic8ball/later.png"),
            ("Try again later", ft.Colors.BLUE, "images.magic8ball/later.png"),
            ("Cannot predict now", ft.Colors.BLUE, "images.magic8ball/later.png")
        ]

        chosen = random.choice(answers)

        answerMessage = chosen[0]
        answerColor = chosen[1]
        answerImage = chosen[2]

        questionShow.value = "Your question: " + question
        resultText.value = "Magic 8 Ball says: " + answerMessage
        resultText.color = answerColor
        imagen.src = answerImage

        page.update()

    def clearClick(e):
        questionInput.value = ""
        questionShow.value = "Your question: "
        resultText.value = "Magic 8 Ball says: "
        resultText.color = ft.Colors.WHITE
        imagen.src = "images.magic8ball/question.png"
        page.update()

    page.title = "Magic 8 Ball"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    titleText = ft.Text(value="Magic 8 Ball", size=30, weight=ft.FontWeight.BOLD)

    questionText = ft.Text(
        value="Type a yes or no question, then click the button :)",
        size=16
    )

    questionInput = ft.TextField(width=420, label="Your question")

    askButton = ft.Button(
        content=ft.Text("Ask the 8-Ball", size=15),
        width=220,
        height=60,
        on_click=askClick
    )

    clearButton = ft.Button(
        content=ft.Text("Clear", size=15),
        width=140,
        height=60,
        on_click=clearClick
    )

    buttonsRow = ft.Row(
        controls=[askButton, clearButton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    questionShow = ft.Text(value="Your question: ", size=16)

    resultText = ft.Text(
        value="Magic 8 Ball says: ",
        size=20,
        weight=ft.FontWeight.BOLD
    )

    imagen = ft.Image(
        src="images.magic8ball/question.png",
        width=400,
        height=400
    )

    page.add(
        titleText,
        questionText,
        questionInput,
        buttonsRow,
        questionShow,
        resultText,
        imagen
    )

ft.run(main=main, assets_dir="assets")