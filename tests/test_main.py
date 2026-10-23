import flet.testing as ftt


async def test_home_view_is_shown(flet_app: ftt.FletTestApp):
    tester = flet_app.tester

    await tester.pump_and_settle()

    assert (await tester.find_by_text("Welcome to the Greeting App")).count == 1
