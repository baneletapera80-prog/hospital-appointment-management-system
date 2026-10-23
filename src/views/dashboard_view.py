import flet as ft
from api_service import ApiService

def DashboardView(page: ft.Page):
    appointments = ApiService.get_data("appointments")
    patients = ApiService.get_data("patients")
    doctors = ApiService.get_data("doctors")

    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Hospital Management Dashboard"), bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE),
            ft.Container(
                content=ft.Column([
                    ft.Text("CareSync Hospital Portal", size=24, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Row([
                        ft.Card(content=ft.Container(content=ft.Column([
                            ft.Text("Total Patients", weight=ft.FontWeight.BOLD),
                            ft.Text(str(len(patients)), size=20, color=ft.Colors.BLUE_600)
                        ]), padding=20)),
                        ft.Card(content=ft.Container(content=ft.Column([
                            ft.Text("Available Doctors", weight=ft.FontWeight.BOLD),
                                ft.Text(str(len(doctors)), size=20, color=ft.Colors.TEAL_600)
                        ]), padding=20)),
                        ft.Card(content=ft.Container(content=ft.Column([
                            ft.Text("Appointments", weight=ft.FontWeight.BOLD),
                                ft.Text(str(len(appointments)), size=20, color=ft.Colors.ORANGE_600)
                        ]), padding=20)),
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Container(height=30),
                    ft.Row([
                        ft.Button("Book Appointment", icon=ft.Icons.ADD, on_click=lambda _: page.navigate("/booking")),
                        ft.Button("View Patients", icon=ft.Icons.PERSON, on_click=lambda _: page.navigate("/patients")),
                        ft.Button("Appointment History", icon=ft.Icons.HISTORY, on_click=lambda _: page.navigate("/history")),
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                ], alignment=ft.MainAxisAlignment.CENTER),
                padding=30
            )
        ]
    )