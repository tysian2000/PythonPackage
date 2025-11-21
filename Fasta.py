class Fasta:
    # constructor
    def __init__(self, file):
        self._file= file

    def file(self):
        return self._file

    def instance_DNA(self,sequence_class):
        with open(self._file) as filehandle:
            for line in filehandle:
                if line.startswith('>'):
                        id = line.lstrip('>').rstrip()
                        seq=filehandle.readline().rstrip()
                        yield sequence_class(id, seq)