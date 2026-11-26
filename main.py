from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from logic import generate

class GeneratorUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.history = []

        self.entry = TextInput(hint_text='Введи число, "пароль" или "пароль 12"', multiline=False)
        self.entry.bind(on_text_validate=self.process_input)
        self.add_widget(self.entry)

        self.btn = Button(text='Выполнить', size_hint_y=None, height=50)
        self.btn.bind(on_press=self.process_input)
        self.add_widget(self.btn)

        self.scroll = ScrollView()
        self.output_label = Label(text='', size_hint_y=None, halign='left', valign='top')
        self.output_label.bind(texture_size=self.output_label.setter('size'))
        self.scroll.add_widget(self.output_label)
        self.add_widget(self.scroll)

    def process_input(self, instance):
        text = self.entry.text.strip()
        if not text:
            return

        result_lines = generate(text)
        result_lines.append("Источник: криптографический генератор Android через Python secrets. Интернет не нужен.")
        self.update_output(result_lines)
        self.entry.text = ''

    def update_output(self, lines):
        self.history.extend(lines)
        self.output_label.text = '\n'.join(self.history)

class GeneratorApp(App):
    def build(self):
        return GeneratorUI()

if __name__ == '__main__':
    GeneratorApp().run()
