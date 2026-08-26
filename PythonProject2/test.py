from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


# Define the main app interface using KV language
KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: "10dp"
    spacing: "10dp"

    MDTextField:
        id: user_input
        hint_text: "Enter text here"
        size_hint: None, None
        size: "280dp", "50dp"
        pos_hint: {"center_x": 0.5}

    MDRaisedButton:
        text: "Change Label Text"
        size_hint: None, None
        size: "200dp", "50dp"
        pos_hint: {"center_x": 0.5}
        on_press: app.change_label_text()

    MDLabel:
        id: output_label
        text: "This is a label"
        halign: "center"
        theme_text_color: "Secondary"
        font_style: "H5"
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_label_text(self):
        user_input_text = self.root.ids.user_input.text
        self.root.ids.output_label.text = f"You entered: {user_input_text}"


if __name__ == "__main__":
    MyApp().run()
