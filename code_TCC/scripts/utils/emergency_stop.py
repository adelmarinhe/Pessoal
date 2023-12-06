from pynput import keyboard


class EmergencyStop:
    def __init__(self, base, data, return_function, save_function, base_cyclic):
        """
        This function is used to initialize the base object of the robot and simplify the object manipulate.
        Arguments:
            base: base object of the robot
        """
        self.base = base
        self.data = data
        self.return_function = return_function
        self.save_function = save_function
        self.base_cyclic = base_cyclic  # TODO: Use partial functions to remove this attr

    def on_press(self, key):
        """
        This function is used to stop the robot in case of emergency stop when the space bar is pressed.
        """
        if str(key) == 'Key.space':
            self.base.ApplyEmergencyStop()
            self.save_function(self.return_function(self.base_cyclic, self.data))

    def emergency_stop(self):
        """
        This function is used to stop the robot in case of emergency stop.

        This function calls the function on_press when any key is pressed,
        but the emergency stop is trigger when the space bar is pressed.
        """
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
