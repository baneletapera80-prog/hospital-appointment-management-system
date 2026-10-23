import flet as ft
from views.dashboard_view import DashboardView
from views.booking_view import BookingView
from views.patients_view import PatientsView
from views.history_view import HistoryView

def main(page: ft.Page):
    page.title = "Hospital Appointment Management System"
    
    #theme
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.RED_700,
            secondary=ft.Colors.GREY_800,
        )
    )

    def route_change(route):
        page.views.clear()
        
        if page.route == "/" or page.route == "/dashboard":
            page.views.append(DashboardView(page))
        elif page.route == "/booking":
            page.views.append(BookingView(page))
        elif page.route == "/patients":
            page.views.append(PatientsView(page))
        elif page.route == "/history":
            page.views.append(HistoryView(page))
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.navigate(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change(page.route or "/")

ft.run(main)