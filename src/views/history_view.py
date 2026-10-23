import flet as ft
from api_service import ApiService

def HistoryView(page: ft.Page):
    appointments = ApiService.get_data("appointments")
    
    app_list = ft.ListView(expand=True, spacing=10, padding=10)
    for app in appointments:
        app_list.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"Patient: {app.get('patient_name', 'N/A')}", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Doctor: {app.get('doctor_name', 'N/A')}"),
                        ft.Text(f"Date & Time: {app.get('date', 'N/A')} at {app.get('time', 'N/A')}"),
                            ft.Text(f"Status: {app.get('status', 'Pending')}", color=ft.Colors.GREEN_700),
                    ]),
                    padding=15
                )
            )
        )

    return ft.View(
        route="/history",
        controls=[
            ft.AppBar(title=ft.Text("Appointment History & Tracking"), bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("All Scheduled Appointments", size=20, weight=ft.FontWeight.BOLD),
                        ft.Button("Back to Dashboard", on_click=lambda _: page.navigate("/"))
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Divider(),
                    app_list
                ], expand=True),
                padding=20
            )
        ]
    )