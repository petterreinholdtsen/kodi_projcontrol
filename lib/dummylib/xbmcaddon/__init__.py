#
class Addon():
    _settings = {
        'manufacturer' : 'InFocus',
        'infocus_model' : 'IN72/IN74/IN76',
        'device' : '/dev/ttyUSB0',
        'timeout' : 10,
        'set_input' : None,
        'input_source' : None,
        'lib_output' : 'false',
        }
    def getSetting(self, key):
        return self._settings[key]
