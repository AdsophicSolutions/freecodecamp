class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        
        output = []
        for s in strs: 
            if not s: 
                output.append('e')
                continue
            line = []   
            for c in s: 
                line.append(str(ord(c)))
            output.append("|".join(line))
        
        return "*".join(output)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        output = []
        for line in s.split('*'):
            if line == 'e': 
                output.append('')
                continue 
            rec_string = []
            for c_value in line.split('|'): 
                rec_string.append(chr(int(c_value)))
            output.append(''.join(rec_string))
        
        return output 
        

# Your Codec object will be instantiated and called as such:

if __name__ == '__main__':
    codec = Codec()
    coded_string = codec.encode(["",""])    
    result = codec.decode(coded_string)
    print(result)