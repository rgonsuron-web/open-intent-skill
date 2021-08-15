from mycroft import MycroftSkill, intent_file_handler


class OpenIntent(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('intent.open.intent')
    def handle_intent_open(self, message):
        self.speak_dialog('intent.open')


def create_skill():
    return OpenIntent()

