from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
import webbrowser




class App(MDApp):
    def calculate(self,args):
        if self.input_w.text == '' or self.input_h.text == '':
            self.calculated.text = 'One or more fields are empty !'
        else:
            try:
                val=float(self.input_w.text) / float(self.input_h.text)**2
                self.calculated.text=str(round(val,2))

            except ValueError:
                self.calculated.text = 'Wrong input please try again !'


    def github(self):
        webbrowser.open_new('https://github.com/Shakil-Mahmud-Programmer')

    def facebook(self):
        webbrowser.open_new_tab('https://www.facebook.com/profile.php?id=100036971298466')

    def build(self):
        self.screen = MDScreen()
        self.title='BMI'
        self.toolbar = MDToolbar(title='Body Mass Index Calculator')
        self.toolbar.pos_hint={'top':1}
        self.toolbar.right_action_items=[['github',lambda g: self.github()],['facebook',lambda f:self.facebook()]]
        self.screen.add_widget(self.toolbar)
        self.label1=MDLabel(text='Weight(kg)',size_hint=(0.1,0.2),pos_hint={'center_x':0.39,'center_y':0.8})
        self.screen.add_widget(self.label1)
        self.input_w=MDTextField(size_hint=(0.1,0.2),pos_hint={'center_x':0.5,'center_y':0.8})
        self.screen.add_widget(self.input_w)

        self.label2 = MDLabel(text='Height(m)', size_hint=(0.1, 0.2), pos_hint={'center_x': 0.40, 'center_y': 0.7})
        self.screen.add_widget(self.label2)
        self.input_h = MDTextField(size_hint=(0.1, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.screen.add_widget(self.input_h)

        self.im=Image(source='bmi.png',size_hint=(0.3, 0.3), pos_hint={'center_x': 0.46, 'center_y': 0.5})
        self.screen.add_widget(self.im)

        self.label3=MDLabel(text='BMI:',pos_hint={'center_x': 0.9, 'center_y': 0.3})
        self.screen.add_widget(self.label3)

        self.calculated = MDLabel( pos_hint={'center_x': 0.95, 'center_y': 0.3})
        self.screen.add_widget(self.calculated)

        self.developer = MDLabel(text='Developed By Shakil Mahmud',font_size=10,pos_hint={'center_x': 1, 'center_y': 0.1 })
        self.screen.add_widget(self.developer)


        self.cal=MDFillRoundFlatButton(text='Calculate',font_size=15,on_press=self.calculate,pos_hint={'center_x':0.7, 'center_y':0.7})
        self.screen.add_widget(self.cal)

        return self.screen


if __name__=='__main__':
    App().run()