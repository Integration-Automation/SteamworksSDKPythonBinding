from steamworks.exceptions import *


class SteamInput:
    def __init__(self, steam: object):
        self.steam = steam
        if not self.steam.loaded():
            raise SteamNotLoadedException('STEAMWORKS not yet loaded')

    def init(self, explicitlyCallRunFrame=False):
        return self.steam.ControllerInit(explicitlyCallRunFrame)

    def run_frame(self):
        return self.steam.RunFrame()

    def get_connected_controllers(self) -> list[int]:
        controllers_array = self.steam.GetConnectedControllers()
        return [controller for i in range(16) if (controller := controllers_array[i]) != 0]

    def get_controller_for_gamepad_index(self, index: int) -> int:
        return self.steam.GetControllerForGamepadIndex(index)

    def get_action_set_handle(self, name: str) -> int:
        return self.steam.GetActionSetHandle(name.encode('ascii'))

    def activate_action_set(self, controller, action_set):
        return self.steam.ActivateActionSet(controller, action_set)

    def get_analog_action_handle(self, name: str) -> int:
        return self.steam.GetAnalogActionHandle(name.encode('ascii'))

    def get_analog_action_data(self, controller, analog_action):
        return self.steam.GetAnalogActionData(controller, analog_action)

    def get_digital_action_handle(self, name: str) -> int:
        return self.steam.GetDigitalActionHandle(name.encode('ascii'))

    def get_digital_action_data(self, controller, digital_action):
        return self.steam.GetDigitalActionData(controller, digital_action)
