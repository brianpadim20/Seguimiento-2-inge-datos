class AbstractChannel(ABC):

    def get_channel_message(self) -> str:
        pass

class AbstractCommunicator(ABC):

    def get_channel(self) -> AbstractChannel:
        pass

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
            self.get_channel().get_channel_message(),
            sep = '\n')

class SMSChannel(AbstractChannel):

    def get_channel_message(self) -> str:
        return "(via SMS)"

class SMSCommunicator(AbstractCommunicator):  

    def __init__(self):
        self._channel = SMSChannel()

    def get_channel(self) -> AbstractChannel:
        return self._channel