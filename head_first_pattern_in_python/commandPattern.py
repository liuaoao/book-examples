# Chapter 6: Remote Control Test

# items
class Light():

    def __init__(self, location):
        self.location = location

    def on(self):
        print('%s Light is on' %self.location)

    def off(self):
        print('%s Light is off.' %self.location)

class GarageDoor():

    def open(self):
        print('Garage door is opened')

    def close(self):
        print('Garage door is closed')

class Stereo():

    def playWithCD(self):
        print('Stereo is playing with CD.')

    def off(self):
        print('Stereo is off')

class CellingFan():

    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0
    location = str
    speed = int

    def __init__(self, location):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print('%s celling fan is on high.' %self.location)

    def medium(self):
        self.speed = self.MEDIUM
        print('%s celling fan is on medium.' %self.location)

    def low(self):
        self.speed = self.LOW
        print('%s celling fan is on low.' %self.location)

    def off(self):
        self.speed = self.OFF
        print('%s celling fan is off.' % self.location)

    def getSpeed(self):
        return self.speed


# command
class Command():

    def execute(self):
        pass

class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class GarageDoorOpenCommand(Command):

    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.open()

    def undo(self):
        self.garageDoor.close()

class GarageDoorCloseCommand(Command):

    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.close()

    def undo(self):
        self.garageDoor.open()

class StereoPlayWithCDCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.playWithCD()

    def undo(self):
        self.stereo.off()

class StereoOffCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.playWithCD()

class CellingHighCommand(Command):
    prevSpeed = int

    def __init__(self, cellingFan):
        self.cellingFan = cellingFan

    def execute(self):
        self.prevSpeed = self.cellingFan.getSpeed()
        self.cellingFan.high()

    def undo(self):
        if self.prevSpeed == self.cellingFan.HIGH:
            self.cellingFan.high()
        elif self.prevSpeed == self.cellingFan.MEDIUM:
            self.cellingFan.medium()
        elif self.prevSpeed == self.cellingFan.LOW:
            self.cellingFan.low()
        elif self.prevSpeed == self.cellingFan.OFF:
            self.cellingFan.off()

class CellingMediumCommand(Command):
    prevSpeed = int

    def __init__(self, cellingFan):
        self.cellingFan = cellingFan

    def execute(self):
        self.prevSpeed = self.cellingFan.getSpeed()
        self.cellingFan.medium()

    def undo(self):
        if self.prevSpeed == self.cellingFan.HIGH:
            self.cellingFan.high()
        elif self.prevSpeed == self.cellingFan.MEDIUM:
            self.cellingFan.medium()
        elif self.prevSpeed == self.cellingFan.LOW:
            self.cellingFan.low()
        elif self.prevSpeed == self.cellingFan.OFF:
            self.cellingFan.off()

class CellingLowCommand(Command):
    prevSpeed = int

    def __init__(self, cellingFan):
        self.cellingFan = cellingFan

    def execute(self):
        self.prevSpeed = self.cellingFan.getSpeed()
        self.cellingFan.low()

    def undo(self):
        if self.prevSpeed == self.cellingFan.HIGH:
            self.cellingFan.high()
        elif self.prevSpeed == self.cellingFan.MEDIUM:
            self.cellingFan.medium()
        elif self.prevSpeed == self.cellingFan.LOW:
            self.cellingFan.low()
        elif self.prevSpeed == self.cellingFan.OFF:
            self.cellingFan.off()

class CellingOffCommand(Command):
    prevSpeed = int

    def __init__(self, cellingFan):
        self.cellingFan = cellingFan

    def execute(self):
        self.prevSpeed = self.cellingFan.getSpeed()
        self.cellingFan.off()

    def undo(self):
        if self.prevSpeed == self.cellingFan.HIGH:
            self.cellingFan.high()
        elif self.prevSpeed == self.cellingFan.MEDIUM:
            self.cellingFan.medium()
        elif self.prevSpeed == self.cellingFan.LOW:
            self.cellingFan.low()
        elif self.prevSpeed == self.cellingFan.OFF:
            self.cellingFan.off()

class noCommand(Command):

    def __init__(self):
        print('no command.')


# party
class MacroCommand(Command):

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()

# remote control
class RemoteControl():
    onCommands = []
    offCommands = []
    undoCommand = Command()

    def __init__(self):
        nocommand = noCommand()
        for i in range(7):
            self.onCommands.append(nocommand)
            self.offCommands.append(nocommand)

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPush(self):
        self.undoCommand.undo()

# test
def RemoteLoader():
    remoteControl = RemoteControl()

    living_room_light = Light('Living Room')
    kitchen_light = Light('Kitchen')
    living_room_celling_fan = CellingFan('Living Room')
    bedroom_celling_fan = CellingFan('Bed Room')
    garage_door = GarageDoor()
    stereo = Stereo()

    lightOn, lightOff = LightOnCommand(living_room_light), LightOffCommand(living_room_light)
    k_lightOn, k_lightOff = LightOnCommand(kitchen_light), LightOffCommand(kitchen_light)
    stereoOn, stereoOff = StereoPlayWithCDCommand(stereo), StereoOffCommand(stereo)
    doorOpen, doorClose = GarageDoorOpenCommand(garage_door), GarageDoorCloseCommand(garage_door)
    fanOn, fanOff = CellingHighCommand(living_room_celling_fan), CellingOffCommand(living_room_celling_fan)
    b_fanOn, b_fanOff = CellingHighCommand(bedroom_celling_fan), CellingOffCommand(bedroom_celling_fan)

    remoteControl.setCommand(0, lightOn, lightOff)
    remoteControl.setCommand(1, k_lightOn, k_lightOff)
    remoteControl.setCommand(2, doorOpen, doorClose)
    remoteControl.setCommand(3, stereoOn, stereoOff)
    remoteControl.setCommand(4, fanOn, fanOff)
    remoteControl.setCommand(5, b_fanOn, b_fanOff)

    go_home_commands = [lightOn, doorOpen, fanOn]
    leave_home_commands = [lightOff, doorClose, fanOff]

    go_home_macro = MacroCommand(go_home_commands)
    leave_home_macro = MacroCommand(leave_home_commands)

    remoteControl.setCommand(6, go_home_macro, leave_home_macro)

    # testing...
    remoteControl.onButtonWasPushed(0)
    remoteControl.onButtonWasPushed(5)
    remoteControl.offButtonWasPushed(5)
    remoteControl.offButtonWasPushed(0)

    print('----go home-----')
    remoteControl.onButtonWasPushed(6)
    print('----leave home----')
    remoteControl.offButtonWasPushed(6)

if __name__ == '__main__':
    RemoteLoader()


