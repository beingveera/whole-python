from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp

spinner = Spinner(
    text='Home',
    values=('Home', 'Work', 'Other', 'Custom'),
    size_hint=(None, None), size=(200, 144),
    pos_hint={'center_x': .5, 'center_y': .5})


def show_selected_value(spinner, text):
    print('The spinner', spinner, 'have text', text)


spinner.bind(text=show_selected_value)

runTouchApp(spinner)
