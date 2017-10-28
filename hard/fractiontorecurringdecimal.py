class SolutionFTD(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator:
            return ''
        
        is_result_negative = (numerator < 0) != (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        integer_part = str(numerator // denominator)
        
        remainder = numerator % denominator
        if not remainder:
            return (integer_part 
                    if not is_result_negative or integer_part == '0' 
                    else '-' + integer_part)
        
        if is_result_negative: 
            integer_part = "-" + integer_part 
            
        decimals = []
        remainders = {}
        is_repeated = False
         
        while remainder: 
            if str(remainder) in remainders: 
                is_repeated = True
                break 
            
            remainders[str(remainder)] = len(decimals)
            remainder *= 10 
            if remainder < denominator:                 
                decimals.append('0')
            else: 
                decimals.append(str(remainder // denominator))                
                remainder %= denominator
        
        if not is_repeated:
            return integer_part + '.' + ''.join(decimals)
        else: 
            repeat_index = remainders[str(remainder)] 
            return (
                integer_part + '.' + 
                ''.join(decimals[:repeat_index]) + '(' + 
                ''.join(decimals[repeat_index:]) + ')')   

if __name__ == '__main__':
    s = SolutionFTD()
    print(s.fractionToDecimal(-50, 8))