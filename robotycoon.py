from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class FactoryScreen(Screen):
    pass



class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        # Load KV and return the root widget (MyScreenManager)
        return Builder.load_file("robotycoon.kv")

if __name__ == "__main__":
    MyApp().run()
