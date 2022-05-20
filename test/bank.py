from bfv.batch_encoder import BatchEncoder
from bfv.int_encoder import IntegerEncoder
from bfv.bfv_decryptor import BFVDecryptor
from bfv.bfv_encryptor import BFVEncryptor
from bfv.bfv_evaluator import BFVEvaluator
from bfv.bfv_key_generator import BFVKeyGenerator
from bfv.bfv_parameters import BFVParameters

def main():

    degree = 2048
    plain_modulus = 256
    ciph_modulus = 0x3fffffff000001
    params = BFVParameters(poly_degree=degree,
                           plain_modulus=plain_modulus,
                           ciph_modulus=ciph_modulus)
    key_generator = BFVKeyGenerator(params)
    public_key = key_generator.public_key
    secret_key = key_generator.secret_key
    relin_key = key_generator.relin_key
    encoder = IntegerEncoder(params)
    encryptor = BFVEncryptor(params, public_key)
    decryptor = BFVDecryptor(params, secret_key)
    evaluator = BFVEvaluator(params)
    balance = 10000
    bal = encoder.encode(balance)
    ciph1 = encryptor.encrypt(bal)
    k=1
    while k!=0:
        print("Enter 1 To Deposit Money \nEnter 2 To View Balance \nEnter 3 To Exit")
        j=int(input())
        if j==1:
            print("Enter the amount to deposit")
            dep=int(input())
            deposit = encoder.encode(dep)
            ciph2 = encryptor.encrypt(deposit)
            ciph1 = evaluator.add(ciph1,ciph2)
            print("Amount successfully added to the account \n")
        elif j==2:
            decrypted_balance = decryptor.decrypt(ciph1)
            decoded_balance = encoder.decode(decrypted_balance)
            print("Current balance : "+str(decoded_balance)+"\n")
        elif j==3:
            k=0
        else:
            print("Please select a proper option")
            

if __name__ == '__main__':
    main()
