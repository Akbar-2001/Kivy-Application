from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class HomeScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class CoursesScreen(Screen):
    pass


class UgScreen(Screen):
    pass


class CseScreen(Screen):
    pass


class EeeScreen(Screen):
    pass


class EceScreen(Screen):
    pass


class PgScreen(Screen):
    pass


class FeeScreen(Screen):
    pass


class BtScreen(Screen):
    pass


class MtScreen(Screen):
    pass


class MbaScreen(Screen):
    pass


class BpScreen(Screen):
    pass


class MpScreen(Screen):
    pass


class AdministrationScreen(Screen):
    pass


class AdmissionprocedureScreen(Screen):
    pass


class LateralEntryScreen(Screen):
    pass


class BcategoryScreen(Screen):
    pass


class NRIScreen(Screen):
    pass


class JEEScreen(Screen):
    pass


class EamcetScreen(Screen):
    pass


class IntermediateVocationalPassoutScreen(Screen):
    pass


class CertificatesToBeSubmittedScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(CoursesScreen(name='course'))
sm.add_widget(UgScreen(name='ug'))
sm.add_widget(CseScreen(name='cse'))
sm.add_widget(EeeScreen(name='eee'))
sm.add_widget(EceScreen(name='ece'))
sm.add_widget(PgScreen(name='pg'))
sm.add_widget(FeeScreen(name='fee'))
sm.add_widget(BtScreen(name='bt'))
sm.add_widget(MtScreen(name='mt'))
sm.add_widget(MbaScreen(name='mba'))
sm.add_widget(BpScreen(name='bp'))
sm.add_widget(MpScreen(name='mp'))
sm.add_widget(AboutScreen(name='about'))
sm.add_widget(AdmissionprocedureScreen(name='ap'))
sm.add_widget(LateralEntryScreen(name='le'))
sm.add_widget(BcategoryScreen(name='bc'))
sm.add_widget(NRIScreen(name='nri'))
sm.add_widget(JEEScreen(name='jee'))
sm.add_widget(EamcetScreen(name='eamcet'))
sm.add_widget(IntermediateVocationalPassoutScreen(name='ivp'))
sm.add_widget(CertificatesToBeSubmittedScreen(name='certificates'))


class SNTI(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


screen_helper = """
ScreenManager:
    HomeScreen:
    MenuScreen:
    CoursesScreen:
    UgScreen:
    CseScreen:
    EeeScreen:
    EceScreen:
    PgScreen:
    FeeScreen:
    BtScreen:
    MtScreen:
    MbaScreen:
    BpScreen:
    MpScreen:
    AdministrationScreen:
    AdmissionprocedureScreen:
    LateralEntryScreen:
    BcategoryScreen:
    NRIScreen:
    JEEScreen:
    EamcetScreen:
    IntermediateVocationalPassoutScreen:
    CertificatesToBeSubmittedScreen:
    AboutScreen:



<HomeScreen>:
    name: 'home'
    MDRectangleFlatButton:
        text: 'SCIENT INSTITUTE OF TECHNOLOGY'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'menu'



<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Courses'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'course'

    MDRectangleFlatButton:
        text: 'Admission Procedure'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'ap'

    MDRectangleFlatButton:
        text: 'Administration'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'admin'

    MDRectangleFlatButton:
        text: 'Fee Structure'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'fee'

    MDRectangleFlatButton:
        text: 'About'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'about'

<CoursesScreen>:
    name: 'course'
    MDRectangleFlatButton:
        text: 'UG = under graduation'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'ug'

    MDRectangleFlatButton:
        text: 'PG = post graduation'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'pg'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<UgScreen>:
    name: 'ug'
    MDRectangleFlatButton:
        text: 'Computer Science of Engineering'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'cse'

    MDRectangleFlatButton:
        text: 'Electrical & Electronics Engineering'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'eee'

    MDRectangleFlatButton:
        text: 'Electronics & Communication Engineering'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'ece'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'course'

<CseScreen>:
    name: 'cse'
    MDLabel:
        text:str('Computer Science of Engineering Duration 4 Years Intake 120 seats')
        font_size: 30

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ug'

<EEEScreen>:
    name: 'eee'
    MDLabel:
        text:str('Electrical & Electronics Engineering Duration 4 Years Intake 120 seats')
        font_size: 30

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ug'

<EceScreen>:
    name: 'ece'
    MDLabel:
        text:str('Electrical & Electronics Engineering Duration 4 Years Intake 120 seats')
        font_size: 30

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ug'

<PgScreen>:
    name: 'pg'
    MDLabel:
        text:str('Master of Business Administration Duration 2 Years Intake 60 seats')
        font_size: 30


    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'course'

<FeeScreen>:
    name: 'fee'
    MDRectangleFlatButton:
        text: 'B tech'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'bt'

    MDRectangleFlatButton:
        text: 'M tech'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'mt'

    MDRectangleFlatButton:
        text: 'MBA'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'mba'

    MDRectangleFlatButton:
        text: 'B pharmacy'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'bp'

    MDRectangleFlatButton:
        text: 'M pharmacy'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'mp'


    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'menu'

<BtScreen>:
    name: 'bt'
    Image:
        source:'b.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'fee'

<MtScreen>:
    name: 'mt'
    Image:
        source:'mt.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'fee'

<MbaScreen>:
    name: 'mba'
    Image:
        source:'mba.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'fee'

<BpScreen>:
    name: 'bp'
    Image:
        source:'bp.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'fee'

<MpScreen>:
    name: 'mp'
    Image:
        source:'mp.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'fee'

<AdministrationScreen>:
    name: 'admin'
    Image:
        source:'admin.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<AdmissionprocedureScreen>:
    name: 'ap'
    MDRectangleFlatButton:
        text: 'Lateral Entry'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current='le'

    MDRectangleFlatButton:
        text: 'Bcategory'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'bc'

    MDRectangleFlatButton:
        text: 'NRI'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current='nri'

    MDRectangleFlatButton:
        text: 'JEE'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current='jee'

    MDRectangleFlatButton:
        text: 'Eamcet'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current='eamcet'

    MDRectangleFlatButton:
        text: 'Intermediate Vocational Passout'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current='ivp'

    MDRectangleFlatButton:
        text: 'Certificates To Be Submitted'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current='certificates'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<LateralEntryScreen>:
	name: 'le'
	MDLabel:
	    text:str('20% of students are allotted for students who complete 3 years diploma to join in the 2nd year B.Tech') 
	    font_size:30 

	MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'



<IntermediateVocationalPassoutScreen>:
	name:'ivp'
	MDLabel:
	    text:str('intermediate vocational passouts must pass Mathematics Biology and Physical Sciences')
        font_size:30

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'

<CertificatesToBeSubmittedScreen>:
	name:'certificates'
	Image:
        source:'cps.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'

<BcategoryScreen>:
	name:'bc'
	Image:
        source:'bc.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'

<NRIScreen>:
	name:'nri'
	Image:
        source:'nri.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'

<JEEScreen>:
	name:'jee'
	Image:
        source:'jee.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'

<EamcetScreen>:
	name:'eamcet'
	Image:
        source:'eamcet.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'ap'

<AboutScreen>:
	name:'about'
	Image:
        source:'ABT.png'

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
"""

SNTI().run()
