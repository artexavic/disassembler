import string
import os
import commands

class disasembler():
    def __init__(self):
        self.commandsMask: list[str] = []
        self.commands: list[str] = []
        self.commandWords: list[str] = []
        self.fill_commands_lists()

    def fill_commands_lists(self):
        file = commands.commands
        for line in file.split("\n"):
            line = line.strip()
            line: str = line.strip()
            self.commandsMask.append(line[0:line.find('-')])
            self.commands.append(line[line.find('-') + 1:len(line)])

    def make_asm_code(self, input_hex, only_data: bool) -> str:
        self.fill_command_words(input_hex, only_data)
        return self.make_out()
        

    def fill_command_words(self, input_hex: str, only_data: bool) -> None:
        self.commandWords = []
        for line in input_hex.split("\n"):
            currentLine = ""
            for char in line:
                if char in string.hexdigits:
                    currentLine += char
            if not only_data:
                currentLine = currentLine[8:-2]
            if currentLine != '':
                for i in range(len(currentLine) // 4): #invert bytes
                    self.commandWords.append(currentLine[i * 4 + 2:i * 4 + 4] 
                                             + currentLine[i * 4:i * 4 + 2]) #big endian

    def invert_word_to_bin(self, invertWord: str) -> str:
        currCommand = ""
        for char in invertWord:
            currCommand += f"{int(char, 16):04b}"
        return currCommand

    def check_word(self, word: str) -> dict:
        currCommand: str = self.invert_word_to_bin(word)
        bestEquals: int = 0
        out = {'cmd': -1}
        for commandId in range(len(self.commandsMask)):
            currentEquals: int = 0
            currMask = self.commandsMask[commandId]
            isEqual: bool = True
            currOut = {'cmd': commandId}
            for bit in range(0, 16):
                if currMask[bit] != '0' and currMask[bit] != '1':
                    if not currMask[bit] in currOut:
                        currOut[currMask[bit]] = ""
                    currOut[currMask[bit]] += str(currCommand[bit])
                    continue
                if currMask[bit] != currCommand[bit]:
                    isEqual = False
                    break
                currentEquals += 1
            if isEqual:
                if currentEquals > bestEquals:
                    bestEquals = currentEquals
                    out = currOut
        return out

    def makeCommand(self, data: dict) -> str:
        command_str = self.commands[data['cmd']]
        if 'r' in data:
            r = data['r']
            if len(r) < 5:
                r = f"r{int(r, 2)+16}"
            else:
                r = f"r{int(r, 2)}"  # r + int
            command_str = command_str.replace('Rr', r)
        if 'd' in data:
            d = data['d']
            if len(d) < 5:
                d = f"r{int(d, 2)+16}"
            else:
                d = f"r{int(d, 2)}" # r + int
            command_str = command_str.replace('Rd', d)
        if 'K' in data:
            K = int(data['K'], 2)
            K = "0x" + f"{K:02x}" #some hex number constant
            command_str = command_str.replace('K', K)
        if 'k' in data:
            if data['cmd'] in (0, 3):  # JMP, CALL
                k = "0x" + f"{int(data['k'], 2) * 2:02x}"
            elif data['cmd'] in (1, 2):  # LDS, STS
                k = "0x" + f"{int(data['k'], 2):02x}"
            else:
                if data['k'][0] == '1': # if first digit is 1 then its negative jump
                    inverted = ''
                    for char in data['k']:
                        if char == '0':
                            inverted += '1'
                        else:
                            inverted += '0'
                    k = f"-{(int(inverted, 2) + 1) * 2}"
                else:
                    k = f"+{int(data['k'] + '0', 2)}"
            command_str = command_str.replace('k', k)
        if 'b' in data:
            b = int(data['b'], 2) #bit (0-7) in register
            command_str = command_str[0:command_str.find(' ')] + command_str[command_str.find(' '):].replace('b', str(b))
        if 'P' in data:
            P = int(data['P'], 2)
            P = "0x" + f"{P:02x}" #hex number port
            command_str = command_str.replace('P', P)
        if 'q' in data:
            q = int(data['q'], 2)
            command_str = command_str.replace('q', str(q))
        if 's' in data: #bit (0-7) in SREG
            s = int(data['s'], 2)
            command_str = command_str.replace('s', str(s))
        return command_str

    def make_out(self) -> str:
        words = self.commandWords
        wordId = 0
        file = ""
        while wordId < len(words):
            res = self.check_word(words[wordId])
            currComandId = res['cmd']
            currLine = f"0x{wordId*2:04x}: " #make address in hex format for output
            currLine += f"{words[wordId][2:4]} {words[wordId][0:2]} " #invert to little-endian for output
            if currComandId == -1:
                currLine += "command not found\n"
                wordId += 1
            else:
                if len(self.commandsMask[currComandId]) == 32:
                # if currComandId in [0, 1, 2, 3]: # 2-words commands 
                    if not 'k' in res: # special for lds and sts commands
                        res['k'] = ''
                    res['k'] += self.invert_word_to_bin(words[wordId + 1]) # add second part
                    currLine += f"{words[wordId + 1][2:4]} {words[wordId + 1][0:2]} " #add second word to output
                    wordId += 2 # skip 1 word, because its part of current command 
                else:
                    currLine += "      "
                    wordId += 1
                currLine += f"   {self.makeCommand(res)}\n" # make a normal asm command for output
            file += currLine # add to file
        return file