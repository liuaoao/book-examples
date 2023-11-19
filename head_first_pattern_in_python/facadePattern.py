# Chapter 7: Being Adaptive

# subsystem
class Amplifier():

    def on(self):
        print('Amplifier is on.')

    def off(self):
        print('Amplifier is off.')

    def setCd(self):
        print('CD is set.')

    def setDvd(self):
        print('DVD is set.')

    def setStereoSound(self, sound):
        print('Stereo sound is set to %s' %sound)

    def setSurroundSound(self, sound):
        print('Surround sound is set to %s' %sound)

    def setTuner(self):
        print('Tuner is set.')

    def setVolume(self, volume):
        print('Volume is set to %s.' %volume)

class Tuner(Amplifier):

    def on(self):
        pass

    def off(self):
        pass

    def setAm(self):
        pass

    def setFm(self):
        pass

    def setFrequency(self):
        pass

class Screen():

     def up(self):
         print('Screen is up.')

     def down(self):
         print('Screen is down.')

class PopcornPopper():

    def on(self):
        print('PopcornPopper is on.')

    def off(self):
        print('PopcornPopper is off.')

    def pop(self):
        print('PopcornPopper is popping.')

class Cdplayer(Amplifier):

    def on(self):
        print('Cdplayer is on.')

    def off(self):
        print('Cdplayer is off.')

    def eject(self):
        print('Cdplayer is eject.')

    def pause(self):
        print('Cdplayer is pause.')

    def play(self):
        print('Cdplayer is playing.')

    def stop(self):     
        print('Cdplayer is stop.')

class TheaterLight():

    def on(self):
        print('Theater light is on.')

    def off(self):
        print('Theater light is off.')

    def dim(self, number):
        print('Theater light dims to %s.' %number)

class DvdPlayer(Amplifier):

    def on(self):
        print('Dvd player is on.')

    def off(self):
        print('Dvd player is off.')

    def eject(self):
        print('Dvd player is eject.')

    def pause(self):
        print('Dvd player is pause.')

    def play(self):
        print('Dvd player is playing.')

    def setSurroundAudio(self, sound):
        print('Dvd player surround audio sets to %s' %sound)

    def setTwoChannelAudio(self, sound):
        print('Dvd player two channel audio sets to %s' %sound)

    def stop(self):
        print('Dvd player is stop.')

class Projector(DvdPlayer):

    def on(self):
        print('Projector is on.')

    def off(self):
        print('Projector is off.')

    def tvMode(self):
        print('Projector tvMode is on.')

    def wideScreenMode(self):
        print('Projector wideScreenMode is on.')

# Facade!
class HomeTheaterFacade():

    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watchMovie(self):
        print('Get ready to watch a movie...')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDvd()
        self.amp.setSurroundSound(1)
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play()

    def endMovie(self):
        print('Shutting movie theater down...')
        self.popper.off()
        self.lights.off()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

if __name__ == '__main__':
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = Cdplayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLight()
    popper = PopcornPopper()

    facade = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)
    facade.watchMovie()
    facade.endMovie()