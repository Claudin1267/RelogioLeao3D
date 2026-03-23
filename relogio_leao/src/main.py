import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Relógio Leão 3D"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#000000"

    relogio = ft.Text(
        value="",
        size=50,
        color="#FFD700",
        weight=ft.FontWeight.BOLD
    )

    def atualizar_relogio(e):
        relogio.value = datetime.datetime.now().strftime("%H:%M:%S")
        page.update()

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src="https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg",
                    width=500,
                    border_radius=20
                ),
                ft.Text("🦁 Relógio Leão 3D", size=24, color="white"),
                relogio,
            ]
        )
    )

    page.timer_interval = 1000
    page.on_timer = atualizar_relogio

ft.run(main)
