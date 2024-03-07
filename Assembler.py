import sys

inputfile = open(r"inputfile.txt") 
outputfile = open("outputbinary.txt","w")

# creating a list of all lines in input txt file, each element in lines is a line
lines_unrefined = inputfile.readlines() 
lines = [line.strip() for line in lines_unrefined]




global instrCounter
global stackCounter
global dataMemoryCounter

PrgC = 0 # Program Counter
PrgCMax = len(lines) -1

instrCounter = 0 #for tracking the numbers of instructions assembled don't exceed program memory
stackCounter = 32 #for tracking variables don't exceed stack memory, we have only 32 registers
dataMemoryCounter = 0 # don't know for now



# register type instructions
R_type_instr = ['add','sub','slt','sltu','xor','sll','srl','or','and'] 
# immediate type instructions
I_type_instr = ['lw','addi','sltiu','jalr']
# s type instructions
S_type_instr = ['sw']
# branch type instructions
B_type_instr = ['beq','bne','blt','bge','bltu','bgeu']
# unsigned type instructions
U_type_instr = ['lui','auipc']
# j type instructions
J_type_instr = ['jal']
# bonus instructions
Bonus_instr = ['mul','rst','halt','rvrs']

# register encodings in dict (ABI:Address)

registers_dict = {
    'zero': '00000',
    'ra':   '00001',
    'sp':   '00010',
    'gp':   '00011',
    'tp':   '00100',
    't0':   '00101',
    't1':   '00110',
    't2':   '00111',
    's0':   '01000',
    's1':   '01001',
    'a0':   '01010',
    'a1':   '01011',
    'a2':   '01100',
    'a3':   '01101',
    'a4':   '01110',
    'a5':   '01111',
    'a6':   '10000',
    'a7':   '10001',
    's2':   '10010',
    's3':   '10011',
    's4':   '10100',
    's5':   '10101',
    's6':   '10110',
    's7':   '10111',
    's8':   '11000',
    's9':   '11001',
    's10':   '11010',
    's11':   '11011',
    't3':   '11100',
    't4':   '11101',
    't5':   '11110',
    't6':   '11111',
}

labels_dict = {} 
#empty dict for storing label:PC values here (Note PC has hex range from 00 to ff i.e 0 to 255 bytes each instruction consuming 4 bytes)

func3_dict = {
    'add': '000',
    'sub': '000',
    'sll': '001',
    'slt': '010',
    'sltu': '011',
    'xor': '100',
    'srl': '101',
    'or': '110',
    'and': '111',
    'lw': '010',
    'addi': '000',
    'sltiu': '011',
    'jalr': '000',
    'sw': '010',
    'beq': '000',
    'bne': '001',
    'blt': '100',
    'bge': '101',
    'bltu': '110',
    'bgeu': '111'
}


def R_type_encoder(token_1):
    op_code = '0110011'
    op_name = token_1[0]
    func3 = func3_dict[op_name]
    token_2 = token_1[1].split(",")
    rd = registers_dict[token_2[0]]
    rs1 = registers_dict[token_2[1]]
    rs2 = registers_dict[token_2[2]]
    if op_name == 'sub':
        func7 = '0100000'
    else:
        func7 = '0000000'

    binstr = func7 + rs2 + rs1 + func3 + rd + op_code + '\n'
    outputfile.write(binstr)
    global PrgC
    PrgC = PrgC + 1



def I_type_encoder(token_1):
    
    

def S_type_encoder(token_1):
    pass

def B_type_encoder(token_1):
    pass

def U_type_encoder(token_1):
    pass

def J_type_encoder(token_1):
    pass

def Label_type_encoder(opname,token_1):
    label = opname[0:-1]
    if label in labels_dict:
        print("Error:Redefining already used label")
        sys.exit()
    else:
        labels_dict.update({opname:PrgC})
    token_1.remove(opname)
    new_line = token_1.join()
    instr_identifier(new_line)


def instr_identifier(line):
    
    token_1 = line.split()
    opname = token_1[0]
    if opname[-1] == ":":
        Label_type_encoder(opname,token_1)
    elif opname in R_type_instr:
        R_type_encoder(token_1)
    elif opname in I_type_instr:
        I_type_encoder(token_1)
    elif opname in S_type_instr:
        S_type_encoder(token_1)
    elif opname in B_type_instr:
        B_type_encoder(token_1)
    elif opname in U_type_instr:
        U_type_encoder(token_1)
    elif opname in J_type_instr:
        J_type_encoder(token_1)
    else:
        print("Invalid instruction code on line",PrgC)
        sys.exit()




    

    



while(PrgC <= PrgCMax):
    line = lines[PrgC]
    if(line == ""):
        PrgC = PrgC+1
        continue
    instr_identifier(line)



#dekh lenge iske logic bad me ek to last line of output file pr if lgake bhi check kr skte h
print("Error: Virtual halt not used as last instruction")
sys.exit(-1)








