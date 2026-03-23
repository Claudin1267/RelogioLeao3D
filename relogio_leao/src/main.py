import flet as ft
import datetime
import asyncio
import math

def main(page: ft.Page):
    page.title = "Relógio Leão 3D"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0a0a0a"
    page.padding = 0

    relogio = ft.Text(
        value="00:00:00",
        size=52,
        color="#FFD700",
        weight=ft.FontWeight.BOLD,
        font_family="Courier New",
    )

    data = ft.Text(
        value="",
        size=14,
        color="#B8860B",
        weight=ft.FontWeight.W_500,
    )

    status = ft.Text(
        value="⚙ SISTEMA ATIVO ⚙",
        size=12,
        color="#00FF41",
    )

    def atualizar(e):
        agora = datetime.datetime.now()
        relogio.value = agora.strftime("%H:%M:%S")
        data.value = agora.strftime("%A, %d/%m/%Y").upper()
        page.update()

    page.add(
        ft.Container(
            width=400,
            height=800,
            bgcolor="#0a0a0a",
            border=ft.border.all(2, "#FFD700"),
            border_radius=20,
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    # Topo futurístico
                    ft.Text("◈ LEÃO 3D SYSTEM ◈", size=13, color="#FFD700"),
                    ft.Divider(color="#FFD700", thickness=1),

                    # Leão realista
                    ft.Container(
                        content=ft.Image(
                            src="https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg",
                            width=280,
                            height=220,
                            fit=ft.ImageFit.COVER,
                            border_radius=15,
                        ),
                        border=ft.border.all(3, "#FFD700"),
                        border_radius=15,
                        shadow=ft.BoxShadow(
                            blur_radius=30,
                            color="#FFD70088",
                            offset=ft.Offset(0, 0),
                        )
                    ),

                    ft.Divider(color="#333333", thickness=1),

                    # Engrenagens decorativas
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("⚙", size=30, color="#FFD700"),
                            ft.Text("⚙", size=20, color="#B8860B"),
                            ft.Text("⚙", size=35, color="#FFD700"),
                            ft.Text("⚙", size=20, color="#B8860B"),
                            ft.Text("⚙", size=30, color="#FFD700"),
                        ]
                    ),

                    # Relógio principal
                    ft.Container(
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                ft.Text("[ HORA DO LEÃO ]", size=11, color="#555555"),
                                relogio,
                                data,
                            ]
                        ),
                        bgcolor="#111111",
                        border=ft.border.all(1, "#FFD700"),
                        border_radius=10,
                        padding=15,
                        width=300,
                    ),

                    ft.Divider(color="#333333", thickness=1),

                    # Barras de status futurísticas
                    ft.Column(
                        spacing=5,
                        controls=[
                            ft.Row([
                                ft.Text("PODER", size=10, color="#FFD700", width=60),
                                ft.ProgressBar(value=0.95, color="#FFD700", bgcolor="#222222", width=200),
                            ]),
                            ft.Row([
                                ft.Text("FORÇA", size=10, color="#FF6600", width=60),
                                ft.ProgressBar(value=0.88, color="#FF6600", bgcolor="#222222", width=200),
                            ]),
                            ft.Row([
                                ft.Text("SISTEMA", size=10, color="#00FF41", width=60),
                                ft.ProgressBar(value=1.0, color="#00FF41", bgcolor="#222222", width=200),
                            ]),
                        ]
                    ),

                    ft.Divider(color="#FFD700", thickness=1),
                    status,
                ]
            )
        )
    )

    page.run_task(ticker, atualizar)

async def ticker(callback):
    while True:
        await asyncio.sleep(1)
        callback(None)

ft.app(target=main)