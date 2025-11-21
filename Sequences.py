class Sequence:

    # constructor
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()


    # getter and setter for id
    @property
    def id(self):
        return self._id 
    
    @property
    def seq(self):
        return self._seq
    
    def __str__(self):
        return f'sequence id  : {self.id},{self.seq}'
    def __len__ (self):
        return len(self.seq)

        # method to return fasta string
    def create_fasta(self):
       return f'>{self.id}\n{self.seq}\n'
    

class DNASequence(Sequence):
    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)

    # translate the sequence
    def translate_sequence(self):
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))
        translation = ''
        aa_list = [codon_table[self.seq[start:start+3]] for start in range(0,len(self.seq)-2,3)]
        translation =''.join(aa_list)
        return translation
    
    
    def get_protein_len(self):
        return len(self.seq) // 3 
    
    
class ProteinSequence(Sequence):
    def __init__ (self,id,seq,descr = ''):
        super().__init__(id,seq)
        self._descr = descr

    def descr (self):
        return self._descr
    
    def calculate_hydrophobic(self, dp=2):
        aa_list = ['A','I','L','M','F','W','Y','V']
        count = 0
        for base in self.seq:
            if base in aa_list:
                count += 1
        hydrophobic = (count/len(self.seq))*100
        return round(hydrophobic, dp)
    
   
    def get_protein_len(self):
        return len(self.seq)