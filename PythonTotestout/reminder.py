# from kivy.metrics import dp
# from kivy.tools.report import title
# from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.button import MDRaisedButton, MDFlatButton
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.label import MDLabel
# from kivymd.uix.list import OneLineListItem
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.snackbar import Snackbar
# from kivy.clock import Clock
# from datetime import datetime,timedelta
#
# from kivymd.uix.textfield import MDTextField
#
#
# class RemindersScreen(MDScreen):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#
#         self.reminders = [] #Each item will be(Title, Datetime,Alerted)
#         self.notified = set() #Keep track of which reminders have been notified
#
#         layout = MDBoxLayout(
#             orientation = "vertical",
#             padding=dp(20),
#             spacing=dp(10)
#         )
#
#         header = MDLabel(
#             text = "Set Reminders",
#             halign = "center",
#             font_style = "H5"
#         )
#         layout.add_widget(header)
#
#         #Reminder list container
#         self.list_container = MDBoxLayout(
#             orientation = "vertical",
#             spacing = dp(5)
#         )
#         layout.add_widget(self.list_container)
#
#         #Buttons
#         btn_box = MDBoxLayout(
#             size_hint_y = None,
#             height = dp(50),
#             spacing = dp(10)
#         )
#         add_btn = MDRaisedButton(
#             text = " Add Reminder", on_release = self.add_reminder_dialog)
#         back_btn = MDFlatButton(
#             text = "Back", on_release = self.go_back)
#         btn_box.add_widget(back_btn)
#         btn_box.add_widget(add_btn)
#         layout.add_widget(btn_box)
#
#         self.add_widget(layout)
#
#         #Schedule notification check every minute
#     def add_reminder_dialog(self, *args):
#         self.dialog = MDDialog(
#             title = "New Reminder",
#             type = "customs",
#             content_cls = MDBoxLayout(
#                 MDTextField(
#                     hint_text = "Reminder Title",
#                     id = "title"),
#                 MDTextField(
#                     hint_text = "Date & Time (YYYY-MM-DD HH:MM)",
#                     id = "datetime"),
#
#                 orientation = "vertical",
#                 spacing = dp(10),
#                 size_hint_y = None,
#                 height = dp(150)
#             ),
#             buttons = [
#                 MDFlatButton(
#                     text = "Cancel", on_release = lambda x: self.dialog.dismiss()
#                 ),
#                 MDRaisedButton(
#                     text = "Save", on_release = self.save_reminder
#                 ),
#             ],
#         )
#         self.dialog.open()
#     def save_reminders(self, *args):
#         content = self.dialog.content_cls.children[::-1]
#         title = content[0].text.strip()
#         dt_text = content[1].text.strip()
#
#         if title and dt_text:
#             try:
#                 reminder_time = datetime.strptime(dt_text, "%Y-%m-%d %H:%M")
#                 self.reminders.append((title, reminder_time, False))
#                 self.update_reminders_list()
#                 self.dialog.dismiss()
#             except ValueError:
#                 Snackbar(
#                     text = "Invalid format! Use YYYY-MM-DD HH:MM"
#                 ).open()
#             else:
#                 Snackbar(
#                     text = "Please fill in all fields"
#                 ).open()
#     def update_reminders_list(self):
#         self.list_container.clear_widgets()
#         for title, dt, _ in self.reminders:
#             item = OneLineListItem(
#                  text = f"{title} - {dt.strftime('%Y-%m-%d %H:%M')}",
#                  on_release = lambda x , t=title: self.delete_reminder(t)
#                 )
#             self.list_container.add_widget(item)
#
#     def delete_reminder(self,title):
#         self.reminders = [r for r in self.reminders if r[0] != title]
#         self.update_reminders_list()
#
#     def check_reminders(self, dt):
#         """Check if any reminders are due and show a notifications."""
#         now = datetime.now()
#         for title, remind_time, alerted in self.reminders:
#             if not alerted and now >= remind_time:
#                 self.reminders = [(t , r , True if  t==title else a) for t,r,a in self.reminders]
#                 Snackbar(text = f" Reminder: {title}").open()
#
#     class ReminderApp(MDApp):
#         def build(self):
#             return RemindersScreen()
#
#     if __name__ == "__main__":
#         ReminderApp().run()

from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from datetime import datetime


class RemindersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Store reminders: (title, datetime, alerted)
        self.reminders = []
        self.dialog = None

        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(10)
        )

        # Header
        header = MDLabel(
            text="Set Reminders",
            halign="center",
            font_style="H5"
        )
        layout.add_widget(header)

        # Reminder list container
        self.list_container = MDBoxLayout(
            orientation="vertical",
            spacing=dp(5)
        )
        layout.add_widget(self.list_container)

        # Buttons
        btn_box = MDBoxLayout(
            size_hint_y=None,
            height=dp(50),
            spacing=dp(10)
        )
        add_btn = MDRaisedButton(
            text="Add Reminder",
            on_release=self.add_reminder_dialog
        )
        back_btn = MDFlatButton(
            text="Back",
            on_release=self.go_back
        )
        btn_box.add_widget(back_btn)
        btn_box.add_widget(add_btn)
        layout.add_widget(btn_box)

        self.add_widget(layout)

        # Schedule notification check every minute
        Clock.schedule_interval(self.check_reminders, 60)

    def add_reminder_dialog(self, *args):
        """Open dialog to add a new reminder."""
        title_field = MDTextField(hint_text="Reminder Title")
        datetime_field = MDTextField(hint_text="Date & Time (YYYY-MM-DD HH:MM)")

        content = MDBoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None,
            height=dp(150)
        )
        content.add_widget(title_field)
        content.add_widget(datetime_field)

        self.dialog = MDDialog(
            title="New Reminder",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="Save",
                    on_release=lambda x: self.save_reminder(title_field.text, datetime_field.text)
                ),
            ],
        )
        self.dialog.open()

    def save_reminder(self, title, dt_text):
        """Save the new reminder from dialog input."""
        title = title.strip()
        dt_text = dt_text.strip()

        if not title or not dt_text:
            Snackbar(text="Please fill in all fields").open()
            return

        try:
            reminder_time = datetime.strptime(dt_text, "%Y-%m-%d %H:%M")
        except ValueError:
            Snackbar(text="Invalid format! Use YYYY-MM-DD HH:MM").open()
            return

        self.reminders.append((title, reminder_time, False))
        self.update_reminders_list()
        self.dialog.dismiss()
        Snackbar(text="Reminder added!").open()

    def update_reminders_list(self):
        """Refresh displayed reminders."""
        self.list_container.clear_widgets()
        for title, dt, _ in self.reminders:
            item = OneLineListItem(
                text=f"{title} - {dt.strftime('%Y-%m-%d %H:%M')}",
                on_release=lambda x, t=title: self.delete_reminder(t)
            )
            self.list_container.add_widget(item)

    def delete_reminder(self, title):
        """Delete a reminder when tapped."""
        self.reminders = [r for r in self.reminders if r[0] != title]
        self.update_reminders_list()
        Snackbar(text=f"Deleted reminder: {title}").open()

    def check_reminders(self, dt):
        """Check if any reminders are due and show a notification."""
        now = datetime.now()
        for i, (title, remind_time, alerted) in enumerate(self.reminders):
            if not alerted and now >= remind_time:
                Snackbar(text=f"⏰ Reminder: {title}").open()
                self.reminders[i] = (title, remind_time, True)

    def go_back(self, *args):
        """Placeholder for navigation (go back to another screen)."""
        Snackbar(text="Going back...").open()


class ReminderApp(MDApp):
    def build(self):
        return RemindersScreen()


if __name__ == "__main__":
    ReminderApp().run()
