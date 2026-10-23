import flet as ft
from api_service import ApiService

def PatientsView(page: ft.Page):
    patients = ApiService.get_data("patients")
    appointments = ApiService.get_data("appointments")
    
    patient_list = ft.ListView(expand=True, spacing=10, padding=10)
    
    for pat in patients:
        pat_name = pat.get('name', 'Unknown')
        
        # Match appointments belonging to this patient
        pat_appointments = [
            app for app in appointments 
            if app.get('patient_name', '').strip().lower() == pat_name.strip().lower()
        ]
        
        if pat_appointments:
            booking_details = "\n".join([
                f"• {app.get('doctor_name')} | Date: {app.get('date')} ({app.get('time')}) - [{app.get('status', 'Confirmed')}]"
                for app in pat_appointments
            ])
            booking_status = ft.Text(f"Bookings:\n{booking_details}", color=ft.Colors.GREEN_700, size=13)
        else:
            booking_status = ft.Text("No active appointments booked.", color=ft.Colors.GREY_500, size=13, italic=True)

        patient_list.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.PERSON, color=ft.Colors.RED_700),
                            title=ft.Text(pat_name, weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text(f"Phone: {pat.get('phone', 'N/A')} | Email: {pat.get('email', 'N/A')} | Age: {pat.get('age', 'N/A')}"),
                        ),
                        ft.Divider(height=1),
                        ft.Container(content=booking_status, padding=ft.Padding.only(left=16, bottom=10, right=16))
                    ]),
                    padding=10
                )
            )
        )

    return ft.View(
        route="/patients",
        controls=[
            ft.AppBar(title=ft.Text("Patient Directory & Bookings"), bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Registered Patients & Appointment Status", size=20, weight=ft.FontWeight.BOLD),
                        ft.Button("Back to Dashboard", on_click=lambda _: page.navigate("/"))
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Divider(),
                    patient_list
                ], expand=True),
                padding=20
            )
        ]
    )