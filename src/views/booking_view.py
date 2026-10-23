import flet as ft
from api_service import ApiService

def BookingView(page: ft.Page):
    patient_name_input = ft.TextField(label="Patient Name", width=300)
    
    # Fetch available doctors from MockAPI for the dropdown
    doctors = ApiService.get_data("doctors")
    doctor_options = [
        ft.dropdown.Option(f"{doc.get('name')} - {doc.get('specialization', 'General')}") 
        for doc in doctors
    ]
    
    if not doctor_options:
        doctor_options = [ft.dropdown.Option("Dr. John Smith - Cardiology")]

    doctor_dropdown = ft.Dropdown(
        label="Select Available Doctor",
        width=300,
        options=doctor_options
    )
    
    date_input = ft.TextField(label="Date (YYYY-MM-DD)", width=300)
    time_input = ft.TextField(label="Time (e.g., 10:00 AM)", width=300)
    status_text = ft.Text("", color=ft.Colors.GREEN_700)

    def submit_appointment(e):
        if not patient_name_input.value or not doctor_dropdown.value:
            status_text.value = "Please enter patient name and select a doctor!"
            status_text.color = ft.Colors.RED_700
            page.update()
            return

        new_appointment = {
            "patient_name": patient_name_input.value,
            "doctor_name": doctor_dropdown.value,
            "date": date_input.value,
            "time": time_input.value,
            "status": "Confirmed"
        }

        success = ApiService.post_data("appointments", new_appointment)
        if success:
            status_text.value = "Appointment booked successfully!"
            status_text.color = ft.Colors.GREEN_700
            patient_name_input.value = ""
            doctor_dropdown.value = None
            date_input.value = ""
            time_input.value = ""
        else:
            status_text.value = "Failed to book appointment. Try again."
            status_text.color = ft.Colors.RED_700
        page.update()

    return ft.View(
        route="/booking",
        controls=[
            ft.AppBar(title=ft.Text("Book Appointment"), bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE),
            ft.Container(
                content=ft.Column([
                    ft.Text("New Appointment Booking", size=20, weight=ft.FontWeight.BOLD),
                    patient_name_input,
                    doctor_dropdown,
                    date_input,
                    time_input,
                    ft.Button("Submit Booking", bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE, on_click=submit_appointment),
                    status_text,
                    ft.TextButton("Back to Dashboard", on_click=lambda _: page.navigate("/"))
                ], spacing=15, alignment=ft.MainAxisAlignment.CENTER),
                padding=30
            )
        ]
    )